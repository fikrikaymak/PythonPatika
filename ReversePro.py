'''
2- A type function that returns the parts inside the given list. If the elements inside the listen also contain the list, return their elements as well. For example:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
'''
l = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(x):
    for i in x:
        i.reverse()
    x.reverse()
    
reverse(l)
print(l)