print("Write to file DB")
productid = input("Enter product ID: ")

f = open ("filedb.txt", "a")
f.write(productid + "\n")
f.close()
