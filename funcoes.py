def soma(numero1 , numero2):
    resultado = numero1 + numero2
    return resultado

def sub(numero1 , numero2):
    resultado = numero1 - numero2
    return resultado

def mult(numero1 , numero2):
    resultado = numero1 * numero2
    return resultado

def div(numero1, numero2):
    if numero2 == 0:
        return "Não e possivel dividir por zero"
    resultado = numero1 / numero2
    return resultado