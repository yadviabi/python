#!/usr/bin/env python3

import random
def sum(input):
    total=0
 
    for ele in input:
        total=total+ele
           
    print("the total is {}".format (total))
    return total

def calc():
    input=[]
    total=0

    for i in range(10):
    
        rand_value=random.randrange(1,100)
        total=total+rand_value
        input.append(rand_value)

    return total,input



total,input=calc()
total_sum=sum(input)
        
if total_sum==total:
    print("sum is equal and the value is {}.the input is {}".format (total,input))
else:
    print("the sum is unequal")