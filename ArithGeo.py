#Checks if array of numbers is an arithmetic or geometric sequence
def ArithGeo(arr): 
  diff = arr[1]-arr[0]
  try:
    gdiff = arr[1]/arr[0]
  except:
    gdiff = 0
  arit = False
  geo = False
  for n in range(1,len(arr)):
    if (arr[n]== arr[n-1]+diff):
      arit = True
    else:
      arit = False
      break
  if(arit == True):
    return "Arithmetic"

  for n in range(1,len(arr)):
    if(arr[n]== arr[n-1]*gdiff):
      geo = True
    else:
      geo = False
      break
  if(geo == True):
    return "Geometric"
  
  return "-1"
    

print ArithGeo(raw_input())    