# raise NameError("HiThere")

try:
    raise NameError("HiThere")
except NameError:
    print("An exception Flew by!")
    raise