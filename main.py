import os
import time


def get_folder_path():
    dir_path = str(input('Podaj ścieżkę do folderu:  '))
    return dir_path


def list_photo_in_folder(dir_path):
    return(os.listdir(dir_path))


def get_time_created(path_single_photo):
    # loading the photo creation date
    c_time = os.path.getmtime(path_single_photo)
    local_time = time.ctime(c_time)
    return local_time


def new_file_name(dir_path, path_single_photo):
    # new photo name, change the colon to a hyphen
    new_name = str(
        "_".join((get_time_created(dir_path + "/" + path_single_photo)).split(" ")).replace(":", "-"))
    return new_name


def result_new_photo(dir_path, path_single_photo):
    # renaming and saving a new photo
    old_file = path_single_photo
    new_photo = new_file_name(dir_path, path_single_photo) + ".jpg"
    return os.rename(os.path.join(dir_path, old_file), os.path.join(dir_path, new_photo))


def check_rename_photo():
    dir_path = get_folder_path()
    folder_content = list_photo_in_folder(dir_path)
    for path_single_photo in folder_content:
        change_file = result_new_photo(dir_path, path_single_photo)
    return change_file


if __name__ == '__main__':
    
    check_rename_photo()
