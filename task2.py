import hashlib
import os
import sys 

def md5_hash(file):
    _hash = hashlib.md5()
    with open(file, "rb") as f:
        for ch in iter(lambda: f.read(1024), b""):
            _hash.update(ch)
    
    return _hash.hexdigest()

hash_map = {}
def watch_dir(dirpath):
    for r, dirs, files in os.walk(dirpath):
        for f in files:
            file_path = f'{r}/{f}';
            h = md5_hash(file_path)

            if h in hash_map:
                print(f'"{file_path}" дубликат из "{hash_map[h]}"')
            else:
                hash_map[h] = file_path



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("task2.py ./dir")
    else:
        for dir in sys.argv[1:]:
            watch_dir(dir)
else:
    print("Не делай так.")