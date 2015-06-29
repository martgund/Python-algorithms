# Returns "1" if parenthases are used correctly.
def BracketMatcher(string): 

  listen = list(string)
  l = 0
  r = 0
  for n in range(0, len(listen)):
    if listen[n] == '(':
      l += 1
    elif listen[n] == ')':
      r += 1
  if l == r:
    return "1"
  return "0"

print BracketMatcher(raw_input())           
