def isPalindrome(x):
        number = x 
        reversed_number = 0 
        while number > 0:
            num = number % 10
            reversed_number = (reversed_number *10)+ num
            x = x // 10
        print(reversed_number)
        if x == reversed_number:
            return True
        else:
            return False
        
print(isPalindrome(121))