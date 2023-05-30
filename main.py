import re

def pre_processador(arquivo_c): #função para ler o arquivo
  with open(arquivo_c,'r') as file: #abrindo o arquivo e atribuindo-o à variável 'file'
    arquivo = file.readlines() #'arquivo' receberá cada linha dentro de 'file'
    file.close() #fechando o arquivo 'file'

  lista_arquivo=[] #criando uma lista para atribui-la as mudanças que faremos ao arquivo recebido

  #FOR PARA TIRAR QUEBRA DE LINHAS
  for linha in arquivo: #for que passa em todas as linhas de "arquivo"
    if '\n' in linha: #se a linha for igual a \n 
      linha = linha.replace('\n','') #mudamos a linha para \nç
    lista_arquivo.append(linha) #inserindo a linha alterada na nova lista "lista_arquivo"

  nova_lista=[] #nova lista auxiliar
  
  #FOR PARA TIRAR COMENTARIOS 
  for linha in lista_arquivo: #for que passa em todas as linhas de "lista_arquivo"
    if ' ':
      linha=re.sub("^\s+",'', linha) #regex (expressão regular) pega os espaços iniciais (até acabarem) e os substitui por vazio 
    if '#' in linha:
      linha = linha + '\n'
    if '//' in linha: #se a linha tiver //
      linha = '' #linha receberá vazio
    nova_lista.append(linha) #inserindo a linha alterada na nova lista "nova_lista"
    
  arquivo_processado=''.join(nova_lista)

  #CRIANDO NOVO ARQUIVO EM C PARA O CÓDIGO JÁ PROCESSADO
  with open('arquivoProcessado.c','w') as file: 
    for linha in arquivo_processado:
      file.write(linha)
    file.close()
    
  return arquivo_processado #retornando o arquivo processado para leitura

#main
arquivo_c = 'exemplo.c' #'arquivo_c' recebe o arquivo para ser pré-processado
arquivo_processado = pre_processador(arquivo_c) #variável "arquivo_processado" receberá o retorno da função "pre_processador"

#IMPRIMINDO O ARQUIVO ANTES DE SER PROCESSADO
with open(arquivo_c,'r') as file:
  read_arquivo_c=file.read()
print(read_arquivo_c) 
print('-------------------------------------------------')
#IMPRIMINDO O ARQUIVO APÓS SER PROCESSADO
print(arquivo_processado)