
def process_files(files):
    """
    Process a list of files to extract their extensions and create a message.
    
    Parameters:
    files (list): A list of File objects
    
    Returns:
    list: A list of strings containing messages about each file's extension
    """
    message = []

    for file in files:
        file_name = file.filename
        file_ext = file_name.split(".")[-1]
        data = f"The file extension for {file.filename} is {file_ext}"
        message.append(data)

    return message