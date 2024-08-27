secret_word = 'perfume'
palavra_acertada = ''
num_tentativa = 0

while True:
    print(f'{10*'*'} Palavra Secreta {10*'*'}')

    letra_digit = input('Digite uma letra: ').lower()

    num_tentativa += 1

    if len(letra_digit) > 1:
        print('Digite apenas uma letra')
    
    if letra_digit in secret_word:
        palavra_acertada += letra_digit

    palavra_formada = ''

    for letra in secret_word:
        if letra in palavra_acertada:
            palavra_formada += letra

        else: 
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == secret_word:
        print('Parabens voce acertou!')
        print(f'número de tentativas: {num_tentativa}')
        break
