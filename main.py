import os
import time

path_test = "testy_photo_checker\FB_IMG_1652721744105.jpg"

# loading the file creation date
def get_time_created(path):
    c_time = os.path.getctime(path)
    local_time = time.ctime(c_time)
    return local_time

# new photo name, change the colon to a hyphen
def new_file_name(path):
    get_new_name = str(get_time_created(path)).split(" ")
    new_name = "_".join(get_new_name).replace(":", "-")
    return new_name




def resault(path):
    old_file = path
    new_photo = new_file_name(old_file) + ".jpg"
    return os.rename(old_file, new_photo)

print(resault(path_test))