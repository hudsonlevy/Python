m = int(input('Metros: '))
if m % 54 != 0:
    latas = int(m / 54) + 1
else:
    latas = m / 54
valor = latas * 80

print('%d lata(s) a um custo de %.2f' %(latas, valor))
