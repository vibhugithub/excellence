# Question 3:-
# Python 3 program to count maximum consecutive 1's. Returns count of maximum consecutive 1's in binary 

def getMaxLength(bin_array: list):
	if len(bin_array) <= 0 or type(bin_array) != list:
		return 0

	# intitialize count 
	repeatitions = 0
	
	# initialize max 
	result_count = 0

	for element in bin_array:

		# If 1 is found, increment count 
		# and update result if count 
		# becomes more. 
		if element == 1:
			# increase count 
			repeatitions += 1
			result_count = max(result_count, repeatitions)
			
		else:
			# Reset count when the repeatition is breaked
			repeatitions = 0
			
	return result_count

# Driver code 
arr = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

print(getMaxLength(arr))
