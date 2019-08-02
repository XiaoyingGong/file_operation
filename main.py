import file_rename


path = r"C:\Users\95628\Desktop\1\1\6"
cate_num = 6
state = 'h'
# 创造重命名串
start_num = 0
new_names = []

for i in range(11):
    new_name = cate_num.__str__() + "_" + state + "_" + (i+1).__str__()+ ".bmp"
    new_names.append(new_name)

file_rename.file_list_rename(path, new_names)