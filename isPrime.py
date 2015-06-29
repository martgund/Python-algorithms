# Checks if number is a prime
def isPrime(number):
    if number==2 or number==3: return True
    if number%2==0 or number<2: return False
    for i in range(3,int(number**0.5)+1,2):
        if number%i==0:
            return False    
    return True
print isPrime(input())