import numpy as np
data = np.array([45,36,54,67,49,20])
#elem greator than 50
print("elements greater than 50: ")
print(data>50)
#divisible by 5
numbers2 = data/5
print("after dividing each element by 5")
print(numbers2)


#output
#elements greater than 50: 
#[False False  True  True False False]
#after dividing each element by 5
#[ 9.   7.2 10.8 13.4  9.8  4. ]