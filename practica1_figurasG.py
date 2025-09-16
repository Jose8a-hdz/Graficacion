import turtle
t = turtle.Turtle()
t.pencolor("green") #color del lapiz
t.fillcolor("blue") #color de relleno
t.begin_fill() #comienza a rellenar la figura
t.forward(100) #avanzar la cantidad de espacios
t.right(90) #gira 90 grados a la derecha
t.forward(100)
t.right(90) #gira 90 grados a la derecha
t.forward(100)
t.right(90) #gira 90 grados a la derecha
t.forward(100)
t.end_fill() #termina de rellenar la figura

t.pencolor("blue") #cambia el color del lapiz a rojo
t.penup() #levanta el lapiz
t.goto(100,60) #se mueve a la posicion (100,50)
t.pendown() #baja el lapiz
t.fillcolor("red") #cambia el color de relleno a rojo
t.begin_fill() #comienza a rellenar la figura
t.circle(50) #dibuja un circulo de radio 50
t.end_fill() #termina de rellenar la figura

t.pencolor("red") #cambia el color del lapiz a verde
t.penup() #levanta el lapiz
t.fillcolor("green") #cambia el color de relleno a verde
t.begin_fill() #comienza a rellenar la figura
t.goto(-150,-50) #se mueve a la posicion (-50,-50)
t.pendown() #baja el lapiz
t.right(120) #gira 120 grados a la derecha
t.forward(100) #avanza 100 espacios
t.right(120) #gira 120 grados a la derecha  
t.forward(100) #avanza 100 espacios
t.right(120) #gira 120 grados a la derecha
t.forward(100) #avanza 100 espacios
t.end_fill() #termina de rellenar la figura

t.pencolor("purple") #cambia el color del lapiz a morado
t.penup() #levanta el lapiz
t.goto(-150,100) #se mueve a la posicion (-150,100)
t.pendown() #baja el lapiz
t.right(90) #gira 90 grados a la derecha
t.forward(100) #avanza 100 espacios
turtle.done() #termina el programa