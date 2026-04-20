#create a numpy array from the even factors of a given numbers

import numpy as np

def even_factors_array(n):
    factors = []
    
    # Find factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    # Filter even factors
    even_factors = [x for x in factors if x % 2 == 0]
    
    # Convert to NumPy array
    arr = np.array(even_factors)
    
    return arr

# Example
num = 12
result = even_factors_array(num)
print("Even factors array:", result)


# Even factors array: [ 2  4  6 12]