from read_input_file import read_input_file

def list_user_data(all_user_data):
    return all_user_data

def show_user_incomes(all_user_data):
    output=[]
    for key in all_user_data:
        output+=all_user_data[key]['income']
    return list(sorted(output))

def show_user_savings(all_user_data):
    pass

def show_user_deposits(all_user_data):
    pass

def show_user_expenses(all_user_data):
    output=[]
    for key in all_user_data:
        output+=all_user_data[key]['expense']
    return list(sorted(output))

def list_user_expenses_ordered_by_categories(all_user_data):
    output=[]
    for key in all_user_data:
        output+=all_user_data[key]['expense']
    output=sorted(sorted(output),key=lambda x:x[-1])
    return output


def show_user_data_per_date(date, all_user_data):
    return (all_user_data[date])


def list_income_categories(all_user_data):
    incomes=[]
    for key in all_user_data:
        incomes+=all_user_data[key]['income']
    output=[incomes[i][1] for i in range(len(incomes))]
    return list(sorted(set(output)))

def list_expense_categories(all_user_data):
    expenses=[]
    for key in all_user_data:
        expenses+=all_user_data[key]['expense']
    output=[expenses[i][1] for i in range(len(expenses))]
    return list(sorted(set(output)))


def add_income(income_category, money, date, all_user_data):
    if date in all_user_data:
        all_user_data[date]['income']+=[(money,income_category)]
    else:
        all_user_data[date]={'income':[(money,income_category)],'expense':[]} 
    return all_user_data

def add_expense(expense_category, money, date, all_user_data):
    if date in all_user_data:
        all_user_data[date]['expense']+=[(money,expense_category)]
    else:
        all_user_data[date]={'income':[] ,'expense':[(money,expense_category)]} 
    return all_user_data
def main():
    user_data = read_input_file()
    print('Hello Peter!')
    choice = ''
    while choice != 10:
        print('Choose one of the following options to continue:')
        print('1 - show all data')
        print('2 - show data for specific date')
        print('3 - show expenses, ordered by categories')
        print('4 - add new income')
        print('5 - add new expense')
        print('6 - show expense categories')
        print('7 - show income categories')
        print('8 - show user expenses')
        print('9 - show user incomes')
        print('10 - exit')
        choice = int(input())
        if choice == 1:
            file=open('money_tracker.txt','r')
            lines=file.readlines()
            output = ''.join(lines)
            file.close()
            print(output)
        elif choice == 2:
            try:
                date=input('Check for date -> ')
                output=show_user_data_per_date(date,user_data)
                for key in output:
                    print(key.upper()+'S')
                    for values in output[key]:
                        print(str(values[0])+', ' + values[1])
            except Exception as e:
                print('\nInvalid date!')
        elif choice == 3:
            output = list_user_expenses_ordered_by_categories(user_data)
            for item in output:
                print(str(item[0]) + ', ' + item[1])
        elif choice == 4:
            income_category = str(input('Income category -> '))
            money = float(input('Money -> '))
            date = str(input('Date -> '))
            user_data = add_income(income_category,  money, date, user_data)
        elif choice == 5:
            expense_category = str(input('Expense category -> '))
            money = float(input('Money -> '))
            date = str(input('Date -> '))
            user_data = add_expense(expense_category, money, date, user_data)
        elif choice == 6:
            output = list_expense_categories(user_data)
            for item in output:
                print(item)
        elif choice == 7:
            output = list_income_categories(user_data)
            for item in output:
                print(item)
        elif choice == 8:
            output = show_user_expenses(user_data)
            for item in output:
                print(str(item[0]) + ', ' + item[1])
        elif choice == 9:
            output = show_user_incomes(user_data)
            for item in output:
                print(str(item[0]) + ', ' + item[1])

        print()

if __name__ =='__main__':
    main()
