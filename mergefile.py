with open("file1.txt", "r")as f1, open("file2.txt" , "r")as f2:
    data_1= f1.read()
    data_2= f2.read()

with open("merge.txt", "w") as  mf:
    mf.write(data_1 + "\n" + data_2)

print("File merged Succesfully :")
