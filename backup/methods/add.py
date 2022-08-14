import os
import filecmp
import pandas as pd
import shutil

# change color for consol output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Functions: WRITE >>>>>
def save_folder(folder_read_path, folder_target_path):
    global counter_new_files, counter_file_changes, counter_new_folders
    files_folders = os.listdir(folder_read_path)
    for file in files_folders:
        read_path_i = os.path.join(folder_read_path, file) #full path
        target_path_i = os.path.join(folder_target_path, file) #full path
        
        #file exist
        if os.path.isfile(read_path_i) and os.path.isfile(target_path_i) and filecmp.cmp(read_path_i, target_path_i):
            continue
        #file exist but changes
        elif os.path.isfile(read_path_i) and os.path.isfile(target_path_i) and not filecmp.cmp(read_path_i, target_path_i):
            print(bcolors.OKGREEN + 'Changes adjust: ' + bcolors.ENDC + read_path_i + ' --> ' + target_path_i)
            os.remove(target_path_i)
            shutil.copyfile(read_path_i, target_path_i)
            counter_file_changes += 1
        #file doesent exist
        elif os.path.isfile(read_path_i) and not os.path.isfile(target_path_i):
            print(bcolors.OKGREEN + 'Copy: ' + bcolors.ENDC + read_path_i + ' --> ' + target_path_i)
            shutil.copyfile(read_path_i, target_path_i)
            counter_new_files += 1
            
        #folder exist
        elif os.path.isdir(read_path_i) and os.path.isdir(target_path_i):
            save_folder(read_path_i, target_path_i)
        #folder doesnt exist
        elif os.path.isdir(read_path_i) and not os.path.isdir(target_path_i):
            print(bcolors.OKGREEN + 'Create new Folder:' + bcolors.ENDC + target_path_i)
            os.mkdir(target_path_i)
            counter_new_folders += 1
            save_folder(read_path_i, target_path_i)
        else:
            print(bcolors.FAIL + 'SHOULDNT HAPPENED!! ERROR!' + bcolors.ENDC)

# add backup
def write(filepath: str):
    global counter_new_files, counter_file_changes, counter_new_folders
    # get total path to this file

    # config
    index_save_location = 0

    # Read in paths
    # source
    df = pd.read_csv(f'{filepath}/path_source.csv', names=['Name', 'Path'], comment='#')
    print(bcolors.OKCYAN + 'Source Location:' + bcolors.ENDC)
    print(df, '\n')

    source_names = df['Name'].astype(str).values.tolist()
    abs_read_path_list = df['Path'].astype(str).values.tolist()

    # target
    df_target = pd.read_csv(f'{filepath}/path_target.csv', names=['Name', 'Path'], comment='#')
    target_names = df_target['Name'].astype(str).values.tolist()
    target_path = df_target['Path'].astype(str).values.tolist()
    print(bcolors.OKCYAN + 'Write Location: ' + bcolors.ENDC)
    print(target_path[index_save_location], '\n')


    if len(source_names) != len(abs_read_path_list):
        print(bcolors.FAIL + 'ERROR: Wrong len of name and path list.' + bcolors.ENDC)
        quit()

    # Variables
    end_folder_names = [os.path.basename(os.path.normpath(path)) for path in abs_read_path_list]
    abs_write_path = target_path[index_save_location]
    abs_write_path_list = [os.path.join(abs_write_path, name) for name in end_folder_names]

    counter_new_files = 0
    counter_file_changes = 0
    counter_new_folders = 0

        # Loop over absolute paths (read location)
    for read_path, write_path in zip(abs_read_path_list, abs_write_path_list):
        if not os.path.isdir(write_path):
            os.mkdir(write_path)

        save_folder(read_path, write_path)

    print(bcolors.OKCYAN + '\nActions:' + bcolors.ENDC)
    print('New files:', counter_new_files)
    print('File changes:', counter_file_changes)
    print('New folders:',counter_new_folders)
# <<<<< Functions: WRITE