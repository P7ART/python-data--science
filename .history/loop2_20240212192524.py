#while loop
from turtle import*
speed('fast')

s = 0
while s < 250:
    fd(50 + s )
    lt(60)
    write (s)
    s += 5
  
  
    hideturtle()
    mainloop()
    