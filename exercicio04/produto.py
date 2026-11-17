def produto(valor,valor_desconto):

    desconto =  valor_desconto * valor / 100
    valor_com_desconto = valor - desconto
    
    return valor_com_desconto