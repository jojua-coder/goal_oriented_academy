#1 Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    return length * width * height

#2 No zeros for heros 
def no_boring_zeros(n):
    if n == 0:
        return 0
    n=str(n)   
    
    while n[-1]=="0":
        
        n=n[:-1]
        
    return int(n)
#3 Simple multiplication

def simple_multiplication(number) :
    # Your code goes here
    if number %2==0:
        return number *8
    else:
        return number *9
    
#4 Is he gonna survive?
def hero(bullets, dragons):
    return bullets>= dragons*2