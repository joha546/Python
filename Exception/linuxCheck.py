def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except RuntimeError as error:
    print(error)               # In the except clause, you assign the RuntimeError to the temporary variable error—often also called 
    #err—so that you can access the exception object in the indented block. In this case, you’re printing the object’s string representation, which corresponds to the error message
    #  attached to the object.
    print("The linux_interaction() function wasn't executed.")


# ...

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exceptions.")