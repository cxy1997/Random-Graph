from Tkinter import *
from random import *
n = 100
p = 0.01

def DFS(k):
    global cnt
    global Map
    global visited
    global tmp
    cnt += 1
    visited[k] = cnt
    tmp.append(k)
    for i in range(n):
        if Map[k][i] and visited[i] == -1:
            DFS(i)
root = Tk()
root.title("Random Graph illustrator")
root.geometry('800x800')
canvas = Canvas(root, height = 800, width = 800, bg = 'white')
canvas.pack()
var = DoubleVar()
def display(k):
    global cnt
    global Map
    global visited
    global tmp
    p=var.get()
    Map = []
    edges = 0
    for i in range(n):
        Map.append([False]*n)
        for j in range(i):
            Map[i][j] = Map[j][i] = (random() < p)
            if Map[i][j]:
                edges += 1
    visited = [-1] * n
    division = []
    tmp = []
    cnt = -1
    for i in range(n):
        if visited[i] == -1:
            if tmp != []:
                division.append(tmp)
            tmp = []
            DFS(i)
    division.append(tmp)
    number = len(division)
    size = -1
    for i in division:
        if len(i) > size:
            size = len(i)
    print "Number of strongly connected components:", number
    print "Largest size of strongly connected components:", size
    print "Total number of edges:", edges
    canvas.delete("all")
    for i in range(10):
        for j in range(10):
            canvas.create_oval(30+70*i-2,30+70*j-2,30+70*i+2,30+70*j+2,fill='black')
    for i in range(n):
        for j in range(i):
            if Map[i][j]:
                canvas.create_line(30+70*(i/10), 30+70*(i%10), 30+70*(j/10), 30+70*(j%10))
                canvas.create_text(300, 710, text="Number of strongly connected components: %d"%number)
                canvas.create_text(300, 735, text="Largest size of strongly connected components: %d"%size)
                canvas.create_text(300, 760, text="Total number of edges: %d"%edges)

scale = Scale(root, variable = var, label='p', from_=0.5, to=0.001, resolution=0.001, length=700, command=display)
scale.place(x=650,y=30)

root.mainloop()
