def args(arg1, arg2):
    print (arg1, " ", arg2)
    return args
    
    
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result
    
    
print (power(3))
print (power(num=5, x=3))