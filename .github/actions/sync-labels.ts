import fs, { stat } from "fs";
import { Command } from "commander";
import githubLabelSync, { LabelDiff, LabelInfo } from "github-label-sync";
import github from "octonode";
import YAML from "yaml";

main();

async function main() {
  const accessToken = process.env.GITHUB_TOKEN!;
  const repo = process.env.GITHUB_REPOSITORY!;
  console.log(`Repository: ${repo}`);
  
  const cmd = new Command("sync-labels.ts")
    .option('--labels <path...>')
    .parse();
  const opts = cmd.opts();
  console.log(`Input files: ${opts.labels}`);
  
  const merged = new Map<string, LabelInfo>();
  
  for (const arg of opts.labels) {
    console.log(`Loading labels from ${arg}`);
    const labels = fs.existsSync(arg) ? readLabelsFromFile(arg) : await readLabelsFromRepo(arg, accessToken);
    if (!labels) {
      continue;
    }
  
    for (const label of labels) {
      if (!label.name) {
        console.warn(`Ignoring invalid label without a name: ${label}`);
        continue;
      }
      if (merged.has(label.name)) {
        console.log(`Overriding label ${label.name}`);
      } else {
        console.log(`Importing label ${label.name}`);
      }
      merged.set(label.name, label);
    }
  }

  githubLabelSync({
    accessToken,
    repo,
    labels: [...merged.values()],
    dryRun: true, // TODO: Remove this once we know this thing actually works
  }).then((diffs: LabelDiff[]) => {
    console.log(`Label sync completed ${diffs.length ? "with" : "without"} changes`);
    for (const diff of diffs) {
      console.log(`${diff.type} ${diff.name}`);
      if (diff.expected?.description != diff.actual?.description) {
        console.log(`  description (actual)   - ${diff.actual?.description}`);
        console.log(`  description (expected) - ${diff.expected?.description}`);
      }
      if (diff.expected?.color != diff.actual?.color) {
        console.log(`  color (actual)   - ${diff.actual?.color}`);
        console.log(`  color (expected) - ${diff.expected?.color}`);
      }
    }
  }).catch(error => {
    console.error(error);
    throw error;
  });
  
}

function readLabelsFromFile(file: string): LabelInfo[] {
  const content = fs.readFileSync(file, "utf-8");
  return YAML.parse(content) as [LabelInfo];
}

async function readLabelsFromRepo(slug: string, accessToken: string): Promise<LabelInfo[]> {
  const client = github.client(accessToken);

  const labels: LabelInfo[] = [];
  const params = { page: 1, per_page: 100 };

  while (true) {
    const [status, chunk] = await client.getAsync(`/repos/${slug}/labels`, params);
    if (status !== 200) {
      throw `Fetching labels failed: ${status}`;
    }

    for (const item of chunk) {
      labels.push({
        name: item.name,
        description: item.description ?? "",
        color: item.color,
      })
    }

    if (labels.length !== params.per_page) {
      break;
    }
    
    params.page += 1;
  }

  return labels;
}
