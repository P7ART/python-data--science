from turtle import*
speed(0)
def polygon(side):
    for _ in range(side,size,color):
        fillcolor(color)
        begin_fill    
        fd(size)
        lt(360/side)
        end_fill()
        
for i in range(6):
    polygon(6,17,"")
    polygon(10)
    lt(60)
    
hideturtle()
mainloop()             

    