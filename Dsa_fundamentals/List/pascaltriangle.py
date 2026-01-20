def pascal_triangle(n):
   # how to create double list
   triangle = []
   for i in range(n): # Iterate through the number of rows from 0 to n-1
       row = [0] * (i + 1) # Initialize a row with zeros
       row[0], row[-1] = 1, 1 # Set the first and last elements to 1
       for j in range(1, i): # Fill in the middle elements
           row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] # Calculate the value based on the previous row
       # Append the row to the triangle
       triangle.append(row)
   return triangle
