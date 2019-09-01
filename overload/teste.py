# !/usr/bin/env python3


if __name__ == "__main__":
    import fruits
    lote1 = fruits.Caixa(10,"pera")
    lote50 = fruits.Caixa(53,"laranja")
    lote1000 = fruits.Caixa(10,"pera")

    lote51 = lote1 + lote1000
    lote50 = lote50 - fruits.Caixa(10,"laranja")

    print("Pedido > 20 {} ? {}".format(lote51.name,lote51 > fruits.Caixa(20,"pera")))
    print("{} suficientes para entrega <= 10  ? {}".format(lote50.name,lote50 < fruits.Caixa(10,"laranja")))    

    caminhao1 = fruits.Caminhao("caminhao1",100)
    caminhao1.add(lote51)
    caminhao1.add(lote50)

    print("\n{} tem {} caixas de frutas".format(str(caminhao1),len(caminhao1)))
    for caixa in caminhao1:
        print("{}".format(str(caixa)))