#Returns "1" if mode is equal to mean
# else "0"

def MeanMode(arr): 
  arr.sort()
 
  if float(sum(arr))/float(len(arr)) == float(arr[len(arr)/2]):
    return "1"
  return "0"
    
    

print MeanMode(raw_input())           
