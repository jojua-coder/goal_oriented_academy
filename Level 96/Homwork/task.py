#1 List Filtering
def filter_list(l):
    filtered = []
    for i in l:
        if type(i) == int:
            filtered.append(i)
    return filtered

#2 Delete occurrences of an element if it occurs more than n times
def delete_nth(order,limit):
    new_list = []
    
    for i in order:
        if new_list.count(i) >= limit:
            continue
        else:
            new_list.append(i)
    return new_list