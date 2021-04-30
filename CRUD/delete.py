from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData


def delete():
    try:
        criteria = input('\n Enter employee id to delete \n')
        db.Employees.delete_many({'id': criteria})
        print('\n Deletion successful\n')

    except ImportError:
          platform_specific_module = None