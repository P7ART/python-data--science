from turtle import*
speed(0)
def polygon(side):
    for _ in range(side):
        fd(100)
        lt(360/side)
        
for i in range(6):
    polygon(60)
    polygon(100)
    lt(60)
    
hideturtle()
mainloop()             

    