def LongestWord(sen): 

  listen = unicode(sen).split()
  wordlength = 0
  lword = None
  for word in listen:
    lista = list(word)
    count = 0
    for n in range(0,len(word)):
      if lista[n].isalpha():
        count += 1
    if count > wordlength:
      wordlength = count
      lword = word
      
  return lword
    

print LongestWord(raw_input())           
