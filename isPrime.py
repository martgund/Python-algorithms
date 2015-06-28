def isPrime(num): 

  
  for i in range(2,num):
    if (num % i) == 0:
    	return "false"
    else:
      return "true"

  return "false"
    
    

print isPrime(raw_input())           
