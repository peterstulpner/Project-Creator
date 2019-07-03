
import os, sys, subprocess, shutil
from distutils.dir_util import copy_tree

# Paths
p5_libs = r'C:\\Users\\peter\\Desktop\\Python Projects\\P5 Libraries'
atom_path = r'C:\Users\peter\AppData\Local\atom\atom.exe'

def createDirectory(filename, language_to_be_used, application_name="sketch"):
    '''Function creates the directory in which the projects files will be stores'''
    print(application_name)
    # Navigate to main project directory:
    os.chdir(r'C:\\Users\\peter\\Desktop\\Python Projects')
    try:
        os.mkdir(filename)
        os.chdir(r'C:\\Users\\peter\\Desktop\\Python Projects' + f'\\{filename}')
        curr_dir = os.getcwd()

        if language == 'p5':
            copy_tree(p5_libs, curr_dir)
            html_path = f'{curr_dir}\index.html'
            subprocess.Popen([atom_path, html_path])

        project_name = f'{application_name}{POSSIBLE_LANGAUGES[language_to_be_used]}'
        open(project_name, 'x')
        app_path = f'{curr_dir}\{project_name}'
        subprocess.Popen([atom_path, app_path])

        if include_html:
            open('index.html', 'x')
            html_path = f'{curr_dir}\index.html'
            subprocess.Popen([atom_path, html_path])


    except OSError:
        print('error file already exists')
        sys.exit()

    return f'Project Created'

# User input
new_project_name = input('Enter the new project name: ')
language_used = int(input('What language is primarily going to be used? \
                            \n 1) Python                                \
                            \n 2) Javascript                            \
                            \n 3) Javascript with P5.js \n'))
app_name = input('Name of the porjects type e.g sketch etc.: ')

# Defaults
include_html = True
POSSIBLE_LANGAUGES = {'python':'.py',
                      'js':'.js',
                      'p5':'.js',
                      'html':'.html'}

# Here we create the new direcotry and the porject files we need to get started
if language_used == 1:
    include_html = False
    language = 'python'
    print(createDirectory(new_project_name, language, app_name) \
                if app_name else createDirectory(new_project_name, language))

elif language_used == 2:
    language = 'js'
    print(createDirectory(new_project_name, language, app_name) \
                if app_name else createDirectory(new_project_name, language))

else:
    language = 'p5'
    print(createDirectory(new_project_name, language, app_name) \
                if app_name else createDirectory(new_project_name, language))
