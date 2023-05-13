
# import sys
# import argparse
# import json
# from google.cloud import dataform_v1beta1
import openfolder as openf
import create_repository as create_repo
import create_workflow as run_pipeline
import create_workspace as create_workspace
import writefile as create_project
import npminstall as npm
import os 


def call_create_repo(project,repo_id,region):
    create_repo.sample_create_repository(project=project,repository=repo_id,region=region)

def call_create_workspace(project,repo_id,workspace_id,region):
    create_workspace.sample_create_workspace(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)

def call_create_project(project,repo_id,workspace_id,region):
    create_project.multifile(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)

def call_npm_install(project,repo_id,workspace_id,region):
    npm.sample_install_npm_packages(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)
    
def call_run_pipeline(project,repo_id,workspace_id,region):
    run_pipeline.sample_create_workflow_invocation(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)






if __name__ == '__main__':
    print("Please select path of service account key file.")
    credentials= openf.get_file_path()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    
    print("Select option as per your requirement.............\n \
            1. Create Repo \n \
            2. Create workspace \n \
            3. Create Project with write files. \n Hint :Select root folder of dataform project \n \
            4. Install npm modeule \n\
            5. Run Pipeline \n\
            6. Exit")
    choice=int(input("Enter your input : "))

    if choice == 1:
        print("Enter Project name: ")
        project=input()
        print("Enter Repo name: ")
        repo_id=input()
        print("Enter region or location name: \n \
            Hint: region will be as bigquery location")
        region=input()
        print(f"You have enter \n Project :{project} \n Repo name : {repo_id} \n region :{region} ")
        call_create_repo(project=project,repo_id=repo_id,region=region)


    if choice == 2:
        print("Enter Project name: ")
        project=input()
        print("Enter Repo name: ")
        repo=input()
        print("Enter region or location name: \n ")
        region=input()
        print("Enter workspace name: ")
        workspace=input()
        print(f"You have enter \n Project :{project} \n Repo name : {repo_id} \n region :{region} \n workspace :{workspace}")
        call_create_workspace(project=project,repo_id=repo,region=region,workspace_id=workspace)


    if choice == 3:
        print("Enter Dataform Project name: ")
        project=input()
        print("Enter Repo name: ")
        repo=input()
        print("Enter region or location name: ")
        region=input()
        print("Enter workspace name: ")
        workspace=input()
        print(f"You have enter \n Project :{project} \n Repo name : {repo_id} \n region :{region} \n workspace :{workspace}")
        call_create_project(project=project,repo_id=repo,region=region,workspace_id=workspace)

    if choice == 4:
        print("Enter Project name: ")
        project=input()
        print("Enter Repo name: ")
        repo=input()
        print("Enter region or location name: ")
        region=input()
        print("Enter workspace name: ")
        workspace=input()
        print(f"You have enter \n Project :{project} \n Repo name : {repo_id} \n region :{region} \n workspace :{workspace}")
        call_npm_install(project=project,repo_id=repo,region=region,workspace_id=workspace)

    if choice == 5:
        print("Enter Project name: ")
        project=input()
        print("Enter Repo name: ")
        repo=input()
        print("Enter region or location name: ")
        region=input()
        print("Enter workspace name: ")
        workspace=input()
        print(f"You have enter \n Project :{project} \n Repo name : {repo_id} \n region :{region} \n workspace :{workspace}")
        call_run_pipeline(project=project,repo_id=repo,region=region,workspace_id=workspace)

    if choice == 6:
        os._exit(0)










# ='dataform-382904'="py-test"="py-test-workspace"="us-central1"



    # parser = argparse.ArgumentParser(description='Run a Dataform workflow.')
    # parser.add_argument('--workspace', dest='workspace', required=True, help='Dataform workspace id.')
    # parser.add_argument('--project', dest='project', required=True, help='Google Cloud Project ID.')
    # parser.add_argument('--region', dest='region', required=True, help='Region as per Google Cloud bigquery dataset location.')
    # parser.add_argument('--repository', dest='repository', required=True, help='Dataform repository id.')
    # parser.add_argument('--config-vars', type=json.loads, dest='config_vars', help='Custom variables of config of Dataform workspace. type: MapField<String, String>')
    # args = parser.parse_args()

    # run_workflow(args.project, args.region, args.repository, args.workspace, args.config_vars)

