#C:/Users/samub/arquivo-teste.txt

if __name__ == '__main__':
  arquivo = input('Digite o diretório do arquivo de texto qualquer -> ')
  
  try:
    with open(arquivo, 'r', encoding='utf-8') as file:
      num = 0
      for linha in file:
        num += 1
      print(f'\n·O arquivo tem {num} linhas')
  except:
    print(f'\n·Arquivo não encontrado.')
