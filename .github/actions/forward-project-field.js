const { Octokit } = require("@octokit/action");

const octokit = new Octokit();

const headers = { "GraphQL-Features": "projects_next_graphql" }

const REPO_OWNER = process.env.REPO_OWNER;
const REPO_NAME = process.env.REPO_NAME;
const ISSUE_NUMBER = parseInt(process.env.ISSUE_NUMBER);
const PROJECT_ID = process.env.PROJECT_ID;
const FIELD_ID = process.env.FIELD_ID;
const FIELD_NAME = process.env.FIELD_NAME;

async function queryFieldValue(repoOwner, repoName, issueNumber, fieldName) {
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
      }
    }
  }`;

  const parameters = {
    owner: repoOwner,
    repo: repoName,
    issueNumber: issueNumber,
    fieldName: fieldName,
    headers
  };

  const result = await octokit.graphql(query, parameters);
  
  return result.repository.issue.projectItems.edges;
}

function determineFieldValue(projectItems, projectId, fieldId) {
  for (const item of projectItems) {
    if (item.node.project.id == projectId && item.node.fieldValueByName && item.node.fieldValueByName.field.id == fieldId) {
      return { name: item.node.fieldValueByName.name, id: item.node.fieldValueByName.optionId };
    }
  }

  return {}
}

async function queryTrackedIssues(repoOwner, repoName, issueNumber) {
  const query = `query ($owner: String!, $repo: String!, $issueNumber: Int!) {
    repository(owner: $owner, name: $repo) {
      issue(number: $issueNumber) {
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
              url
            }
          }
        }
      }
    }
  }`;

  const parameters = {
    owner: repoOwner,
    repo: repoName,
    issueNumber: issueNumber,
    headers
  };

  const result = await octokit.graphql(query, parameters);

  return result.repository.issue.trackedIssues.edges;
}

(async function main() {
  // Get project items

  console.log(`Querying value for field ${FIELD_NAME} of #${ISSUE_NUMBER} in ${REPO_OWNER}/${REPO_NAME}`);
  const projectItems = await queryFieldValue(REPO_OWNER, REPO_NAME, ISSUE_NUMBER, FIELD_NAME);

  if (!projectItems) {
    console.log("Aborting because issue is not part of any projects");
    return;
  }

  // Determine field value

  fieldValue = determineFieldValue(projectItems, PROJECT_ID, FIELD_ID);

  if (!fieldValue.name || !fieldValue.id) {
    console.log("Aborting because issue is not part of the correct project");
    return;
  }
  
  console.log(`Determined field value "${fieldValue.name}" (${fieldValue.id})`);

  // Get tracked issues

  console.log(`Querying tracked issues of #${ISSUE_NUMBER} in ${REPO_OWNER}/${REPO_NAME}`);
  const trackedIssues = await queryTrackedIssues(REPO_OWNER, REPO_NAME, ISSUE_NUMBER);

  if (!trackedIssues) {
    console.log("Aborting because issue has no tracked issues");
    return;
  }
  
  // Set field values

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
          optionId: fieldValue.id,
          headers
        };

        const result = await octokit.graphql(mutation, parameters);
        console.log(`Set value "${fieldValue.name}" for field ${FIELD_NAME} on ${issue.node.url}`);

        break;
      }
    }
  }
})();
