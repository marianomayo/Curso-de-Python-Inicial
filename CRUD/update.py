from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client.EmployeeData

def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')
        
        db.Employees.update_once(
            {'id': criteria},
            {
                '$set':{
                    'name': name,
                    'age': age,
                    'country': country
                }
            }
        )
        print('\n Records updated successfuly \n')

    except ImportError:
        platform_specific_module = None