import os


# 重命名指定路径的指定文件名
def file_rename(dir_path, old_filename, new_filename):
    old_file = os.path.join(dir_path, old_filename)
    new_file = os.path.join(dir_path, new_filename)
    return os.rename(old_file, new_file)

# 对一堆文件进行重命名
def file_list_rename(dir_path, new_filename_list):
    files = os.listdir(dir_path)
    for i in range(len(new_filename_list)):
        file_rename(dir_path, files[i], new_filename_list[i])
