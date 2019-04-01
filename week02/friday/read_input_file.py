def read_input_file():
    file = open('money_tracker.txt','r')
    lines= file.readlines()
    info=dict()
    dates=[]
    str_dates=[]
    for index,line in enumerate(lines):
        if '===' in line:
            line=list(line.split())
            str_dates+=[line[1]]
            dates+=[index]
    dates += [len(lines)]
    dates=[(dates[i]+1,dates[i+1]) for i in range(len(dates)-1)]
    #print(dates)
    #print(str_dates)

    for i in range(len(dates)):
        incomes=[]
        expenses=[]
        for index in range(dates[i][0],dates[i][1]):
            lines[index]=list(lines[index].split(', '))
            #print(lines[index])
            info[str_dates[i]]={'income':incomes , 'expense' : expenses}
            if 'New Expense' in lines[index][2]:
                expenses.append((float(lines[index][0]),lines[index][1]))
                info[str_dates[i]]['expense'] = expenses
            if 'New Income' in lines[index][2]:
                incomes.append((float(lines[index][0]),lines[index][1]))
                info[str_dates[i]]['income'] = incomes

    file.close()

    return info
