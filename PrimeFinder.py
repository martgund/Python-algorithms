# Returns the nth primenumber

def PrimeFinder(num): 
  
  primes = []
  counter = 0
  number = 2
  while (counter < num):
    if isPrime(number):
      counter +=1
      primes.append(number)
    number +=1
  return  primes[num-1]
    
def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,num):
            if num % div == 0:
                return False
        return True
print (PrimeFinder(input())  )  