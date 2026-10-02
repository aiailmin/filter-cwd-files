import os

files = os.listdir('.')
fileFormat =input("Give format you want filter it: ")
for item in files:
    # شرط: اگر اسم فایل با .py تمام می‌شود
    if item.endswith(f".{fileFormat}"):
        print(item)
        # مأموریت: دستور print را دقیقاً اینجا بنویسید. 
        # (یادتان باشد که باید هم‌تراز با همین خطِ کامنت باشد، یعنی جلوتر از if)
