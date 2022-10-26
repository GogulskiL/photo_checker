import os
import time


def get_folder_path():
    dir_path = str(input('Podaj ścieżkę do folderu:  '))
    return dir_path


def list_photo_in_folder(dir_path):
    return(os.listdir(dir_path))


def get_time_created(i):
    # loading the photo creation date
    c_time = os.path.getmtime(i)
    local_time = time.ctime(c_time)
    return local_time


def new_file_name(dir_path, i):
    # new photo name, change the colon to a hyphen
    new_name = str("_".join((get_time_created(dir_path+ "/" + i)).split(" ")).replace(":", "-"))
    return new_name


def result_new_photo(dir_path,i):
    # renaming and saving a new photo
    old_file = i
    new_photo = new_file_name(dir_path, i) + ".jpg"
    return os.rename(os.path.join(dir_path, old_file), os.path.join(dir_path, new_photo))


def main():
    path = get_folder_path()
    folder_cotent = list_photo_in_folder(path)
    for i in folder_cotent:
        return result_new_photo(path, i)


if __name__ == '__main__':
    main()
