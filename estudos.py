from pickle import TRUE


pode_parcelar = TRUE
valor = int(input ('informar valor'))
limite = 2000

if (pode_parcelar or valor < 3000) and limite >= valor:
    print('vou comprar')
else:
    print('Ainda não')