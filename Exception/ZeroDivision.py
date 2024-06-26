try:
    n=int(input())
    m=int(input())
    result=n/m

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero idiot")

except ValueError as e:
    print(e)
    print("Enter only numbers please!!")

except Exception as e:
    print(e)
    print("Something Went wrong")

else:
    print(result)

finally:
    print("This will be executed")
