import random
import verifica
import time

#---main---

saldo = 1000
valor_aposta = 0
resultado = ""


print("Bem-vindo ao jogo de aposta esportiva!")

valor_aposta = int(input("Digite um valor: "))

for i in range(3):
    print("Imprima Jogo em andamento ", i)
    time.sleep(1)

resultado = ["Vitória", "Derrota"]
aleatorio = random.choice(resultado)

verifica.aposta(saldo, valor_aposta, aleatorio)
   