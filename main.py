import string as st
import numpy as np
import pyfiglet

print(pyfiglet.figlet_format("GERADOR DE SENHAS"))

while True:   
    letras = st.ascii_letters
    numeros = st.digits
    caracteres = st.punctuation
    soma = letras+numeros+caracteres
    senha = np.random.choice(list(soma),10)
    print('SUA SENHA É:')
    print('=================')
    print(''.join(senha))
    print('=================')

    reset = input('DESEJA GERAR OUTRA SENHA? 1 PARA SIM - 2 PARA NAO:')
    if reset == '2':
        break
        



