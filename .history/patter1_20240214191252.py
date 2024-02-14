from turtle import*
speed("fastest")

def hexagon():
    for _ in range(5):
        fd(100)
        lt(60)
        
def pentagon():
    for _ in range(5):
        fd(50)
        lt(72)
        
        
#testing fuction 
for i in range(6):
    fd(100)
    hexagon()               
    pentagon()
        
         