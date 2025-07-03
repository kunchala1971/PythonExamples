import csv
# with open("data.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerow(["id","name","course"])
#     writer.writerow([1,"Rohit","python"])
#     writer.writerow([2,"Vikram","Java"])

with open("data.csv") as file:
    reader=csv.reader(file)
    # print(list(reader))
    for row in reader:
        if(len(row)>0):
            print(row)