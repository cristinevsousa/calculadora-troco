from CalculoTroco import CalculoTroco

valores_caixa = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]        #<-Lista dos valores em caixa
valor_compra = float(input("Valor da compra: R$ "))                             #<-Parâmetros dos valores iniciais para o cálculo do troco total
valor_recebido = float(input("Valor recebido: R$ "))

print("*" * 30, "{:^30}".format("Calculadora de Troco"), "*" * 30, sep="\n")    

calculo_troco = CalculoTroco()
total_troco = calculo_troco.calculo_entrada(valor_recebido, valor_compra)
calculo_troco = calculo_troco.calculo_caixa(total_troco, valor_recebido, valor_compra, valores_caixa)
    
print("*" * 30, "{:^30}".format("Fim do Cálculo"), "*" * 30, sep="\n")
