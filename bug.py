def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.close() #This line might not be reached if an exception occurs

#Example
function_with_unclosed_file("my_file.txt")