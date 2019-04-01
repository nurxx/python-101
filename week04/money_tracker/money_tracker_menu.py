from money_tracker import *

def menu(money_tracker):
    print('Hello user!')
    choice = ''
    user_data = Parser.parse_money_tracker_data('money_tracker.txt')
    while choice is not '9':
        print('Choose one of the following options to continue:')
        print('1 - show all data')
        print('2 - show data for specific date')
        print('3 - show expenses ordered by subcategories')
        print('4 - show incomes in reverse ordered by subcategories')
        print('5 - add new expense')
        print('6 - add new income')
        print('7 - show user incomes')
        print('8 - show user expenses')
        print('9 - exit')

        choice = input()
        if choice is '1':
            money_tracker.show_all_data()
        elif choice is '2':
            date = input('Search for date -> ')
            money_tracker.show_data_for_specific_date(date)
        elif choice is '3':
            money_tracker.show_expenses_ordered_by_subcategories()
        elif choice is '4':
            money_tracker.show_incomes_in_reversed_order_by_subcategories()
        elif choice is '5':
            amount = input('Amount: ')
            sub_category = input('Subcategory: ')
            date = input('Date: ')
            date = '=== ' + date + ' ==='
            money_tracker.add_new_expense(amount,sub_category,date)
            added = False
            for data in user_data:
                for sub_data in data:
                        if date in sub_data:
                            data.append('{0}, {1}, New Expense\n'.format(amount,sub_category))
                            added = True
            if added == False:
                user_data += [[date,'\n{0}, {1}, New Expense'.format(amount,sub_category)]]

        elif choice is '6':
            amount = input('Amount: ')
            sub_category = input('Subcategory: ')
            date = input('Date: ')
            money_tracker.add_new_income(amount,sub_category,'=== ' + date + ' ===')
            added = False
            for data in user_data:
                for sub_data in data:
                        if date in sub_data:
                            data.append('{0}, {1}, New Income\n'.format(amount,sub_category))
                            added = True
            if added == False:
                user_data += [[date,'\n{0}, {1}, New Income'.format(amount,sub_category)]]
        elif choice is '7':
            money_tracker.show_user_incomes()
        elif choice is '8':
            money_tracker.show_user_expenses()
        elif choice is '9':
            updated = ''
            for data in user_data:
                for item in data:
                    updated+=item
            f = open('money_tracker.txt','w')
            f.write(updated)
            f.close()


