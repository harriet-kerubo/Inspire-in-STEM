#!/usr/bin/python
############################################
#   Name: Harriet Kerubo
#   Date: 6/6/2022

#############################################


import operations
from teachers import Teachers

print(operations.add_numbers(3,5))
print(operations.div_numbers(4,2))
print(operations.sub_numbers(40,3))
print(operations.mult_numbers(10,10))



new_teacher = Teachers("Mr John",12464,"Literature")
print(new_teacher.get_tsc_no())
print(new_teacher.salary())
print(new_teacher.subject())