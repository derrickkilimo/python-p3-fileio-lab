def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    try:
        with open(f"{file_name}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return None