from turtle import *
# speed(-1)


n = int(input("Number of edge :"))
for edge in range (3, n+1):
    
    for i in range (edge):
        forward(100)
        left(360/edge)
    for colors in ['blue', 'red']:
        color(colors)
mainloop()
