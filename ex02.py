qtde_internet = int(input('Informe o consumo de internet: '))
qtde_local = int(input('Informe o consumo de ligações locais: '))
qtde_interurbano = int(input('Informe o consumo de ligações interurbanas: '))
qtde_torpedo = int(input('Informe o consumo de torpedos: '))

valor_internet = qtde_internet * 0.5
valor_local = qtde_local * 0.35
valor_interurbano = qtde_interurbano * 0.6
valor_torpedo = qtde_torpedo * 0.2

total_sem_desconto = valor_internet + valor_local + valor_interurbano + valor_torpedo
print(f'Total da fatura sem desconto: R$ {total_sem_desconto:.2f}')

if qtde_internet > 50:
    desconto_internet = valor_internet * 0.05
else:
    desconto_internet = 0

if qtde_local > 200:
    desconto_local = valor_local * 0.1
else:
    desconto_local = 0

if qtde_interurbano > 150:
    desconto_interurbano = valor_interurbano * 0.1
else:
    desconto_interurbano = 0

if qtde_torpedo > 50:
    desconto_torpedo = valor_torpedo * 0.2
else:
    desconto_torpedo = 0

if desconto_internet > desconto_local and\
        desconto_internet > desconto_interurbano and\
        desconto_internet > desconto_torpedo:
    print("O desconto será sobre o serviço internet")
    print(f"O valor do desconto será de R$ {desconto_internet:.2f}")
    total_com_desconto = total_sem_desconto - desconto_internet
    print(f"O total com desconto será R$ {total_com_desconto:.2f}")
elif desconto_local > desconto_internet and\
        desconto_local > desconto_interurbano and\
        desconto_local > desconto_torpedo:
    print("O desconto será sobre o serviço ligação local")
    print(f"O valor do desconto será de R$ {desconto_local:.2f}")
    total_com_desconto = total_sem_desconto - desconto_local
    print(f"O total com desconto será R$ {total_com_desconto:.2f}")
elif desconto_interurbano > desconto_internet and\
        desconto_interurbano > desconto_local and\
        desconto_interurbano > desconto_torpedo:
    print("O desconto será sobre o serviço ligação interurbana")
    print(f"O valor do desconto será de R$ {desconto_interurbano:.2f}")
    total_com_desconto = total_sem_desconto - desconto_interurbano
    print(f"O total com desconto será R$ {total_com_desconto:.2f}")
elif desconto_torpedo > desconto_internet and\
        desconto_torpedo > desconto_local and\
        desconto_torpedo > desconto_interurbano:
    print("O desconto será sobre o serviço torpedo")
    print(f"O valor do desconto será de R$ {desconto_torpedo:.2f}")
    total_com_desconto = total_sem_desconto - desconto_torpedo
    print(f"O total com desconto será R$ {total_com_desconto:.2f}")
else:
    print('Não haverá desconto')
