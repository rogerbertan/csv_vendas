import pandas as pd

tabela = pd.read_csv('vendasMercado.csv')

tabela = tabela[(tabela['Forma de Pagamento'] == 'Cash')]

tabela = tabela.drop(columns=['ID', 'Tipo de Cliente', 'Genero', 'Linha de Produto', 'Preco', 'Quantidade', 'Impostos', 'Data', 'Forma de Pagamento'])

tabela['Cidade'].unique()

tabelaYangon = tabela[(tabela['Cidade'] == 'Yangon')]
tabelaNaypyitaw = tabela[(tabela['Cidade'] == 'Naypyitaw')]
tabelaMandalay = tabela[(tabela['Cidade'] == 'Mandalay')]

tabelaYangon = tabelaYangon.drop(columns=['Cidade'])
tabelaNaypyitaw = tabelaNaypyitaw.drop(columns=['Cidade'])
tabelaMandalay = tabelaMandalay.drop(columns=['Cidade'])

tabelaYangon = tabelaYangon.reset_index(drop=True)
tabelaNaypyitaw = tabelaNaypyitaw.reset_index(drop=True)
tabelaMandalay = tabelaMandalay.reset_index(drop=True)

tabelaYangon.to_csv('tabelaYangon.csv')
