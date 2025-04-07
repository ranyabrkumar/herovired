''' 
      Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
      
      The script should copy all files from the source directory to the destination directory.
      
      Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
      
      Handle errors gracefully, such as when the source directory or destination directory does not exist.
      
      Sample Command:
      
      python backup.py /path/to/source /path/to/destination
      
      By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
'''

import shutil
import os
from datetime import datetime
import argparse
import sys


'''function to check if the folder exists'''
def isfolderexit(folderpath):
    if os.path.exists(folderpath):
        return True
    else:
        return False
    
'''function to copy files from source to destination folder'''
def get_backup(source,destination):                         
      if not isfolderexit(source):                                        # Check if the source directory exists
            print(f"Source directory '{source}' does not exist.")
            return 
      else:
            print(f"Source directory '{source}' exists.")
    
      if not isfolderexit(destination):                                   # Check if the destination directory exists
            print(f"Destination directory '{destination}' does not exist.")
            return
      else:
            print(f"Destination directory '{destination}' exists.")
      try:
            for filename in os.listdir(source):                             # List all files in the source directory
                  source_file = os.path.join(source, filename)              # Create the full path for the source file
                  destination_file = os.path.join(destination, filename)        
                  
                  if os.path.exists(destination_file):                       # Check if the file already exists in the destination directory
                        base, ext = os.path.splitext(filename)                # Split the filename into base and extension
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Get the current timestamp
                        destination_file = os.path.join(destination, f"{base}_{timestamp}{ext}")
                  
                  shutil.copy2(source_file, destination_file)
                  print(f"Copied '{source_file}' to '{destination_file}'")
      except Exception as e:
            print(f"Error occurred while copying files: {e}")            

if __name__ == "__main__":
      try:
            if len(sys.argv) != 3:                          # Check if the number of arguments are provided is not 3 then throw error and exit program
                  print("Error: Incorrect number of arguments.")
                  print("Usage: python backup.py <source> <destination>")
                  sys.exit(1)
            else:
                  args = argparse.Namespace(source=sys.argv[1], destination=sys.argv[2]) # Parse command-line arguments
                  get_backup(args.source, args.destination)                            # Call the function to perform the backup
      except Exception as e:
            print(f"An error occurred: {e}")                                 # Handle any unexpected errors
            sys.exit(1)