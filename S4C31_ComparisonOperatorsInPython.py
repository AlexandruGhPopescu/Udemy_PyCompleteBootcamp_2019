'''Operator | Description Example'''
#     ==    |  If the values of two operands are equal, then the condition becomes true. (a == b) is not true.
#     !=    |  If values of two operands are not equal, then condition becomes true. (a != b) is true.
#     >     | If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
#     <     | If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
#     >=    |  If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. (a >= b) is not true.
#     <=    |  If the value of left operand is less than or equal to the value of right operand, then condition becomes true. (a <= b) is true.


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

print(f"\t1==1 is : {1==1}")
print(f"\t2==1 is : {2==1}\n")
print(f"\t'hello'=='bye' is : {'hello'=='bye'}")

print(f"\t'Bye'=='bye' is : {'Bye'=='bye'}\n")
# in string comparison letter capitalisation counts
# the above example will return False

print(f"\t'2'==2 is : {'2'==2}")
# Python take into account type comparison
# the above example string ==  integer will return False

print(f"\t2.0==2 is : {2.0==2}\n")
# exception from the rule above
# float == integer or integer == float will return Ture

print(f"\t1!=1 is : {1!=1}")
print(f"\t2!=1 is : {2!=1}\n")

print(f"\t1<1 is : {1<1}")
print(f"\t2>1 is : {2>1}\n")


print(f"\t1<=1 is : {1<=1}")
print(f"\t2>=1 is : {2>=1}\n")


print('\n--- THEND ---')
