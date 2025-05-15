#1 Find the odd int
def find_it(seq):
    result=[]
    for i in seq:
        count=seq.count(i)
        if count %2==1:
            result.append(i)
    return result[0]