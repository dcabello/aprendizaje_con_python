import math, random
print("Valor Absoluto de -23.53 : ", abs(-23.53))
print("23 elevado a la 9a potencia : ", pow(23, 9))
print("155.472 redondeado en 2 decimales  : ", round(155.472, 2))
print("155.472 redondeado en 1 decimal    : ", round(155.472, 1))
print("155.472 redondeado en 0 decimal    : ", round(155.472, 0))
print("155.472 redondeado en -1 decimal   : ", round(155.472, -1))
print("155.472 redondeado en -2 decimales : ", round(155.472, -2))
print("math.fmod (-14, 5) : ", math.fmod(-14, 5))
print("(-14%5) : ", (-14%5))
i = 0
while(i < 4):
    x = random.randrange(0, 20)
    print("x : ", x)
    i = i + 1    