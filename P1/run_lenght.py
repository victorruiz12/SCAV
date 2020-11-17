# importing the collections
import collections


# function
def run_length_encoding(string):
    # initializing the count dict
    count_dict = collections.OrderedDict.fromkeys(string, 0)
    # iterating over the string
    for char in string:
        # incrementing the frequency
        count_dict[char] += 1
    # initializing the empty encoded string
    encoded_string = ""
    # joining all the chars and their frequencies
    for key, value in count_dict.items():
        # joining
        encoded_string += key + str(value)
        # printing the encoded string
        print(encoded_string)


# initializing the strings
string = "victorputoamo"
# invoking the function
run_length_encoding(string)
# another string
string = "aaabbbccc"
run_length_encoding(string)
