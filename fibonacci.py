def fibonacci(number):
    first,second=0,1
    for num in range(number):
       print(first, end=" ")
       first,second=second,first+second 
    
fibonacci(10)