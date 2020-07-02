# Compute the value of a block of stock
shares = int( input("shares: ") )
price = float( input("dollars: ") )
price += float( input("eights: ") )/8.0
print( "value", shares * price)