# 2- Faça um programa que calcula a média de temperatura de uma semana.

t = 0 #acumulador (temperaturas)
c = 1 #contador (dia)

while c <= 7:
    td = int(input(f'Digite a temperatura em celcius no {c}º dia: ')) #recebe temperatura do dia
    c += 1
    t += td #soma a temperatura com a do dia anterior

med = t / 7 #tira a media da temperatura da semana

print (f'{med:.1f}')