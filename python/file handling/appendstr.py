string = input("Enter the string : ")
f4 = open("demo.txt","a")
f4.write("\n"+string)
print(string,"has been appended in file.")
f4.close()
