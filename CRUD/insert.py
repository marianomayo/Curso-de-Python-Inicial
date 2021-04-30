from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData

def insert():
    try:
        employeeid = input('Enter Employee id: ')
        employeename = input('Enter Name: ')
        employeeage = input('Enter age: ')
        employeecountry = input('Enter Country')
        db.Employees.insert_one({
            'id': employeeid,
            'name': employeename,
            'age': employeeage,
            'country': employeecountry
        })
        print('Inserted data successfully')
    
    except ImportError:
        platform_specific_module = None