from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client.EmployeeData

def read():
    try:
        empco1 = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empcon1:
            print(emp)

    except ImportError:
        platform_specific_module = None