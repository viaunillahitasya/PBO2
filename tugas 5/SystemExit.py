print("Program that uses BaseException as base class.")
try:
    raise SystemExit  
except BaseException:
    print("Specifying BaseException in this block works.")