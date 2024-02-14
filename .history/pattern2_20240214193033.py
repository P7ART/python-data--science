from turtle import*
speed(0)
def polygon(side):
    for _ in range(side,size):
        fd(100)
        lt(360/side)
        
for i in range(6):
    polygon(6)
    polygon(10)
    lt(60)
    
hideturtle()
mainloop()             

    