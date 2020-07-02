for x in range(2, 11):
    print("Tablas del", x)
    print("-------------")
    for y in range(1, 11):
        print(x, "+", "{:2.0f} = ".format(y), "{:3.0f}".format(x+y), "  ", \
              x, "-", "{:2.0f} = ".format(y), "{:3.0f}".format(x-y), "  ", \
              x, "x", "{:2.0f} = ".format(y), "{:3.0f}".format(x*y), "  ", \
              x, "/", "{:2.0f} = ".format(y), "{:3.0f}".format(x/y)) 
    print(" ")    
    
    
# Print a MAX x MAX multiplication table
MAX = 18

# First, print heading
print(end="     ")
# Print column heading numbers
for column in range(1, MAX + 1):
    print(end=" %2i " % column)
print() # Go down to the next line

# Print line separator; a portion for each column
print(end=" +--")
for column in range(1, MAX + 1):
    print(end="----") # Print portion of line
print() # Go down to the next line
# Print table contents
for row in range(1, MAX + 1): # 1 <= row <= MAX, table has MAX rows
    print(end="%2i | " % row) # Print heading for this row.
    for column in range(1, MAX + 1): # Table has 10 columns.
        product = row*column; # Compute product
        print(end="%3i " % product) # Display product
    print() # Move cursor to next row