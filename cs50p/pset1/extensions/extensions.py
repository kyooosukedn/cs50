import os

def convert(file_name):

    # Dictionary to map file extensions
    file_types = {
        ".gif"  : "image/gif",
        ".jpg"  : "image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png"  : "image/png",
        ".pdf"  : "image/pdf",
        ".txt"  : "image/txt",
        ".zip"  : "image/zip",
    }

    # Split the base name and file extension separately

    base_name, extension = os.path.splitext(file_name)

    file_type = file_types.get(extension.lower(), "application/octet-stream") # default choice

    return file_type

def main():
    file_name = input("File name: ")
    print(convert(file_name))

main()