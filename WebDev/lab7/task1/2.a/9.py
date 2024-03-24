def wrap(string, max_width):
    wrapped_string = ""
    for i in range(0, len(string), max_width):
        wrapped_string += string[i:i+max_width] + '\n'  
    return wrapped_string

string = input()
max_width = int(input())

result = wrap(string, max_width)
print(result)
