# WAP create a folder name  "report" if it is not exist



import os

pwd = os.getcwd()


"""
get_files = os.listdir(pwd)
print(get_files)
path = "C:\\Users\\user\\Desktop\\WK4\\report"
if path not in get_files:
     os.makedirs("report")
else:
     print("Folder exsit")
"""


if not os.path.exists("report"):
     os.makedirs("report")
else:
     print("Path alredy exist")
