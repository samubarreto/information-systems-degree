def mostrarMaisDe6Notas():
  
  for linha in arquivo:
    if len(linha.split()) - 1 > 6:
      print(linha)

def mostrarNomesEMédias():
  pass

def mostrarNomesNotasMinMax():
  pass

if __name__ == '__main__':
  
  arquivo = open('C:/Users/samub/OneDrive/Área de Trabalho/code/4.facul/renata/0.exs/7ªL - arquivo texto/arqs/notas_estudantes.txt')
  
  mostrarMaisDe6Notas()
  mostrarNomesEMédias()
  mostrarNomesNotasMinMax()
