from shutil import copy2, move

file_1 = "experimental/data/foldar_last/sample_1.txt"
file_2 = "experimental/sample_2.txt"
directory_1 = "copired_directory"
directory_2 = "experimental/data"

copy2(file_1, directory_1)
move(file_2, directory_2)
