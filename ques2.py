# Question 2:-
# Python program 


# dict_1 --> student_id(int): student_name(str)
dict_1st = {1: 'Name 1', 2: 'Name 2', 3: 'Name 3' }

# dict_2 --> student_id(int): exam_score(int)
dict_2nd = {1: 50, 2: 60, 3: 70}

# Create function
def find_max_value(dict_1: dict,dict_2: dict):
    if len(dict_1) != len(dict_2) or len(dict_2) <= 0:      # Checking the size of both dictionary is equal or not 
        raise Exception("Dictionary must contain atleast 1 element and must be of same size")
    
    dict_max = {}
    dict_max_with_name = {}
    max_val = -99999
    for item in dict_2.items():
        if item[1] > max_val:
            max_val = item[1]
            dict_max_with_name = {dict_1[item[0]]: item[1]}
            dict_max = {item[0]:item[1]}
        elif item[1] == max_val:
            dict_max_with_name.update({dict_1[item[0]]: item[1]})
            dict_max.update({item[0]:item[1]})
        else:
            pass
    
    """
    uncomment below return line if you want to replace names in place of id's 
    """
    # return dict_max_with_name
    return dict_max


# Driver code

try:
    max_dict = find_max_value(dict_1st, dict_2nd)
    print(max_dict)
except Exception as exception:
    print(exception)