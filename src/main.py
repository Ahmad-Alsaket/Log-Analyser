import pathlib

# "C:\Users\USER\Desktop\filexyz.txt"

counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
}


def read_file(path):
    content = path.read_text()
    return content
    
    
def count(content):
    INFO = content.count("INFO")
    WARNING = content.count("WARNING")
    ERROR = content.count("ERROR")
    
    counts["INFO"] += INFO
    counts["WARNING"] += WARNING
    counts["ERROR"] += ERROR

    return counts
    
    
    
    
def main():
    user_path = input("add file path: ")
    path = pathlib.Path(user_path)
    content = read_file(path)
    count(content)
    
    for key,item in counts.items():
        print(key,item)
        
        
if __name__ == "__main__":
    main()