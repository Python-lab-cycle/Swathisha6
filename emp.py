import csv
with open('employee.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("emp no: Empname")
    print(".........")
    for row in data:
        print(row['empno'],row['empname'])
