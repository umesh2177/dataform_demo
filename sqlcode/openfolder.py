import tkinter
from tkinter import filedialog
import glob
import os 
tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

def get_file_path(title):
    file_path=filedialog.askopenfile(title=title)
    print("You have selected path: {}".format(file_path.name))
    return file_path.name

def get_file_blob():
    path=get_file_path()
    with open(path, mode='rb') as file: # b is  -> binary
        fileContent = file.read()
    return fileContent  

def get_dir(title):
    dir_path=filedialog.askdirectory(title=title)
    return dir_path


def get_dir_list():
    l=glob.glob(get_dir()+"/**/*",recursive=True)
    dir_l=[dl.replace("C:/Task/Dataform/dataform-example-project-bigquery\\","") for dl in l if os.path.isdir(dl) ]
    
    # print(dir_l)
    # print("Files: {}".format(file_l))
    return dir_l

def get_file_list(title):
    l=glob.glob(get_dir(title=title)+"/**/*",recursive=True)
    # print(l)
    file_l=[dl for dl in l if os.path.isfile(dl)]
    # file_l=[dl.replace("C:/Task/Dataform/dataform-example-project-bigquery\\","") for dl in l if os.path.isfile(dl) ]
    # print(file_l)
    return file_l

# get_file_list()
# {
#     [' C:/Task/Dataform/dataform-example-project-bigquery\\dataform.json',
#       'C:/Task/Dataform/dataform-example-project-bigquery\\environments.json', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\package-lock.json', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\package.json',
#       'C:/Task/Dataform/dataform-example-project-bigquery\\schedules.json', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\reporting\\posts_combined.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\reporting\\user_stats.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\sources\\badges.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\sources\\posts_answers.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\sources\\posts_questions.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\sources\\users.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\staging\\stg_badges.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\staging\\stg_posts_answers.sqlx', 
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\staging\\stg_posts_questions.sqlx',
#       'C:/Task/Dataform/dataform-example-project-bigquery\\definitions\\staging\\stg_users.sqlx']
# }