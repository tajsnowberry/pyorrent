import os
dir_repository = "repository"
repo_exists = os.path.exists(dir_repository) # Does Repo Exist
parent_directory = os.getcwd() # Get Current Directory
if repo_exists == False:
      print("Repo Doesn't Exist")
      print(parent_directory)
      make_repo_path = os.path.join(parent_directory, dir_repository) # Make Repo
      print(make_repo_path)
    

