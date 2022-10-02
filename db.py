import pathlib
import os

DB_DIR = pathlib.Path(__file__).resolve().parent

def read(filename):
    fullpath = os.path.join(DB_DIR, filename)

    with open(fullpath, 'r', encoding='utf-8') as f:
        return [line.strip().split(";") for line in f.readlines() if len(line) > 0]

def append(filename, data):
    fullpath = os.path.join(DB_DIR, filename)

    new_id = next_id(filename)
    data.insert(0, new_id)

    data = ";".join(data) # Convert to ; separated

    with open(fullpath, "a", encoding="utf-8") as f:
        f.write(data + "\n")

    return new_id

def remove(filename, value):
    fullpath = os.path.join(DB_DIR, filename)
    
    data = read(filename)
    new_data = [";".join(record) for record in data if record[0] != value]
    new_data = "\n".join(new_data)

    with open(fullpath, "w", encoding="utf-8") as f:
        f.write(new_data + "\n")
    
    return value

def next_id(filename):
    return str(len(read(filename)) + 1)
    