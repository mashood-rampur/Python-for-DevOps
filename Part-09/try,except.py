import os

folders = input("Please provide a list of folder names: ").split()

for folder in folders:
  try:
    files = os.listdir(folder)
  except FileNotFoundError:
     print("Please provide a valid folder name, looks like the folder doesn't exist: " + folder)
     continue
  print("files in folder: "+ folder)
  for file in files:
   print(file)
