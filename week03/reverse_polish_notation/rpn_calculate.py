def rpn_calc(expression):
    operators=['+','-','*','/','//','**']
    stack=[]
    expression=list(expression.split())

    for exp in expression:
        if exp.isdigit():
            stack.append(exp)
        if exp == 'ABS':
            prev=stack.pop()
            stack.append(prev + '*(-1)')
        if exp =='SQRT':
            prev=stack.pop()
            stack.append(prev+'**0.5')
        if exp == 'MAX':
            elements=[]
            while len(stack) !=0 :
                elements.append(eval(stack.pop()))
            max_elem=max(elements)
            stack.append(str(max_elem))
        if exp == 'MIN':
            elements=[]
            while len(stack) != 0 :
                elements.append(eval(stack.pop()))
            min_elem=min(elements)
            stack.append(str(min_elem))
        if exp in operators:
            second=stack.pop()
            first=stack.pop()
            stack.append('('+ first + exp + second +')')

    return eval(stack[0])
