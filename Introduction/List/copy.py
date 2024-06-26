'''
Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. 
Any changes you make to the list through one variable will be seen through all other variables that refer to it.:
'''

rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object

rgba.append('Alpha')
print(rgb)