from heapq import nlargest
dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
highest = nlargest(3, dict, key=dict.get)
print(highest)
