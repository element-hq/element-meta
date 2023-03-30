const { Octokit } = require("@octokit/action");

const octokit = new Octokit();

const headers = { "GraphQL-Features": "projects_next_graphql" }

const REPO_OWNER = process.env.REPO_OWNER;
const REPO_NAME = process.env.REPO_NAME;
const ISSUE_NUMBER = parseInt(process.env.ISSUE_NUMBER);
const PROJECT_ID = process.env.PROJECT_ID;
const FIELD_ID = process.env.FIELD_ID;
const FIELD_NAME = process.env.FIELD_NAME;

(async function main() {
  // Query all the things via GraphQL
  const query = `query ($owner: String!, $repo: String!, $issueNumber: Int!, $fieldName: String!) {
    repository(owner: $owner, name: $repo) {
      issue(number: $issueNumber) {
        projectItems(first: 100) {
          edges {
            node {
              id
              fieldValueByName(name: $fieldName) {
                ... on ProjectV2ItemFieldSingleSelectValue {
                  optionId
                  name
                  field {
                    ... on ProjectV2SingleSelectField {
                      id
                    }
                  }
                }
              }
              project {
                id
              }
            }
          }
        }
        trackedIssues(first: 100) {
          edges {
            node {
              projectItems(first: 100) {
                edges {
                  node {
                    id
                    project {
                      id
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }`;

  const parameters = {
    owner: REPO_OWNER,
    repo: REPO_NAME,
    issueNumber: ISSUE_NUMBER,
    fieldName: FIELD_NAME,
    headers
  };

  console.log(JSON.stringify(query));
  console.log(JSON.stringify(parameters));

  const result = await octokit.graphql(query, parameters);
  console.log(JSON.stringify(result));

  // Check project membership and extract field value

  const projectItems = result.repository.issue.projectItems.edges;

  if (!projectItems) {
    console.log("Issue is not part of any projects");
    return;
  }

  let fieldValueId = null;
  let fieldValueName = null;

  for (const item of projectItems) {
    if (item.node.project.id == PROJECT_ID && item.node.fieldValueByName && item.node.fieldValueByName.field.id == FIELD_ID) {
      fieldValueId = item.node.fieldValueByName.optionId;
      fieldValueName = item.node.fieldValueByName.name;
      break;
    }
  }

  if (!fieldValueId || !fieldValueName) {
    console.log("Issue is not part of the correct project or does not have the field value set");
    return;
  }

  // Apply field value to tracked issues

  const trackedIssues = result.repository.issue.trackedIssues.edges;

  if (!trackedIssues) {
    console.log("Issue has no tracked issues");
    return;
  }

  for (const issue of trackedIssues) {
    const projectItems = issue.node.projectItems.edges;

    if (!projectItems) {
      continue; // TODO: Add tracked issue to project?
    }

    for (const item of projectItems) {
      if (item.node.project.id == PROJECT_ID) {
        const mutation = `mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
          updateProjectV2ItemFieldValue(
            input: {
              projectId: $projectId
              itemId: $itemId
              fieldId: $fieldId
              value: { 
                singleSelectOptionId: $optionId        
              }
            }
          ) {
            projectV2Item {
              id
            }
          }
        }`;

        const parameters = {
          projectId: PROJECT_ID,
          itemId: item.node.id,
          fieldId: FIELD_ID,
          optionId: fieldValueId,
          headers
        };

        const result = await octokit.graphql(mutation, parameters);
        console.log(`Set field value on ${JSON.stringify(result)}`);

        break;
      }
    }
  }
})();
