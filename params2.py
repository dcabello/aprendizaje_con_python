def print_all(first, second, third):
    print first, second, third
def print_reverse(first, second, third):
    print third, second, first
def print_add(first, second, third):
    print first + second + third
def print_add_reverse(first, second, third):
    print third + second + first

one = "fish"
two = "and"
three = "chips"
print_all(one, two, three)  #fish and chips
print_reverse(one, two, three) #chips and fish
print_all(three, two, one)  #fish and chips - correcto: chips and fish
print_add(one, two, three)  #fishandchips
print_add_reverse(one, two, three)  #chipsandfish
print_all(1, 2, 3)  #1, 2, 3
print_reverse(1, 2, 3)  #3, 2, 1
print_add(1, 2, 3)  #123 - correcto: 6
print_add_reverse(1, 2, 3) #321 - correcto: 6
