# list of numbers for testing the code 
numbers = [21, 30, 21, 61, 34, 100, 83, 21, 21, 57]  
res = []

def remove_duplicates(res):
    # using list comprehension to remove duplicates
    [res.append(x) for x in numbers if x not in res]
    #sorting the list in descending order before printing it 
    res.sort(reverse=True)
    return res
print("Original list of numbers: "
      + str(numbers))
# caling the function to display the new list
list_sorted=remove_duplicates(res)
print ("List after removing duplicates and sorting in descending order: " + str(res))
