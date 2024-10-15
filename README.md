# StocksPortfolio

`StocksPortfolio` é uma classe em Python que representa um portfólio de ações, permitindo a realização de operações matemáticas entre diferentes portfólios, além de fornecer funcionalidades úteis para gerenciar e inspecionar um portfólio de forma intuitiva.

## Funcionalidades

- **Soma de Portfólios (`__add__`)**: Permite somar dois portfólios diferentes, combinando os valores das ações comuns e adicionando novas ações.
- **Multiplicação por Escalar (`__mul__`)**: Permite multiplicar os valores de todas as ações de um portfólio por um número inteiro ou float.
- **Acesso a Ações (`__getitem__`)**: Acesso direto a uma ação específica através do seu ticker (ex.: `portfolio['AAPL']`). Se a ação não estiver presente, retorna `0`.
- **Tamanho do Portfólio (`__len__`)**: Retorna o número de diferentes ações no portfólio.
- **Valor Absoluto do Portfólio (`__abs__`)**: Retorna a soma dos valores de todas as ações no portfólio.
- **Representação Amigável (`__repr__`)**: Representação clara do portfólio quando impresso.
- **Avaliação Booleana (`__bool__`)**: Retorna `True` se houver pelo menos uma ação com valor positivo no portfólio, ou `False` se o portfólio estiver vazio ou com todas as ações zeradas.

## Exemplo de Uso

```python
# Importando a classe StocksPortfolio
from stocks_portfolio import StocksPortfolio

# Criando dois portfólios
portfolio1 = StocksPortfolio({
    'ASDF': 10,
    'GHJL': 5
})

portfolio2 = StocksPortfolio({
    'ASDF': 10,
    'ZXCV': 5
})

# Somando os portfólios
combined_portfolio = portfolio1 + portfolio2
print('Combined Portfolio:', combined_portfolio)

# Multiplicando o portfólio por um escalar
scaled_portfolio = portfolio1 * 3
print('Scaled Portfolio:', scaled_portfolio)

# Acessando uma ação específica
apple_stock = portfolio1['ASDF']
print('ASDF stock:', apple_stock)

# Obtendo o tamanho do portfólio
num_stocks = len(portfolio1)
print('Number of stocks in portfolio1:', num_stocks)

# Obtendo o valor absoluto do portfólio
total_value = abs(portfolio1)
print('Total value of portfolio1:', total_value)

# Verificando se o portfólio contém ações válidas
if portfolio1:
    print("Portfolio1 contains stocks with value.")
else:
    print("Portfolio1 is empty or all stocks have zero value.")
```
## Como Funciona
### Soma de Portfólios (__add__)
Este método permite somar dois portfólios. Caso um ticker esteja presente em ambos, seus valores serão somados. Se um ticker estiver presente apenas em um dos portfólios, ele será adicionado ao portfólio resultante.

### Multiplicação por Escalar (__mul__)
O portfólio pode ser multiplicado por um número (inteiro ou float), o que resulta em uma multiplicação proporcional dos valores de todas as ações.

### Acesso a Ações (__getitem__)
Permite acessar diretamente o valor de uma ação específica através de seu ticker. Se o ticker não existir, o método retorna 0.

### Tamanho do Portfólio (__len__)
Retorna o número de tickers diferentes presentes no portfólio.

### Valor Absoluto do Portfólio (__abs__)
Calcula a soma de todos os valores das ações no portfólio, representando o valor total do portfólio.

### Avaliação Booleana (__bool__)
Retorna True se houver ao menos uma ação com valor positivo. Caso contrário, retorna False.

## Requisitos
Python 3.7 ou superior.
## Instalação
1. Clone o repositório:

   ```bash
   git clone https://github.com/botlorien/stocks-portfolio-example.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd stocks-portfolio-example
   ```
3. Execução:
   ```bash
   python stocks_portfolio.py
   ```


## Erros Possíveis
ValueError: Lançado quando uma operação incorreta é tentada, como tentar adicionar um objeto que não seja um StocksPortfolio ou multiplicar por um valor que não seja numérico.
## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE.md](https://github.com/botlorien/Bot_ml_images_classify/blob/main/LICENSE) para mais detalhes.
