def water_state(temperature):
    if temperature > 100:
        print "Steam ", temperature, "C" 
    elif temperature < 0:
        print "Ice", temperature, "C" 
    else:
        print "Liquid", temperature, "C" 
water_state(23)
water_state(125)
water_state(-20)
water_state(33)
