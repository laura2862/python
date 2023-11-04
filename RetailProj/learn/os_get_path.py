import os
path=current_file_path = os.path.abspath(__file__)
print(path)

root_path= os.path.dirname(current_file_path)
print(root_path)

print(os.getcwd())
print(os.path.dirname(os.getcwd()))

name=os.path.basename(os.getcwd())
print(name)
