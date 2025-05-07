# funcion para verificar 
def num_primos (n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0:
            return False      
    return True
# listra para obtener numeros primos 
primos = [n for n in range(1, 1001) if num_primos(n)]
#mostrar lista 
print(primos)
   

