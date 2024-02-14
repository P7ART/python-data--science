from turtle import*
speed(0)
def polygon(side):
    fillcolor(color)
    begin_fill()
    for _ in range(side,size,color):
        
        fd(size)
        lt(360/side)
    end_fill()
        
for i in range(6):
    polygon(6,17,"purple")
    polygon(10,12,"red")
    lt(60)
    
hideturtle()
mainloop()             

    