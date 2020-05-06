#UDACITY
#Linear Searching - It's a searching algorithm taking O(n)
import time
start_time = time.process_time()
def linear_search(input_array, value):
	if value in input_array:
		for i in range(len(input_array)):
			if input_array[i] != value:
				continue
			else:	
				return input_array.index(value) 	

	return -1


test_list = [1,3,9,11,12,14,15,19,29,30]
test_val1 = 25
test_val2 = 15
print(linear_search(test_list, test_val1))
print(linear_search(test_list, test_val2))
print(time.process_time() - start_time)


#Binary Searching - It's a seraching algorithm taking O(log n). This is a preferred one. All test cases passed!
start_time2 = time.process_time()

def binary_search(input_array, value):
	if value in input_array:
  		low = 0
  		high = len(input_array)-1
  		while(low<=high):

	  		mid = int((high + low)/2)
	  		if input_array[mid] == value:
	  			return mid
	  		elif input_array[mid] < value:
	  			low = mid + 1
	  		else:
	  			high = mid -1
	else:
		return -1	

test_list = [1,3,9,11,12,14,15,19,29,30]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(time.process_time() - start_time2)


