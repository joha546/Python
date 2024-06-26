'''
How to Use the Return Keyword in Python
In Python, you can use the return keyword to exit a function so it goes back to where it was called. That is, send something out of the function.

The return statement can contain an expression to execute once the function is called.

The example below demonstrates how the return keyword works in Python:

'''

def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)

# Output: 64

'''
I defined a function named multiplyNum and passed it num1 as an argument
Inside the function, I used the return keyword to specify that I want num1 to be multiplied by 8
After that, I called the function, passed 8 into it as the value for the num1 argument, and assigned the function call to a variable I named result
With the result variable, I was able to print what I intended to do with the function to the terminal
'''