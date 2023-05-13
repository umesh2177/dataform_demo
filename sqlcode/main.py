import argparse
import openfolder as openf
import create_repository as create_repo
import create_workflow as run_pipeline
import create_workspace as create_workspace
import writefile as create_project
import npminstall as npm
import os 

def store_log(logs,filename):
    
    try:
        with open(f"log_{filename}.text","w+") as f:
            print(f"{filename}::{logs}")
            f.writelines(str(logs))
            f.close()
    except Exception as e:
        print(e)        
def call_create_repo(project,repo_id,region):
    try:
        response=create_repo.sample_create_repository(project=project,repository=repo_id,region=region)
    except Exception as e :
        print(f"Exception : {e.args}")
        response=e.args
    finally:
         store_log(response,"create_repo")
def call_create_workspace(project,repo_id,workspace_id,region):
    try:
        response=create_workspace.sample_create_workspace(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)
    except Exception as e :
        print(f"Exception : {e.args}")
        response=e.args
    finally:
         store_log(response,"create_workspace")    
def call_create_project(project,repo_id,workspace_id,region):
    try:
        response=create_project.multifile(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)
    except Exception as e :
        response=e.args
        print(f"Exception : {e.args}")
    finally:
         store_log(response,"create_project")    
def call_npm_install(project,repo_id,workspace_id,region):
    try:
        response=npm.sample_install_npm_packages(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)
    except Exception as e :
        response=e.args
        print(f"Exception : {e.args}")
    finally:
         store_log(response,"install_npm_packages")    
def call_run_pipeline(project,repo_id,workspace_id,region):
    try:
        response=run_pipeline.sample_create_workflow_invocation(project=project,repo_id=repo_id,workspace_id=workspace_id,region=region)
    except Exception as e :
        response=e.args
        print(f"Exception : {e.args}")
    finally:
         store_log(response,"run_pipeline")    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Dataform service. \n Sample cmd: \n \
                                        main.py --project projectname_value --workspace my-workspace  --region us-central1 --repository py-cmd --choice create_repo \n \
                                     ')
    parser.add_argument('--project', dest='project', required=True, help='Google Cloud Project ID.')
    parser.add_argument('--workspace', dest='workspace', required=False, help='Dataform workspace id.')
    parser.add_argument('--region', dest='region', required=True, help='Region as per Google Cloud bigquery dataset location.')
    parser.add_argument('--repository', dest='repository', required=True, help='Dataform repository id.')
    parser.add_argument('--choice', dest='choice', required=True, help='Type of work. Input: create_repo,create_workspace,write_project,install_npm,run_pipeline')
    args = parser.parse_args()
    print("Please select path of service account key file.")
    credentials= openf.get_file_path("Select path of service account keyfile")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

    if args.choice == "create_repo":
        call_create_repo(project=args.project,repo_id=args.repository,region=args.region)
    elif args.choice == "create_workspace":
        call_create_workspace(project=args.project,repo_id=args.repository,region=args.region,workspace_id=args.workspace)
    elif args.choice == "write_project":
        call_create_project(project=args.project,repo_id=args.repository,region=args.region,workspace_id=args.workspace)
    elif args.choice == "install_npm":
        call_npm_install(project=args.project,repo_id=args.repository,region=args.region,workspace_id=args.workspace)
    elif args.choice == "run_pipeline":
        call_run_pipeline(project=args.project,repo_id=args.repository,region=args.region,workspace_id=args.workspace)
    else:
        print("Please check command ")
    
















#--project dataform-382904 --workspace py-workspace --region us-central1 --repository py-cmd --choice create_repo


# ='dataform-382904'="py-test"="py-test-workspace"="us-central1"


'''
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







'''