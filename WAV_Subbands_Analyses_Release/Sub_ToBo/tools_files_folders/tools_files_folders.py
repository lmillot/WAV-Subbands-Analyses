# -*- coding: utf-8 -*-
"""
script name :       tools_files_folders.py

creation date:      05/05/2024, 12h14
modification date:  04/10/2024, 11h59

@author: Millot
"""


import os
import pathlib as pl
import shutil



# ----------
def is_file_existing(file_path):
    """
    is_file_existing(file_path)

    Parameters :
    -----------
    file_path : pathlib Path
        pathlib Path of the form the_path / filename.ext.

    Returns :
    --------
    True is the file exists, False else
    

    """
    # Check if the file exists
    if os.path.exists(file_path):
        return True

    else:
        return False 
   

    
# ----------
def is_folder_existing(studied_path):
    """
    the_path = pl.Path(studied_path)

    Parameters :
    -----------
    file_path : pathlib Path
        pathlib Path for the tested folder
        
    Returns :
    --------
    bool: boolean
        True if folder exists

    """
    
    return studied_path.is_dir()
      
  
# ----------
def create_new_subfolder(studied_path, I_give_info=False):
    """
    create_new_subfolder(studied_path, I_give_info)

    Parameters : 
    -----------
    studied_path : pathlib Path
        pathlib Path for the new folder to be created

    I_give_info : boolean
        if True print some information if the folder does not exist

    Returns :
    --------
    None

    """ 
    the_path = pl.Path(studied_path)
    
    if the_path.is_dir() == False:
        the_path.mkdir()
        
        if I_give_info is True:
            print("creating subfolder:")
            print(studied_path)	

            

# ----------
def is_folder_empty(studied_path):
    """
    folder_empty = is_folder_empty(studied_path)

    Parameters :
    -----------
    studied_path : pathlib Path
        pathlib Path for the new folder to be created

    Returns :
    --------
    folder_empty : boolean
        True if the folder is empty, False otherwise

    """
    if os.path.isdir(studied_path):
        if not os.listdir(studied_path):
            return True
        else:
            return False
    else:
        print("Given directory does not exist...")
        
        
# ----------
def list_subfolders(studied_path):
    """
    sub_folders_names_list, sub_folders_paths_list = \
        list_subfolders(studied_path)
    
    Parameters :
    -----------
    studied_path : pathlib Path
        pathlib Path for the folder under study

    Returns :
    ---------
    sub_folders_names_list : list
        list of the names of the subfolders existing within the studied folder
        
    sub_folders_paths_list : list
        list of the paths of the subfolders existing within the studied folder
    """
    the_path = pl.Path(studied_path)
    
	# list the subfolder paths
    sub_folders_paths_list = [x for x in the_path.iterdir() if x.is_dir()]

	# list subdirectories within studied_path
    sub_folders_names_list = [x.name for x in sub_folders_paths_list]
    
    return sub_folders_names_list, sub_folders_paths_list	


# ----------
def get_possible_filters_sets(global_subfolder_list, analysis_name, 
                              sampling_rate):
    """
    ir_length_array, subfolders_list = \
        get_possible_filters_sets(global_subfolder_list, analysis_name,
                                  sampling_rate)
        
    Parameters :
    ------------
    global_subfolder_list :  list
        list of subfolders to test to find the possibles filters sets
    
    analysis_name : string
        name of the frequency mappinf to be used for the analyses
    
    sampling_rate : int
        sample rate of the WAV to be studied and of the subbands filters to use

    Returns :
    ---------
    ir_length_array : list of integers
        list of the filters' length for the filters sets corresponding to 
        the chosen frequency mapping

    subfolders_list ; list of strings
        list of filters sets' folder corresponding to the chosen frequency 
        mapping

    """
    analysis_subfolders_list = []
    subfolders_list = []
    ir_length_array = []
    
    for x in global_subfolder_list:
        if x.find(analysis_name) > 0:
            analysis_subfolders_list.append(x)
            test_list = x.split('_')
            
            if test_list[2] == str(int(sampling_rate/100)):
                subfolders_list.append(x)
                new_ir_length = int(test_list[3])
                ir_length_array.append(new_ir_length)
                
    return ir_length_array, subfolders_list


# ----------
def list_given_extension_files(the_path, the_extension):
    """
    final_list = list_given_extension_files(the_path, the_extension)

    Parameters :
    ------------
    the_path : pathlib Path
        pathlib Path for the folder under study
    
    the_extension : string
        string corresponding to the extension of the type of searched files 

    Returns :
    --------
    final_list : list of strings
        list of the names of the files existing within the folder under study
        which have the wanted extension

    """
    first_list = list(p for p in pl.Path(the_path).iterdir() if p.is_file())

    list_length = len(first_list)

    final_list = []

    for i in range(list_length):
        the_file =  str(first_list[i])
        the_file = the_file.split('/')[-1]
        
        if the_file != ".DS_Store" and the_file[0] != ".":
            if the_extension in the_file:
                final_list.append(the_file)
                
    return final_list 


# ----------
def copy_file(original_path, filename, copy_path):
    """
    copy_file(original_path, filename, copy_path)

    Parameters :
    ------------
    original_path : pathlib Path
        pathlib Path for the folder where the file to copy exists
    
    filename : string
        filename of the orginal and of the copy
    
    copy_path : pathlib Path
        pathlib Path for the folder where the copied file will be created

    Returns :
    ---------
    None.
    """
    shutil.copyfile(original_path / filename, copy_path / filename)


# ----------
def duplicate_file(beg_path, beg_filename, end_path, end_filename):
    """
    duplicate_file(beg_path, beg_filename, end_path, end_filename)

    Parameters:
    -----------
    beg_path : pathlib Path
        pathlib Path where the file to duplicate exists
    
    beg_filename : string
        filename of the file to duplicate
    
    end_path : pathlib Path
        pathlib Path where the duplicated file will be created
    
    end_filename : string
        filename of the copy
    
    Returns :
    ---------
    None.
    """
    shutil.copyfile(beg_path / beg_filename, end_path / end_filename)


# ----------
def delete_a_file(the_file_path):
    """
    delete_a_file(the_file_path)

    Parameters :
    -----------
    the_file_path: pathlib Path
    pathlib Path of the file to delete

    Returns :
    ---------
    None. 
    
    """
    if os.path.isfile(the_file_path):
        os.remove(the_file_path)
        
        
# ----------
def copy_folder(original_path, copy_path):
    """
    copy_folder(original_path, copy_path)

    Parameters :
    -----------
    original_path : pathlib Path
        pathlib Path of the folder to duplicate

    copy_path : pathlib Path
        pathlib Path where the folder will be duplicated

    Returns :
    ---------
    None. 
    """
    shutil.copytree(original_path, copy_path)


# ----------
def delete_folder(the_folder_path):
    """
    delete_folder(the_folder_path)

    Parameters :
    -----------
    the_folder_path : pathlib Path
        pathlib Path of the folder to delete

    Returns :
    ---------
    None. 
    """
    if os.path.isdir(the_folder_path):
        is_empty = is_folder_empty(the_folder_path)
        
        if is_empty is True:
            os.rmdir(the_folder_path)
            
        elif is_empty is False:
            shutil.rmtree(the_folder_path)
            
        else:
            pass
 