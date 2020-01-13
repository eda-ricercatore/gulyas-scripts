#!/usr/local/bin/python3
results_size_per_dimension = 4
temp_list_per_dimension_in_matrix = [0]*results_size_per_dimension
matrix_tracking_comparisons = []
for i in range(results_size_per_dimension):
  matrix_tracking_comparisons.append(temp_list_per_dimension_in_matrix)
print(matrix_tracking_comparisons)
for i in range(4):
  for j in range(4):
    print("(i,j) is: (",i,",",j,").")
print("========================")
print("Better enumeration.")
for i in range(4):
  for j in range(i,4):
    print("(i,j) is: (",i,",",j,").")
print("========================")
print("Best enumeration.")
for i in range(4):
  for j in range(i+1,4):
    print("(i,j) is: (",i,",",j,").")
print("========================")
print("Desired comparison.")
print("(",0,",",1,").")
print("(",0,",",2,").")
print("(",0,",",3,").")
print("(",1,",",2,").")
print("(",1,",",3,").")
print("(",2,",",3,").")
