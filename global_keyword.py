# Global keyword

nombre = 'Leandro'

def saludador():
    global nombre
    return 'hola ' + nombre


print(saludador())

