import csv
import pandas as pd

class path:
    def __init__(self):

        #path to csv files
        self.PATH_READ='paths/path_source.csv' 
        self.PATH_WRITE='paths/path_target.csv'

        #get current saved paths
        self.df_read = pd.read_csv(self.PATH_READ,)
        self.df_write = pd.read_csv(self.PATH_WRITE)

    # save df in csv >>>
    def __update_csv_write(self):
        self.df_write.to_csv(self.PATH_WRITE, index=False)
    def __update_csv_read(self):
        self.df_read.to_csv(self.PATH_READ, index=False)

    # delete all paths
    def reset(self):
        self.df_read = pd.DataFrame(columns=['name', 'path'])
        self.df_write = pd.DataFrame(columns=['name', 'path'])
        self.__update_csv_read()
        self.__update_csv_write()
        return

    # save path to df >>>
    def add_path_write(self, name, path_input):
        num_contains_str = self.df_write['path'].str.contains(path_input).sum()
        if num_contains_str > 0:
            name_exist = self.df_write['name'].iloc[num_contains_str-1]
            print(f'Path {path_input} already in Target: {name_exist}')
            return False
        else:
            self.df_write = self.df_write.append({'name': name, 'path': path_input}, ignore_index=True)
            self.__update_csv_write()
            print(f'Path {path_input} saved.')
            return True

    def add_path_read(self, name, path_input):
        num_contains_str = self.df_read['path'].str.contains(path_input).sum()
        if num_contains_str > 0:
            name_exist = self.df_read['name'].iloc[num_contains_str-1]
            print(f'Path {path_input} already in Source: {name_exist}')
            return False
        else:
            self.df_read = self.df_read.append({'name': name, 'path': path_input}, ignore_index=True)
            self.__update_csv_read()
            print(f'Path {path_input} saved.')
            return True

    # remove paths from df >>>
    def del_path_write(self, name):
        # check if name exist than drop row with name
        num_contains_str = self.df_write['name'].str.contains(name).sum()
        if num_contains_str > 0:
            _mask = self.df_write[self.df_write['name']==name].index

            self.df_write.drop(_mask, inplace=True)
            self.__update_csv_write()
            print(f'Source "{name}" deleted from destination directory.')
            return True
        else:
            print(f'"{name}" does not exit in destination directory.')
            return False
    
    def del_path_read(self, name):
        # check if name exist than drop row with name
        num_contains_str = self.df_read['name'].str.contains(name).sum()
        if num_contains_str > 0:
            _mask = self.df_read[self.df_read['name']==name].index

            self.df_read.drop(_mask, inplace=True)
            self.__update_csv_read()
            print(f'Source "{name}" deleted from source.')
            return True
        else:
            print(f'"{name}" does not exit in source.')
            return False

if __name__ =='__main__':
    obj = path()
    
    obj.add_path_read('QUELLE', 'test/nein')
    obj.add_path_write('TARGET', 'hier/nicht')
    obj.add_path_read('dfw', 'hier/wqdwqd/nicht')
    obj.add_path_write('wqdwqd', 'qwdwq/nicht')

    obj.del_path_write('TARGET')

    obj.reset()