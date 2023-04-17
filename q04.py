valor       = float(input())
icms        = (18*valor)/100
ipi         = (13*valor)/100
pis         = (1.4*valor)/100
cofins      = (7.6*valor)/100
semimpostos = valor-icms-ipi-pis-cofins

print(f'{icms:.2f}')
print(f'{ipi:.2f}')
print(f'{pis:.2f}')
print(f'{cofins:.2f}')
print(f'{semimpostos:.2f}')