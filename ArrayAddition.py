#Checks if some numbers in an array add up to the largest number in the array

def ArrayAdditionI(arr): 
  num = max(arr)
  arr.sort()
  if len(subsetsum(arr,num))!= 1:
    return "true"
  return "false"
    

def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)


print ArrayAdditionI(raw_input())    