# strings having length greater than 5


strings = input("Enter any String seperated by space: ")
result = list(filter(lambda x: len(x)> 5), strings)
print("Strings with length > 5: ", result)