import os
import time

def get_folder_path():
    folder_path = input("Podaj ścieżkę do folderu:  ")
    return folder_path


def get_time_created(path):
    # loading the photo creation date
    c_time = os.path.getmtime(path)
    local_time = time.ctime(c_time)
    return local_time


def new_file_name(path):
    # new photo name, change the colon to a hyphen
    get_new_name = str(get_time_created(path)).split(" ")
    new_name = "_".join(get_new_name).replace(":", "-")
    return new_name


def result_new_photo(path):
    # renaming and saving a new photo
    old_file = path
    new_photo = new_file_name(old_file) + ".jpg"
    return os.rename(old_file, new_photo)
