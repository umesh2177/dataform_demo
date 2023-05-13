from google.cloud import dataform_v1beta1

import os
# credentials="C:\Task\Dataform\Scripts\key\dataform-382904-b4bcbf07fb5e.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

def sample_install_npm_packages(project,repo_id,workspace_id,region):
    # Create a client
    client = dataform_v1beta1.DataformClient()
    parent = f"projects/{project}/locations/{region}/repositories/{repo_id}"
    workspace = f"{parent}/workspaces/{workspace_id}"
    # Initialize request argument(s)
    request = dataform_v1beta1.InstallNpmPackagesRequest(
        workspace=workspace
    )

    # Make the request
    response = client.install_npm_packages(request=request)

    # Handle the response
    print(response)
    return response

# [END dataform_v1beta1_generated_Dataform_InstallNpmPackages_async]
# sample_install_npm_packages(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="us-central1")
# sample_install_npm_packages(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="europe-west4")