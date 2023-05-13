from google.cloud import dataform_v1beta1
import os
# credentials="C:\Task\Dataform\Scripts\key\dataform-382904-b4bcbf07fb5e.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

def sample_create_workspace(project,region,repo_id,workspace_id):
    # Create a client
    client = dataform_v1beta1.DataformClient()
    parent = f"projects/{project}/locations/{region}/repositories/{repo_id}"
    print(parent)
    workspace = workspace_id
    print(workspace)
    # Initialize request argument(s)
    request = dataform_v1beta1.CreateWorkspaceRequest(
        parent=parent,
        workspace_id=workspace,
    )

    # Make the request
    response = client.create_workspace(request=request)

    # Handle the response
    print(response)
    return response

# sample_create_workspace(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="europe-west4")
# sample_create_workspace(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="us-central1")