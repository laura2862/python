import os
import logging
from RetailProj.util import logging_util

'''
define a funtion to pass a path and return a file list under this path 
'''
def get_dir_files_list(path='/',recursion=False):
    logger=logging_util.init_logger()
    logger.info(f' reading all filenames under the {path}')
    # os.listdir is to get all the files' name under the given path
    dir_names=os.listdir(path)
    files=[]
    for dir_name in dir_names:
        absolute_path=f'{path}/{dir_name}'
        # files in this if///////// os.path.isdir: to judge is the file name is a directory
        if not os.path.isdir(absolute_path):
            files.append(absolute_path)
        else:
            if recursion:
                recursion_files_list=get_dir_files_list(absolute_path,recursion=recursion)
                # +: compond 2 lists
                # append: to add one obj to a list
                files+=recursion_files_list
    return files


# list a includes list b
def get_new_by_cmp_lists(list_a,list_b):
    new_list=[]
    for i in list_a:
        if i not in list_b:
            new_list.append(i)
    return new_list


