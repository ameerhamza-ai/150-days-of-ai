def test():
    import math
    print(math.pi)
test()
#print(math.pi)  
# Error: 
"""
    Line: print(math.pi) outside function
    Error: NameError — math is not defined

Reason: 'math' was imported INSIDE
the function test() — making it a
LOCAL variable. It only exists within
that function's scope.

Once the function ends, math is gone.
Accessing it outside = NameError.

Fix: Move import math to the top
of the file (global scope).
"""