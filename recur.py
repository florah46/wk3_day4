def sum_number(x):
    
    if not isinstance(x,list):
        return "Invalid"
    total = 0
    for i in x:
        if isinstance(i,int):
           total += i
        elif isinstance(i,list):
            total += sum_number(i)
    return total
if __name__ == '__main__':
    print(sum_number(x=[2,8,5,[5,9]]))