#Smart Data Type Detector.
User = input("Enter the data :")

print("*************************/RESULT/******************************")
print(f"The value of the user is {User}")
print(f"The type of value is {type(User)}")

# FOR INT
try:
    int_val = int(User)
    print(f"Convert to int  :  {int_val}")
except ValueError:
    print("Convert to int  : Not possible")
# Float
try:
  float_val = float(User)
  print(f"convert to float :  {float_val}")
except ValueError:
  print("Convert to float  : Not possible")
# bool
print(f"Bool value      : {bool(User)}")



# predict
print("##################33")
try:
  int(User)
  print("It is an int")
except ValueError:
  try:
    float(User)
    print("It is an float")
  except ValueError:
    print("Its string")