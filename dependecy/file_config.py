import os

def create_file():
    file_directory = "data-log"
    new_file = "log.txt"
    file_path = os.path.join(file_directory, new_file)
    
    if not os.path.exists(file_directory):
        os.mkdir(file_directory)
    
    if not os.path.exists(file_path):
        open(file_path, "x")
    
    print("sucessfully created")
    

