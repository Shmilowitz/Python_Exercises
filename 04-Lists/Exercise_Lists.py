import timeit

#Exercise 1
print('\n')
print("Exercise 1")
my_list=list(range(1000001))
start = timeit.default_timer()
s = sum(my_list)
stop = timeit.default_timer()
print (s)
print(stop - start, "Sekunder")
print('\n')

#Exercise 2
print("Exercise 2")
one_list = list(range(1,21))
sum_result = (one_list[0] + one_list[-1]) * len(one_list) / 2
print(sum_result)
print('\n')

#Exercise 3
print("Exercise 3")
odd_list=list(range(1,20,2))
print(odd_list)
print('\n')

#Exercise 4
print("Exercise 4")
three_list=list(range(3,31,3))
print(three_list)
print('\n')

#Exercise 5
print("Exercise 5")
print('First solution')
#First solution
cube_list=list()
for x in range(1,11):
    cube_list.append(x**3)
print(cube_list)
print('\nSecond solution')
#Second solution
cube_list2 = list(x**3 for x in range(1,11))
print (cube_list2)
'''
1. Create a list with the interger values from one to one million. use min() and max() to make sure your list actually starts at one and ends at one million. also use the sum() function to compute the sum of all values and %timeit's execution time.
2. write a single line program that computes the sum of a range of integer values without using the sum() function and without using a loop
3 use the range() function to make a list of the odd numbers from 1 to 20. hint: in ipython and this notebooks you can see a functions help text by executing for example range?
4. create a  list of the multiples of 3 from 3 to 30
5. A number raised to the third power is called a cube. for example the cube of 2 is written as 2**3 in python. create a list of the first 10 cubes that is the cube of each integer from 1 through 10
'''
