import time
def selection_sort(data,drawData,timeTick):
    
    n = len(data)
    for s in range(n):
        min_idx = s
         
        for i in range(s + 1, n):
             
            # For sorting in descending order
            # for minimum element in each loop
            if data[i] < data[min_idx]:
                min_idx = i
            drawData(data, ['yellow' if x == i or x == i+1 else 'red' for x in range(len(data))] )
            time.sleep(timeTick)
 
        # Arranging min at the correct position
        (data[s], data[min_idx]) = (data[min_idx], data[s])
        

 
