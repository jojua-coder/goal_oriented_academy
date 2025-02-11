#1 Dollars and Cents
def format_money(amount):
    amount = str(amount)
    amount = amount.split(".")    
    
    if len(amount) == 1:
        return f"${amount[0]}.00"
    
    

    elif len(amount) == 2:
        if len(amount[1]) == 1:
            return f"${amount[0]}.{amount[1]}0"
        elif len(amount[1]) == 2:
            return f"${amount[0]}.{amount[1]}"
        

#2 Swap Values
def swap_values(args): 
    arg = args.copy()

    args[0] = arg[1]
    args[1] = arg[0]

    return args



# 3 Check same case
def same_case(a, b): 
    

    if a.isalpha() and b.isalpha():
        if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
            return 1
        elif(a.isupper() and b.islower()) or (a.islower() and b.isupper()):
            return 0
    else:
        return -1
    
# 4 Sum of Multiples
def sum_mul(n, m):
    
    if n <= 0 or m <=0 :
        return 'INVALID'
    
    
    sum = 0
    for i in range(n,m):
        if i % n == 0:
            sum += i
    return sum