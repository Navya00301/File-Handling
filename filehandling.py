# f=open("filehandling.txt",'x')

# with open('files.text','a')as f:
#     f.write("Farsad")
#     f.writelines(['Farsad\n','Neena'])

# with open("filehandling.txt") as f:
#     print(f.read(2))

# import csv
# with open('shop.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Serial no", "Name", "Item"])
#     writer.writerow([1, "Navya", "Book"])
#     writer.writerow([2, "Farsad", "Bag"])


# import csv

# with open('shop.csv', 'r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# import zipfile

# with zipfile.ZipFile('myfiles.zip', 'w') as zipf:
#     zipf.write('loop.py')
#     zipf.write('oops.py')

# with zipfile.ZipFile('myfiles.zip', 'r') as zipf:
#     print(zipf.namelist())



# with zipfile.ZipFile('myfiles.zip', 'r') as zipf:
#     zipf.extractall('extracted_files')


# with zipfile.ZipFile('new.zip', 'w') as zipf:
#     zipf.write('sets.py')
#     zipf.write('string.py')


# with zipfile.ZipFile('new.zip', 'r') as zipf:
#     print(zipf.namelist())


# with zipfile.ZipFile('new.zip', 'r') as zipf:
#     zipf.extractall('extracted_files')