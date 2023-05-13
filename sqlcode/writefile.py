from google.cloud import dataform_v1beta1
import os
import openfolder
# credentials="C:\Task\Dataform\Scripts\key\dataform-382904-b4bcbf07fb5e.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
def sample_write_file(project,region,repo_id,workspace_id,path_value,fileContent):
    # Create a client
    client = dataform_v1beta1.DataformClient()
    workspace_value=f"projects/{project}/locations/{region}/repositories/{repo_id}/workspaces/{workspace_id}"
    # Initialize request argument(s)
    request = dataform_v1beta1.WriteFileRequest(
        workspace=workspace_value,
        path=path_value,
        contents=fileContent,)
    response = client.write_file(request=request)
    print(response)
    return response

def getfileblob(path):
    #   fileContent=""
    # path=openfolder.get_file_path()
    with open(path, mode='rb') as file: # b is  -> binary
        fileContent = file.read()
# print(fileContent)
    return fileContent    

def multifile(project,repo_id,workspace_id,region):
    paths =openfolder.get_file_list(title="select dataform project folder")
    # print(paths)
    res=[]
    for p in paths:
        f_blob=getfileblob(p)
        path="/".join(p.replace("C:/Task/Dataform/dataform-example-project-bigquery\\","").split("\\"))
        # path="/".join(p.split("\\")[-2:])
        print(f'files :{path}',end="\n")
        res.append(sample_write_file(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region,path_value=path,fileContent=f_blob) )   
    return res
# multifile(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="us-central1")









# #single file 

# def getfile():
#     #   fileContent=""
#     path=openfolder.get_file_path()
#     with open(path, mode='rb') as file: # b is  -> binary
#         fileContent = file.read()
# # print(fileContent)
#     return fileContent    

