import sys
print("este es un mensaje de error---", file=sys.stderr)
print("Esto es stdout")
print("Esto también es stdout---", file=sys.stdout)