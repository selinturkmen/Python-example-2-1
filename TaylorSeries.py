import math

def taylor_series_ln(x, terms):
    """
    Write your code inside this function.
    """
    taylor_series = 0
    taylor_series_parts = 0
    for i in range(terms):
        if (terms%2== 0):
         taylor_series_parts = (x**terms)/(-terms)
         taylor_series += taylor_series_parts
        else :
         taylor_series_parts = (x**terms)/(terms)
         taylor_series += taylor_series_parts       
    return taylor_series

def main():
    """
    You can test your taylor_series_ln function via the function calls below.
    You can add more tests if you want to, but you do not have to. 
    What matters is whether your taylor_series_ln function is correct.
    """
    result = 0
    #result = taylor_series_ln(0.8, 2)
    #result = taylor_series_ln(0.8, 5)
    #result = taylor_series_ln(0.8, 10)
    #result = taylor_series_ln(0.8, 30)
    result = taylor_series_ln(0.8, 100)
    
    print(result)
    

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()