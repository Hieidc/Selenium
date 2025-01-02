import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log',filemode='a', format='%(levelname)s - %(message)s - %(asctime)s') # Setor o nivel

try:        
    email = input('Digite seu e-mail')
    senha = int(input('Digite sua senha bancaria'))
    if senha == 1234:
        print('Login efetuado com sucesso')
        logging.info(f'{email} entrou em sua conta')
except ValueError as erro:
    print('Digite apenas numeros')
    logging.info(erro)