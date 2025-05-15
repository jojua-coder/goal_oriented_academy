#1 Who likes it?
def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    
#2 Create Phone Number
def create_phone_number(n):
    return  f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

#3 Find the odd int
def find_it(numbers_list):
    for i in numbers_list:
        if numbers_list.count(i) % 2 != 0:
            return i
        

#4 Row Weights
def row_weights(array):
    team1 = []
    team2 = []
    
    
    for i in range(len(array)):
        if i % 2 == 0:
            team1.append(array[i])
        else:
            team2.append(array[i])
    
    return (sum(team1),sum(team2))

#5 Largest pair sum in array
def largest_pair_sum(numbers): 
    numbers= sorted(numbers)
    return (numbers[-1]+numbers[-2])