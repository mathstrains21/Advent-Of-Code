from typing import IO, Self

class File:
    def __init__(self, file_name: str, size: int):
        self.file_name = file_name
        self.size = size
    
    def __repr__(self):
        return f"{self.file_name} (file, size={self.size})"

class Folder:
    def __init__(self, folder_name: str, parent: Self = None):
        self.folder_name = folder_name
        self.files: list[File] = []
        self.folders: list[Folder] = []
        self.parent = parent
    
    def add_file(self, file: File):
        self.files.append(file)
    
    def add_folder(self, folder: Self):
        self.folders.append(folder)

    def get_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size
        for folder in self.folders:
            size += folder.get_size()
        return size
    
    def __repr__(self, indent=0):
        string = f"{self.folder_name} (dir, size={self.get_size()})\n"
        indentString = "  " * indent
        for folder in self.folders:
            string += f"{indentString} - {folder.__repr__(indent + 1)}"
        for file in self.files:
            string += f"{indentString} - {file.__repr__()}\n"
        return string
    
    def get_folders(self):
        folders = []
        for folder in self.folders:
            folders.append(folder)
            folders += folder.get_folders()
        return folders

def get_tree(input_file: IO):
    root = Folder("/")
    current_folder = root
    for line in input_file.read().splitlines():
        if line.startswith("$ cd"):
            folder_name = line.split(" ")[2].strip()
            if folder_name == "/":
                current_folder = root
            elif folder_name == "..":
                current_folder = current_folder.parent
            else:
                for folder in current_folder.folders:
                    if folder.folder_name == folder_name:
                        current_folder = folder
                        break
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):            
            folder_name = line.split(" ")[1].strip()
            folder = Folder(folder_name, current_folder)
            current_folder.add_folder(folder)
        else:
            size, file_name = line.split(" ")
            file = File(file_name, int(size))
            current_folder.add_file(file)
    return root

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    root = get_tree(input_file)
    folders = root.get_folders()

    size = 0
    for folder in folders:
        if folder.get_size() <= 100000:
            size += folder.get_size()
    return size

def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    root = get_tree(input_file)
    folders = root.get_folders()

    max_space = 70000000
    free_space_needed = 30000000
    current_free_space = max_space - root.get_size()
    space_needed = free_space_needed - current_free_space

    minimum_delete = root.get_size()
    for folder in folders:
        if folder.get_size() >= space_needed:
            minimum_delete = min(minimum_delete, folder.get_size())
    return minimum_delete

