#create a file
file =open("yaml.txt",'w')
file.write("This is my file\n")
file.close()
file=open("yaml.txt",'r')
con=file.read()
print(con)
file.close()