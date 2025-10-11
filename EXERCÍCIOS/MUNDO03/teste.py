nome = str(input()).strip()
sobrenome = str(input()).strip()
idade = int(input())

nome_completo = nome + " " + sobrenome

if idade < 12:
    print(f'A categoria do atleta {nome_completo} é a infantil.')
elif idade >= 12 and idade <= 17:
        print(f'A categoria do atleta {nome_completo} é a juvenil.')
elif idade >= 18 and idade <= 35:
      print(f'A categoria do atleta {nome_completo} é a adulta.')
else:
      print(f'A categoria do atleta {nome_completo} é a master.')