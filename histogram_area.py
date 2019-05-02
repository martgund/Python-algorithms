def max_area_histogram(histogram): 
      
    # This function calulates maximum  
    # rectangular area under given  
    # histogram with n bars 
  
    stack = list() 
    max_area = 0
  
    index = 0
    while index < len(histogram):  
        if (stack.len()==0) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
        else: 
            top_of_stack = stack.pop() 
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
            max_area = max(max_area, area) 
    
    while stack: 
        top_of_stack = stack.pop() 
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
        max_area = max(max_area, area) 
    return max_area 
  
hist = [8, 0, 5, 0, 5, 1, 6] 
print("Maximum rectangular area is",  
       max_area_histogram(hist)) 
