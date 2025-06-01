import os

folders = input("Please provide a list of folder names: ").split()

for folder in folders:
    files = os.listdir(folder)
    print("files in folder: "+ folder)
    for file in files:
      print(file)
