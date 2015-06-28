def FirstReverse(str): 

  listen = list(str)
  lista = []
  for n in range(0,len(listen)):
    lista.append(listen[-1-n])
  return ''.join(lista)
    
    

print FirstReverse(raw_input())      

