def en_to_br():
  palavra = input(f'''\n{"="*60}\n
Inglês para Português

Palavra -> ''')
  if palavra in tradEN:
    print(f'{palavra} = {tradEN.get(palavra)}')
  else:
    print(f'Palavra {palavra} não encontrada.')

def br_to_en():
  palavra = input(f'''\n{"="*60}\n
Português para inglês

Palavra -> ''')
  if palavra in tradBR:
    print(f'{palavra} = {tradBR.get(palavra)}')
  else:
    print(f'Palavra {palavra} não encontrada.')

def quit():
  print(f'\n{"="*60}')
  print('\nFechando o Tradutor.\n')
  print(f'{"="*60}')
  exit()

while True:
  tradBR = {'arroz': 'rice',
          'feijão': 'bean',
          'alho': 'garlic'}
  
  tradEN = {'rice': 'arroz',
          'bean': 'feijão',
          'garlic': 'alho'}
  
  op = input(f'''\n{"="*60}\nEscolha uma opção:
1. Português para Inglês
2. Inglês para Português
3. Sair
Opção -> ''')
  
  br_to_en() if op == '1' else en_to_br() if op == '2' else quit() if op =='3' else None
  