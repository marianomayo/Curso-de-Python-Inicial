import insert
import read
import update
import delete

class Programa:

    def __init__(self):
        self.dato = 1
    
    def menu(self):
        while self.dato:
            selecction = input('\n Select 1 to insert, 2 to update, 3 to read, 4 to delete')

            if selecction == '1':
                insert.insert()
            elif selecction == '2':
                update.update()
            elif selecction == '3':
                read.read()
            elif selecction == '4':
                delete.delete()
            else:
                print('\n INVALID SELECTION \n')

persona1 = Programa()
persona1.menu()