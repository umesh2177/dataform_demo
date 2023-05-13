from google.cloud import dataform_v1beta1
def sample_query_workflow_invocation_actions(name_value):
    client = dataform_v1beta1.DataformClient()
    request = dataform_v1beta1.QueryWorkflowInvocationActionsRequest(
        name=name_value,
    )
    page_result = client.query_workflow_invocation_actions(request=request).workflow_invocation_actions

    for response in page_result:
        try:    
            res=f"Status :{response.state.name} \n\nTarget : {response.target} \n\nBigquery Script: {response.bigquery_action}\n\nFailure Reason :{response.failure_reason}"
        except Exception as e:
            print(e)
            res=e.args    
