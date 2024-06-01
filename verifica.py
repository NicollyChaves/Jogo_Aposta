def aposta(saldo, valor_aposta, aleatorio):
    if saldo > 0:
        print("Saldo disponivél R$:",saldo)
        total_sub =  saldo - valor_aposta
        print("Aposta realizada. Saldo restante: $", total_sub)
        if aleatorio == "Vitória":
            total_som = (valor_aposta * 2) + saldo
            print("Parabéns! Você ganhou a aposta. Seu saldo ficou: R$", total_som) 
        else:
            print("Que pena! Você perdeu a aposta.")