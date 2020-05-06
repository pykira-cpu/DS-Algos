#Udacity
#Sorting algorithms : Bubble sort, Merge sort and Quick sort

#creating randomized integers in an array
from random import randint
def create_array( length = 10, maxint = 50):
	new_arr = [randint(0,maxint) for i in range(length)]
	return new_arr

'''
Bubble Sorting algorithm:

Time Complexity  : O(n^2) (quadratic time increase), best case is O(n) which is highly unlinkely to occur
Space Complexity : O(1) (constant)
'''

def bubble_sort(arr):
	swapped = True
	while swapped:
		swapped = False
		for i in range(1,len(arr)):
			if arr[i-1]>arr[i]:
				arr[i-1],arr[i] = arr[i],arr[i-1]
				swapped = True 
	return arr

#return True if the passed array is sorted successfully or not. We are using python's built-in sort function
def is_sort(arr):
	return x_bsorted == sorted(arr)

x = create_array()
print(x)
x_bsorted = bubble_sort(x)
print(x_bsorted)
print(is_sort(x))


'''
Merge sort algorithm:

Time complexity  : O(nlogn)
Space complexity : O(n)(Linear space)
'''

#a function to merge 2 sorted lists
def merge(x,y):
	z =[]
	x_idx,y_idx = 0,0
	while x_idx<len(x) and y_idx<len(y):
		if x[x_idx]<y[y_idx]:
			z.append(x[x_idx])
			x_idx += 1
		else:
			z.append(y[y_idx])
			y_idx += 1

	if x_idx == len(x):
		z.extend(y[y_idx:])
	else:
		z.extend(x[x_idx:])

	return z

#check for merging  
print(merge([1,3,2,7,8],[4,5,6,9,10]))
print(merge([0,2,5],[1,3,4]))


def merge_sort(x):

	if len(x)<=1:
		return x
	else:
		#split the list into half and recursing them 
		left,right = merge_sort(x[:int(len(x)/2)]), merge_sort(x[int(len(x)/2):])

		#merge the sorted sublists
		return merge(left,right)

a =create_array()
print(a)
merge_sort_a = merge_sort(a)
print(merge_sort_a)


'''
Quick sort algorithm:

Time complexity  : O(n^2)(worst case) , O(nlogn)(best case)
Space complexity : O(logn) 
'''
def quick_sort(a):
	if len(a)<=1:
		return a
	pivot = a[randint(0,len(a)-1)]
	smaller,equal,larger =[],[],[]
	for i in a:
		if pivot > i:
			smaller.append(i)
		elif pivot == i:
			equal.append(i)
		else:
			larger.append(i)

	return quick_sort(smaller)+equal+quick_sort(larger)		

n = create_array()
print('Unsorted : ',n)
print('Sorted : ',quick_sort(n))
