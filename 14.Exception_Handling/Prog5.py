#with out file mode raise exception
try:
    f = open("Sample.txt") #with exception
    #f = open("../Sample.txt", 'w') #with out exception
    f.write("Hi Welcome To Python Students")
    f.close()
except:
    print("Something went wrong when writing to the file")
finally:
    print("Work Over")