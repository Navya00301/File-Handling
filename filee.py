# f=open("tes.txt",'x')

# f.close()



# with open('demo.txt','a')as f:
#     # f.write("Navya")
#     f.writelines(['navya\n',"annnuuuuu"])




# with open("demo.txt") as f:
#   print(f.read(3))


# import os
# os.remove("test.txt")



# import csv
# with open('college.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Roll No", "Name", "course"])
#     writer.writerow([1, "Navya", "BCA"])
#     writer.writerow([2, "Harry Potter", "BSc"])



import csv

with open('college.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)