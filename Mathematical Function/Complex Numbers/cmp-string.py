# Example
complex_number = 3 + 4j
string_representation = str(complex_number)
 
print(type(complex_number))
print("String representation using str():", string_representation)
print(type(string_representation))


# Example
# Using format()__ method

complex_number = 3 + 4j
formatted_string = "Real: {:.2f}, Imaginary: {:.2f}".format(complex_number.real, complex_number.imag)
 
print(type(complex_number))
print("Formatted string using format():", formatted_string)
print(type(formatted_string))