import fs from "fs";
import { Command } from "commander";
import githubLabelSync, { LabelInfo } from "github-label-sync";
import YAML from "yaml";

const cmd = new Command("sync-labels.ts")
  .option('--labels <path...>')
  .parse();
const opts = cmd.opts();

const merged = new Map<string, LabelInfo>();

for (const path of opts.labels) {
  const labels = YAML.parse(fs.readFileSync(path, "utf-8")) as [LabelInfo];
  for (const label of labels) {
    if (!label.name) {
      console.warn(`Ignoring invalid label without a name: ${label}`);
      continue;
    }
    if (merged.has(label.name)) {
      console.log(`Overriding label ${label.name} from ${path}`);
    } else {
      console.log(`Importing label ${label.name} from ${path}`);
    }
    merged.set(label.name, label);
  }
}

githubLabelSync({
  accessToken: process.env.GITHUB_TOKEN!,
  repo: process.env.GITHUB_REPO!,
  labels: [...merged.values()],
  dryRun: true, // TODO: Remove this once we know this thing actually works
}).then(diff => console.log(`Updated labels with diff: ${JSON.stringify(diff)}`)).catch(error => {
  console.error(error);
});
