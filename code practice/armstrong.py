def armstrongNumber (n):
        num = n
        print(num)
        sum = 0 
        for i in range(3):
            temp = n % 10
            sum = sum + temp**3
            n = n//10
        print(sum)
        if num == sum:
            return True
        else:
            return False
print(armstrongNumber(371))

