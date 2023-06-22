from datetime import date

sexo = str(input('Digite [M] para sexo Masculino\nDigite [F] para sexo Feminino\n\nQual seu genero? : '))
sexo = sexo.upper()

if sexo == 'F':
    print('\nVocê não precisa se alistar Moça !\n\n')

else:
    ano_nasc = int(input('\nDigite o seu ANO de Nascimento: '))

    ano_atual = date.today().year
    ano_alistamento = ano_atual - ano_nasc #se alista com 18 anos

    print('\nVoce tem {} anos SOLDADO !\n'.format(ano_alistamento))

    if ano_alistamento < 18: #verifica se o soldado ainda n fez 18 anos e calcula quantos anos falta para o alistamento
        print('Você ainda esta novo para se alistar SOLDADO !\n')

        tempo_passou = 18 - ano_alistamento
        print('Ainda falta {} anos, fique tranquilo SOLDADO !\n\n'.format(tempo_passou))

    elif ano_alistamento == 18:  #verifica se o soldado tem 18 anos, se tiver precisa se alistar
        print('Está na hora do seu Alistamento SOLDADO !')

    elif ano_alistamento > 18: #verifica se o soldado tem mais de 18 anoproxis,se sim ele precisa se alistar e calcula quanto tempo passou do alistamento
        print('Ja passou da hora de você se alistar SOLDADO !\n')

        tempo_passou =  ano_alistamento - 18
        print('Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais proximo !\n\n'.format(tempo_passou))