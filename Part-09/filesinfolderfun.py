import os

def list_files_in_folder(folder_path):
  try:
    files = os.listdir(folder_path)
    return files, None
  except FileNotFoundError:
    return None, "Folder not found"
  except PermissionError:
    return None, "Permission Denied"

def main():
    folder_paths = input("Please provide a list of folder paths with spaces in between: ").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
          print(f"List of Files: {folder_path}")
          for file in files:
            print(file)
        else:
            print(f"{error_message}: {folder_path}")

if __name__ == "__main__":
    main()
