from business_card_catalog import *

def info(card):
    print("####################\n")
    print('ID: {}'.format(card[0]))
    print('Full name: {}'.format(card[1]))
    print('Email: {}'.format(card[2]))
    print('Age: {}'.format(card[3]))
    print('Phone: {}'.format(card[4]))
    print('Additional info (optional): {}'.format(card[5]))
    print("####################\n")

if __name__ == '__main__':
    create_users_table()
    print("Hello! This is your business card catalog. What would you like? (enter \"help\" to list all available options)")
    command=''
    while command != 'exit':
        command=input('Enter command: ')

        if command == 'help':
            print(help())
        if command == 'add':
            name = input('Enter user name: ... ')
            email= input('Enter email: ... ')
            age=int(input('Enter age: ... '))
            phone=input('Enter phone: ... ')
            additional_info=input('Enter addional info (optional): ... ')
            if additional_info=="\n":
                add(name,email,age,phone,'NULL')
            else:
                add(name,email,age,phone,additional_info)

        if command == 'list':
            business_cards_catalog=list()
            for card in business_cards_catalog:
                info(card)

        if command == 'get':
            id=int(input('Enter id: ... '))
            print('Contact info: ')
            card=get(id)
            info(card)
            
        if command == 'delete':
            id=int(input('Enter id: ... '))
            print('Following contact is deleted successfully:')
            print(get(id))
            delete(id)


