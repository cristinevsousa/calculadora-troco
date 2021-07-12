class CalculoTroco:    
    def calculo_entrada(self, p_valor_recebido, p_valor_compra):                              #<-Método que faz o cálculo inicial para obter o total que será a base                                                                                                                                                                              
        total = p_valor_recebido - p_valor_compra                                             #da contagem de notas e moedas necessárias
        return total

    def calculo_caixa(self, p_total_troco, p_valor_recebido, p_valor_compra, p_valores):      #<-Método que faz a contagem de notas e a apresentação das msgs principais
        total = p_total_troco        
        valor_recebido = p_valor_recebido
        valor_compra = p_valor_compra
        valores = p_valores        
        
        msg_compra = "Valor total da compra = R$ %.2f" % (valor_compra)
        msg_recebido = "Valor recebido = R$ %.2f" % (valor_recebido)
        msg_troco_total = "Troco total = R$ %.2f" % (total)

        msg_troco_nota = "%.0f Nota: R$ %.2f"
        msg_troco_notas = "%.0f Notas: R$ %.2f"
        msg_troco_moeda = "%.0f Moeda: R$ %.2f"
        msg_troco_moedas = "%.0f Moedas: R$ %.2f"

        if valor_compra == valor_recebido:                                  #<-Se o valor recebido for o mesmo da compra a msg inicial é apresentada e não haverão cálculos
            print(msg_compra, msg_recebido, msg_troco_total, sep="\n")

        elif valor_compra < valor_recebido:
            print(msg_compra, msg_recebido, msg_troco_total, sep="\n")      #<-A msg inicial é apresentada seguida das quantidades necessárias de cada nota ou moeda existente no caixa
            while True:                                                
                for i in valores:                                           #<-Para cada valor na lista, disponível em caixa, é feita a verificação 
                    if total >= i:                                          #<-Se o total remanescente for igual ou maior que o valor da nota ou moeda em caixa,
                        total -= i                                          #desconta-se o valor da nota armazenada do total,
                        quant =+ 1                                          #adicionando na variável quant a quantidade de notas ou moedas para aquele valor
                        total = round(total, 2)                             #<- Arredondamento com 2 casas após a vírgula garantindo a precisão do cálculo
                        while total >= i:                                   #<- Concatena valores na variável quant, enquanto o valor da lista pode se repetir
                            total -= i                                   
                            quant += 1
                            total = round(total, 2)                      
                        if i > 1:
                            if quant == 1:
                                print(msg_troco_nota % (quant, i))
                            else:
                                print(msg_troco_notas % (quant, i))
                        else:
                            if quant == 1:
                                print(msg_troco_moeda % (quant, i))
                            else:
                                print(msg_troco_moedas % (quant, i))
                if total == 0:                                             #<-A verificação continua até o total atingir 0, encerrando o loop
                    break                                               






