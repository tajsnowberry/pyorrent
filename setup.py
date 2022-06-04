import os
import configparser
config = configparser.ConfigParser()
dir_repository = "repository"
parent_directory = os.getcwd() # Get Current Directory
if os.path.exists(dir_repository) == False:
      print("Repository doesn't exist, creating directory...")
      make_repo_path = os.path.join(parent_directory, dir_repository) # Make Repo
      mode = 0o666 # Set to RW
      os.mkdir(make_repo_path, mode) # Set to pyorrent/repository
      if os.path.exists(dir_repository) == True:
            print("Repository is setup successfully!")
            pass
      else:
            print("ABORTED!, unable to create directory.")
else:
      print("You already have the repository, passing...")
      pass


    

