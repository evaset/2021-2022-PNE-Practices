from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"
FILENAME2= "../Hello/hello2.py"

# -- Open and read the file
file_contents = Path(FILENAME2).read_text()

# -- Print the contents on the console
print(file_contents)