from itertools import product
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

#I = {num for num in float_range(0, float('inf'), 1)} # integers
#N = {num for num in float_range(1, float('inf'), 1)} # natural numbers
#R = {(num1 / num2) for num1 in float_range(0, float('inf'), 1) for num2 in float_range(1, float('inf'), 1)} # rational numbers

#A = {1, 2, 3}
#B = {2, 3, 5}

A = set()
B = set()

a_input = int(input("Enter the number of elements in set A, starting with the size: "))
for i in range(0, a_input): 
    ele = int(input())
    A.add(ele)
    
b_input = int(input("Enter the number of elements in set B, starting with the size: "))
for i in range(0, b_input): 
    ele = int(input())
    B.add(ele)

# Create new sets
print("The union of these sets is: ", A | B)
print("The intersection of these sets is: ", A & B)
print("The difference of these sets is: ", A - B)
print("The symmetric difference of these sets is: ", A ^ B)
    
# Set cardinality
print("The cardinality of set A is: ", len(A))
print("The cardinality of set B is: ", len(B))

# Complement of a set and a universal set. If no universal set is given, say so.

# Cartesian product of two sets.
print("The Cartesian product of thse sets is: ", product(A, B))