import turtle
import os

class DibujanteTurtle:
    def __init__(self):
        self.pantalla = turtle.Screen()
        self.pantalla.setup(600, 600)
        
        self.t = turtle.Turtle()
        self.t.speed(2)
        self.t.pensize(2)

        self.comandos = {
            'pencolor', 'fillcolor', 'begin_fill', 'end_fill', 'forward',
            'backward', 'right', 'left', 'penup', 'pendown', 'goto',
            'circle', 'done', 'pensize', 'speed', 'color'
        } #comandos utilizados en dibujante.txt
        
        # Colores válidos en dibujante.txt
        self.colores  = {
            'red', 'green', 'blue', 'yellow', 'black', 'white',
            'orange', 'purple', 'pink', 'gray', 'brown', 'cyan'
        }
    
    def ejecutar_instruccion(self, instruccion):
        """Ejecuta una instrucción individual basada en la Práctica 1"""
        try:
            # Limpiar y dividir la instrucción
            instruccion = instruccion.strip()
            if not instruccion or instruccion.startswith('#'):
                return True
                
            # Buscar el primer paréntesis para separar comando de parámetros
            if '(' in instruccion and instruccion.endswith(')'):
                comando = instruccion.split('(')[0].strip()
                parametros = instruccion.split('(')[1].rstrip(')').strip()
            else:
                comando = instruccion
                parametros = ""
            
            comando = comando.lower()
            
            if comando not in self.comandos:
                print(f"WARNING: Comando '{comando}' no reconocido")
                return False
            
            # Ejecutar comandos según la Práctica 1
            if comando == 'pencolor':
                if parametros.replace('"', '').replace("'", "") in self.colores:
                    color = parametros.replace('"', '').replace("'", "")
                    self.t.pencolor(color)
                else:
                    print(f"WARNING: Color '{parametros}' no válido")
                    
            elif comando == 'fillcolor':
                if parametros.replace('"', '').replace("'", "") in self.colores:
                    color = parametros.replace('"', '').replace("'", "")
                    self.t.fillcolor(color)
                else:
                    print(f"WARNING: Color '{parametros}' no válido")
                    
            elif comando == 'begin_fill':
                self.t.begin_fill()
                
            elif comando == 'end_fill':
                self.t.end_fill()
                
            elif comando == 'forward':
                if parametros.isdigit():
                    self.t.forward(int(parametros))
                else:
                    print("WARNING: 'forward' requiere un número")
                    
            elif comando == 'backward':
                if parametros.isdigit():
                    self.t.backward(int(parametros))
                else:
                    print("WARNING: 'backward' requiere un número")
                    
            elif comando == 'right':
                if parametros.isdigit():
                    self.t.right(int(parametros))
                else:
                    print("WARNING: 'right' requiere un número")
                    
            elif comando == 'left':
                if parametros.isdigit():
                    self.t.left(int(parametros))
                else:
                    print("WARNING: 'left' requiere un número")
                    
            elif comando == 'penup':
                self.t.penup()
                
            elif comando == 'pendown':
                self.t.pendown()
                
            elif comando == 'goto':
                if ',' in parametros:
                    x, y = parametros.split(',')
                    x = x.strip().lstrip('-')
                    y = y.strip().lstrip('-')
                    if x.isdigit() and y.isdigit():
                        # Recuperar signo negativo si existe
                        partes_orig = parametros.split(',')
                        x_val = int(partes_orig[0].strip())
                        y_val = int(partes_orig[1].strip())
                        self.t.goto(x_val, y_val)
                    else:
                        print("WARNING: 'goto' requiere dos números (x,y)")
                else:
                    print("WARNING: 'goto' requiere formato 'x,y'")
                    
            elif comando == 'circle':
                if parametros.isdigit():
                    self.t.circle(int(parametros))
                else:
                    print("WARNING: 'circle' requiere un número")
                    
            elif comando == 'pensize':
                if parametros.isdigit():
                    self.t.pensize(int(parametros))
                else:
                    print("WARNING: 'pensize' requiere un número")
                    
            elif comando == 'speed':
                if parametros.isdigit():
                    self.t.speed(int(parametros))
                else:
                    print("WARNING: 'speed' requiere un número")
                    
            elif comando == 'done':
                print("Ejecución completada")
                
            return True
            
        except Exception as e:
            print(f"ERROR ejecutando '{instruccion}': {str(e)}")
            return False
    
    def cargar_y_ejecutar_archivo(self, nombre_archivo):
        """Carga y ejecuta las instrucciones de un archivo"""
        if not os.path.exists(nombre_archivo):
            print(f"ERROR: El archivo '{nombre_archivo}' no existe")
            return
        
        print(f"Cargando instrucciones desde: {nombre_archivo}")
        print("=" * 50)
        
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        instrucciones_ejecutadas = 0
        instrucciones_fallidas = 0
        
        for numero_linea, linea in enumerate(lineas, 1):
            linea = linea.strip()
            if linea and not linea.startswith('#'):  # Ignorar líneas vacías y comentarios
                print(f"Línea {numero_linea}: {linea}")
                if self.ejecutar_instruccion(linea):
                    instrucciones_ejecutadas += 1
                else:
                    instrucciones_fallidas += 1
        
        print("=" * 50)
        print(f"Resumen de ejecución:")
        print(f"Instrucciones ejecutadas correctamente: {instrucciones_ejecutadas}")
        print(f"Instrucciones con advertencias: {instrucciones_fallidas}")
        
        # Al finalizar, mostrar el mensaje de done
        print("Ejecución completada - Presiona en la ventana para salir")
    
    def mantener_abierto(self):
        """Mantiene la ventana abierta"""
        self.pantalla.exitonclick()

def main():
    dibujante = DibujanteTurtle()
    
    # Cargar y ejecutar el archivo de instrucciones
    archivo_instrucciones = "dibujante.txt"
    dibujante.cargar_y_ejecutar_archivo(archivo_instrucciones)
    
    # Mantener la ventana abierta
    dibujante.mantener_abierto()

if __name__ == "__main__":
    main()