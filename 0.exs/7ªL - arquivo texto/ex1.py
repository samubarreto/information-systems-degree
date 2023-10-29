def mostrarMaisDe6Notas():
  print('='*50)
  arquivo = open('C:/Users/samub/OneDrive/Área de Trabalho/code/4.facul/renata/0.exs/7ªL - arquivo texto/arqs/notas_estudantes.txt', 'r', encoding='utf-8')
  
  for linha in arquivo:
    if len(linha.split()) - 1 > 6:
      print(linha)
  arquivo.close()

def mostrarNomesEMédias():
  print('='*50)
  arquivo = open('C:/Users/samub/OneDrive/Área de Trabalho/code/4.facul/renata/0.exs/7ªL - arquivo texto/arqs/notas_estudantes.txt', 'r')
  
  for linha in arquivo:
    nome, *notas = linha.split()
    média = sum(list(map(int, notas))) / len(list(map(int, notas)))
    print(f'{nome}: {média:.2f}')
  arquivo.close()

def mostrarNomesNotasMinMax():
  print('='*50)
  arquivo = open('C:/Users/samub/OneDrive/Área de Trabalho/code/4.facul/renata/0.exs/7ªL - arquivo texto/arqs/notas_estudantes.txt', 'r')
  for linha in arquivo:
    nome, *notas = linha.split()
    notas = list(map(int, notas))
    print(f'{nome}: (min: {min(notas)}), (max: {max(notas)})')
  arquivo.close()

if __name__ == '__main__':  
  mostrarMaisDe6Notas()
  mostrarNomesEMédias()
  mostrarNomesNotasMinMax()
