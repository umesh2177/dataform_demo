from google.cloud import dataform_v1beta1
import os
# Create an service account and give permission Dataform admin or create /delete
# credentials="C:\Task\Dataform\Scripts\key\dataform-382904-b4bcbf07fb5e.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

def sample_create_repository(project,repository,region):
    # Create a client
    client = dataform_v1beta1.DataformClient()
    # print(client.DEFAULT_ENDPOINT)
    parent = f"projects/{project}/locations/{region}"
    # workspace = f"{parent}/workspaces/{workspace}"
    # Initialize request argument(s)
    request = dataform_v1beta1.CreateRepositoryRequest(
        parent=parent,
        repository_id=repository,
    )

    # Make the request
    response = client.create_repository(request=request)

    # Handle the response
    print(response)
    return response


# sample_create_repository('dataform-382904',"py-test","europe-west4") 
# sample_create_repository('dataform-382904',"py-test","us-central1") 