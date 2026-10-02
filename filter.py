import os

files = os.listdir('.')
fileFormat = input("Give format you want to filter: ").replace('.', '')

for item in files:
    if item.endswith(f".{fileFormat}"):
        print(item)
