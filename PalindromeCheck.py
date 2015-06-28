# Returns true if string entered is a palindrome
def Palindrome(str): 
  strip = str.replace(" ", "")
  if strip == (strip[::-1]):
    return "true"
  return "false"
    
    

print Palindrome(raw_input())           
