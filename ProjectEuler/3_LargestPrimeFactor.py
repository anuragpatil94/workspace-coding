def LargestPrimeFactor(number):
    # Time Complexity: O(sqrt(n)*sqrt(n)) -- Not sure if my time analysis is correct
    largest = -1
    num = 1
    while num*num < number:
        # check for factor
        if number % num == 0:
            # get factor pairs
            arrFactorPairs = [num,number/num] if(number/num != num) else [num]
            # Check for Prime
            for factor in arrFactorPairs:
                flag = 0
                if factor <=1:
                    continue
                if factor < 3:
                    largest = factor
                if (factor % 2 == 0 or factor % 3 == 0):
                    continue
                i = 5
                while i * i <= factor:
                    if factor % i == 0 or factor % (i + 2) == 0:
                        flag = 1
                        break
                    i = i + 6
                    
                if flag == 0:
                    largest = factor
        num = num + 1            
            
    return largest
            


if __name__ == "__main__":
    print(LargestPrimeFactor(600851475143))