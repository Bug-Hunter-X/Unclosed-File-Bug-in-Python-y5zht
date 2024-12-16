def function_with_unclosed_file_fixed(filename):
    f = None
    try:
        f = open(filename, 'w')
        # ... some code that might raise an exception ...
        f.write('This is some text')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if f:
            f.close()

#Example
function_with_unclosed_file_fixed("my_file.txt")
