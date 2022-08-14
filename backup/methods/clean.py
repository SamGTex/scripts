import pandas as pd
import os
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

# Functions: DELETE >>>>

# check target_path for additional files/folder delete them
def delete_folder(folder_read_path, folder_target_path):
    read_items = os.listdir(folder_read_path)
    write_items = os.listdir(folder_target_path)
    print(bcolors.OKGREEN + 'Check: ' + bcolors.ENDC + folder_read_path + bcolors.OKGREEN + ' <==> ' + bcolors.ENDC + folder_target_path)
   
    for i,write in enumerate(write_items):
        write_path = os.path.join(folder_target_path,write)
        if write not in read_items:
            if os.path.isdir(write_path):
                shutil.rmtree(write_path)
            else:
                os.remove(write_path)
            #print(f'{write} deletet. ({folder_target_path})')
            
            print(bcolors.WARNING + f'Old File/Folder deleteted: {write} ({folder_target_path})' + bcolors.ENDC)

    write_items = os.listdir(folder_target_path)
    for write_item in write_items:
        if os.path.isdir(os.path.join(folder_target_path, write_item)):
            delete_folder(os.path.join(folder_read_path, write_item), os.path.join(folder_target_path, write_item))

def remove_duplicate(filepath):
    #config
    index_save_location = 0

    # read in / preprocessing
    # source
    df = pd.read_csv(f'{filepath}/path_source.csv', names=['Name', 'Path'], comment='#')
    print(bcolors.OKCYAN + 'Source Location:' + bcolors.ENDC)
    print(df, '\n')

    name_list = df['Name'].astype(str).values.tolist()
    abs_read_path_list = df['Path'].astype(str).values.tolist()

    if len(name_list) != len(abs_read_path_list):
        print(bcolors.FAIL + 'ERROR: Wrong len of name and path list.' + bcolors.ENDC)
        quit()

    # target
    df_target = pd.read_csv(f'{filepath}/path_target.csv', names=['Name', 'Path'], comment='#')
    target_names = df_target['Name'].astype(str).values.tolist()
    target_path = df_target['Path'].astype(str).values.tolist()
    print(bcolors.OKCYAN + 'Write Location: ' + bcolors.ENDC + target_path[index_save_location] + '\n')

    end_folder_names = [os.path.basename(os.path.normpath(path)) for path in abs_read_path_list]
    abs_write_path = target_path[index_save_location]
    abs_write_path_list = [os.path.join(abs_write_path, name) for name in end_folder_names]

    # loop over all read directories
    for read_path, write_path in zip(abs_read_path_list, abs_write_path_list):
        delete_folder(read_path, write_path)

# <<<<< Functions: DELETE