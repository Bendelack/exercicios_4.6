# Escreva um programa que leia o valor final de venda de um automóvel e calcule
# seu preço sem impostos, os valores pagos para cada tipo de imposto e imprima
# os resultados. Considere que, para automóveis populares, o ICMS (Imposto
# sobre Circulação de Mercadorias e Serviços) é de 18%, o IPI (Imposto sobre
# Produtos Industrializados) é de 13%, o PIS (Programa de Integração Social
# ) é de 1, 4%, e a Cofins (Contribuição para o Financiamento da Seguridade
# Social) é de 7, 6%. Todos os impostos são calculados sobre o valor de custo do
# automóvel. Todos os valors devem ser mostrados com 2 (duas) casas decimais.

valor       = float(input())
inicial     = (valor*100)/140
icms        = (18*inicial)/100
ipi         = (13*inicial)/100
pis         = (1.4*inicial)/100
cofins      = (7.6*inicial)/100

print(f'ICMS: {icms:.2f}')
print(f'IPI: {ipi:.2f}')
print(f'PIS: {pis:.2f}')
print(f'Cofins: {cofins:.2f}')
print(f'Valor sem impostos: {inicial:.2f}')