

def multiples3And5(num1,num2,limit):
    '''Time Complexity: O(n), Space Complexity: O(1)'''
    sum = 0
    for num in range(1,limit+1):
        if(num % num1 == 0 or num % num2 == 0):
            sum = sum + num
    return sum

def BS_multiples3And5(num,limit):
    '''Time Complexity: O(1), Space Complexity: O(1)'''
    x = limit//num
    return ((x*(x+1))/2)*num

if __name__ == "__main__":
    

    num1 = 3
    num2 = 5
    limit = 999
    
    # My Solution
    sum = multiples3And5(num1,num2,limit)
    print(sum)

    # Better Solution
    sum = BS_multiples3And5(num1,limit) + BS_multiples3And5(num2,limit) - BS_multiples3And5(num1*num2,limit)
    print(sum)