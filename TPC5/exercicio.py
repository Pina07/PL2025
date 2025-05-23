import json
import ply.lex as lex


with open('stock.json') as stock:
    db = json.load(stock)
    
    
    
moedas = {
    "2e": 2.00,
    "1e": 1.00,
    "50c": 0.50,
    "20c": 0.20,
    "10c": 0.10,
    "5c": 0.05
}

saldo = 0


def strToInt(str):
    valor = None
    if(str in moedas):
        valor = moedas[str]
    else:
        print("A moeda é inválida")
        valor = 0
    return valor


def intToStr(x):
    inteiro, decimal = str("{:.2f}".format(x)).split('.')
    return f"{inteiro}e{decimal}c"


tokens = (
    'LISTAR',
	'MOEDA',
	'DINHEIRO',
	'SELECIONAR',
	'VIRGULA',
	'PONTO',
	'NOME_PRODUTO',
    'SAIR'
)



t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_DINHEIRO = r'\d{1,2}[ec]'
t_SELECIONAR = r'SELECIONAR'
t_VIRGULA = r','
t_PONTO = r'\.'
t_NOME_PRODUTO = r'A\d{2}'
t_SAIR = r'SAIR'


t_ignore = ' \t\n'


def t_error(t):
    print("Caractere ilegal: ", t.value[0])
    t.lexer.skip(1)
    

lexer = lex.lex()


ligada = True


while ligada:
    command = input('>> ')
    lexer.input(command)
    tok = lexer.token()
    if(tok.type == "MOEDA"):
        for tok in lexer:
            if(tok.type == "DINHEIRO"):
                saldo += strToInt(tok.value)
        print("Saldo = " + intToStr(saldo))
    elif(tok.type == "LISTAR"):
        print (f"{'cod':<10} | {'nome':<20} | {'quantidade':<10} | {'preço':<10}")
        print("-" * 60 + "\n")
        for item in db:
            print(f"{item['cod']:<10} | {item['nome']:<20} | {item['quant']:<10} | {item['preco']:<10.2f}")
    elif(tok.type == "SELECIONAR"):
        tok = lexer.token()
        for item in db:
            if item['cod'] == tok.value:
                if (saldo >= item['preco']):
                    if (item['quant'] > 0):
                        item["quant"] -= 1
                        troco = saldo - item['preco']
                        print(f"Retire o produto: {item['nome']}")
                        if(troco >= 0):
                            print(f"Retire o troco: {intToStr(troco)}")
                        troco = 0
                        saldo = 0
                    else:
                        print("Não há stock do produto escolhido")
                else:
                    print(f"Saldo insuficiente \nSaldo: {saldo}\nPreço do produto: {item['preco']}")
    elif tok.type == "SAIR":
        ligada = False
    else:
        print("Comando inválido")
        
    
with open('stock.json', 'w') as stock:
    json.dump(db, stock, indent=4)