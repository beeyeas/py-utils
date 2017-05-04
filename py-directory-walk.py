#Simple python program to recrursively browse directory for files and list all the files 

def print_directory_contents(ospath, count):
    import os
    for child in os.listdir(ospath):
        subchild = os.path.join(ospath, child)
        if os.path.isdir(subchild):
            print_directory_contents(subchild, count)
        else:
            #count = count + 1
            print(subchild)

directoryPath = input("Enter a valid directory path to list (example:/usr/bin): ")

print_directory_contents(directoryPath,0)