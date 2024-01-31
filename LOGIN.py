from getpass import getpass
from DML import GUI

#LOGIN#
def okno_logowania():
    while True:
        login = input('Enter login: ')
        password = getpass('Enter password: ')
        if (login == 'login') and (password == 'password'):
            GUI()
            break
        else:
            print('\nNOOO\nincorrectly values!!!!\n')
