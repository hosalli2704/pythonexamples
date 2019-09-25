import mymodule
import sys
print(sys.path)
# sys.path.append(r'c:\')
print(mymodule.msg)
print(mymodule.sub(10, 20))

import mymodule as m
print(m.msg)
##############################
from mymodule import msg , sub
print(msg)
print(sub(100,50))

##################################
import project.net.mymodule as y
print(y.msg)
print(y.sub(2, 4))

