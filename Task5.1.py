# CHANGING THE FORMAT OF A NUMBER
def format_number(num, fmt):   # fmt is the format type.
    return format(num, fmt)

# Call the function with 145 and 'o'
result = format_number(145, 'o') #o is used to format number in octal. 
print("Formatted result:", result)

#------------------------OUTPUT-----------------------
#Formatted result: 221