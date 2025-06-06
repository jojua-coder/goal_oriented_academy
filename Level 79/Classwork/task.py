#1 Multiply
# function multiply(a, b){
#    return a * b
# }

#2 Even or Odd
# function evenOrOdd(number) {
#   if(number %2===0){
#     return "Even"
#   }else{
#     return "Odd"
#   }
# }

#3 Return Negative
# function makeNegative(num) {
#   if(num>0){
#     return -num
#   }else{
#     return num
#   }
# }

#4 Opposite number
# function opposite(number) {
#     return -number
# }

#5 Small enough? - Beginner
def small_enough(array, limit):
    for i in array:
        if i >limit:
            return False
    return True

#6 Largest pair sum in array
def largest_pair_sum(numbers): 
    numbers= sorted(numbers)
    return (numbers[-1]+numbers[-2])

#7 Stop gninnipS My sdroW!
def spin_words(sentence):
    sentence = sentence.split(" ")
    
    l = []
    
    for i in sentence:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    return " ".join(l)


#8 Delete occurrences of an element if it occurs more than n times
def delete_nth(order,limit):
    new_list = []
    
    for i in order:
        if new_list.count(i) >= limit:
            continue
        else:
            new_list.append(i)
    return new_list