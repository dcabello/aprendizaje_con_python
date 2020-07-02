def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])
if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
    "database":"master", \
    "uid":"sa", \
    "pwd":"secret" \
    }
def fib(n): 
    print 'n =', n 
    if n > 1: 
        return n * fib(n - 1)
    else: 
        print 'end of the line'
    return 1 
#fib(23)    
print buildConnectionString(myParams)

t = ("a", "b", "mpilgrim", "z", "example")
t
('a', 'b', 'mpilgrim', 'z', 'example')
print t[0]
print t[-1]
print t[1:2], t[2], range(1,8)
print "Today's stock price: %f" % 50.4625 
print "Today's stock price: %.2f" % 50.4625 
print "Change since yesterday: %+.2f" % 1.5
li = {"1":"alfa", "9":"beta", "8":"gamma", "4":"delta"}
print(("%s, %s") % (k, v) for k, v in li)
print buildConnectionString(li)