from google.cloud import dataform_v1beta1
# import os
# credentials="C:\Task\Dataform\Scripts\key\dataform-382904-b4bcbf07fb5e.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
def sample_create_workflow_invocation(project,repo_id,workspace_id,region):
    # print("workspace:{}".format(workspace_id))
    parent=f"projects/{project}/locations/{region}/repositories/{repo_id}"
    workspace = f"{parent}/workspaces/{workspace_id}"
    client = dataform_v1beta1.DataformClient()
    compilation_result_name  = compile(client=client,parent=parent,workspace=workspace)
    invoke_res=invoke(client, parent, compilation_result_name)
    res=sample_query_workflow_invocation_actions(invoke_res)
    return res 
    
def invoke(client, parent, compilation_result_name):
    workflow_invocation = dataform_v1beta1.WorkflowInvocation()
    workflow_invocation.compilation_result=compilation_result_name
    request = dataform_v1beta1.CreateWorkflowInvocationRequest(
        parent=parent,
        workflow_invocation=workflow_invocation)
    response = client.create_workflow_invocation(request=request)
    print(f"Final reponse: \n\t name: {response.name},\n\tstatus: {response.state.name}")
    # sample_query_workflow_invocation_actions(response.name)
    return response.name

def compile(client, parent, workspace):
    # print("workspace:{}".format(workspace))
    code_compilication_config =  dataform_v1beta1.CompilationResult.CodeCompilationConfig()
    compilation_result = dataform_v1beta1.CompilationResult()
    compilation_result.workspace = workspace
    compilation_result.code_compilation_config = code_compilication_config
    request = dataform_v1beta1.CreateCompilationResultRequest(
        parent=parent,
        compilation_result=compilation_result,)
    response = client.create_compilation_result(request=request)
    print("Compile reponse:\n {}".format(response))
    return response.name   



def sample_query_workflow_invocation_actions(name_value):
    client = dataform_v1beta1.DataformClient()
    request = dataform_v1beta1.QueryWorkflowInvocationActionsRequest(
        name=name_value,
    )
    page_result = client.query_workflow_invocation_actions(request=request).workflow_invocation_actions
    return str(page_result)
    # for response in page_result:
    #     try:    
    #         print(f"Status :{response.state.name} \n\nTarget : {response.target} \n\nBigquery Script: {response.bigquery_action}\n\nFailure Reason :{response.failure_reason}")
    #     except Exception as e:
    #         print(e)










# sample_create_workflow_invocation(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="europe-west4") 
# sample_create_workflow_invocation(project='dataform-382904',repo_id="py-test",workspace_id="py-test-workspace",region="us-central1") 

































# def run_workflow(project, region, repository, workspace, config_vars):
#     client = dataform_v1beta1.DataformClient()

#     parent = f"projects/{project}/locations/{region}/repositories/{repository}"
#     workspace = f"{parent}/workspaces/{workspace}"

#     compilation_result_name = compile(client, parent, workspace, config_vars)
#     invoke(client, parent, compilation_result_name)

# def compile(client, parent, workspace, config_vars):
#     code_compilication_config =  dataform_v1beta1.CompilationResult.CodeCompilationConfig()
#     code_compilication_config.vars = config_vars

#     compilation_result = dataform_v1beta1.CompilationResult()
#     # compilation_result.git_commitish = "main"
#     compilation_result.workspace = workspace
#     compilation_result.code_compilation_config = code_compilication_config

#     request = dataform_v1beta1.CreateCompilationResultRequest(
#         parent=parent,
#         compilation_result=compilation_result,
#     )
#     response = client.create_compilation_result(request=request)

#     print(response)
#     return response.name

# def invoke(client, parent, compilation_result_name):
#     workflow_invocation = dataform_v1beta1.WorkflowInvocation()
#     workflow_invocation.compilation_result=compilation_result_name

#     request = dataform_v1beta1.CreateWorkflowInvocationRequest(
#         parent=parent,
#         workflow_invocation=workflow_invocation
#     )

#     response = client.create_workflow_invocation(request=request)

#     print(response)
#     return response.name  

# run_workflow(project='dataform-382904',repository="py-test",workspace="py-test-workspace",region="europe-west4",
#              config_vars={
#                     'default_schema': 'dataform',
#                     'assertion_schema': 'dataform_assertions',
#                     'warehouse': 'bigquery',
#                     'default_database': 'dataform-382904',
#                     'default_location': 'us'
#   }
# )   