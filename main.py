import re

#FUNÇÃO PARA EXPANDIR O INCLUDE
def expandir(linha, novoArquivo):
  biblioteca = ""
  if ("#include" in linha):
    index = linha.find("<") 
    if (index != -1):
      biblioteca = linha[index + 1:len(linha.strip()) - 1]
    index = linha.find("\"")
    if (index != -1):
      biblioteca = linha[index + 1:len(linha.strip()) - 1]

    pre_processador(biblioteca, novoArquivo)

#FUNÇÃO QUE SIMULA O PRÉ-PROCESSADOR
def pre_processador(arquivo_c,ArquivoFinal): #aquivo inicial e arquivo reescrito
  with open(arquivo_c,'r') as file: #abrindo o arquivo e atribuindo-o à variável 'file'
    arquivo = file.readlines() #'arquivo' receberá cada linha dentro de 'file'
    file.close() #fechando o arquivo 'file'

  lista_arquivo=[] #criando uma lista para atribui-la as mudanças que faremos ao arquivo recebido

  #FOR PARA TIRAR QUEBRA DE LINHAS
  for linha in arquivo: #for que passa em todas as linhas de "arquivo"
    if '\n' in linha: #se a linha for igual a \n 
      linha = linha.replace('\n','') #mudamos a linha para vazio
    lista_arquivo.append(linha) #inserindo a linha alterada na nova lista "lista_arquivo"

  nova_lista=[] #nova lista auxiliar
  
  #FOR PARA TIRAR COMENTÁRIOS 
  for linha in lista_arquivo: #for que passa em todas as linhas de "lista_arquivo"
    if ' ' in linha:
      linha=re.sub("^\s+",'', linha) #regex (expressão regular) pega os espaços iniciais (até acabarem) e os substitui por vazio 
    if '#include' in linha:
      lista_arquivo = expandir(linha,ArquivoFinal) #expandindo as bibliotecas em include 
      linha = ''
    if '//' in linha: #se a linha tiver //
      linha = '' #linha receberá vazio
    nova_lista.append(linha) #inserindo a linha alterada na nova lista "nova_lista"

  arquivo_processado=''.join(nova_lista) 

  #CRIANDO NOVO ARQUIVO EM C PARA O CÓDIGO JÁ PROCESSADO
  for linha in arquivo_processado:
    ArquivoFinal.write(linha)
    
  return arquivo_processado #retornando o arquivo processado para leitura

#MAIN
arquivo_c = 'exemplo.c' #'arquivo_c' recebe o arquivo para ser pré-processado
ArquivoFinal = open('arquivoProcessado.c','w') #CRIANDO UM ARQUIVO
arquivo_processado = pre_processador(arquivo_c,ArquivoFinal) #variável "arquivo_processado" receberá o retorno da função "pre_processador"



#IMPRIMINDO O ARQUIVO ANTES DE SER PROCESSADO
with open(arquivo_c,'r') as file:
  read_arquivo_c=file.read()
print(read_arquivo_c) 
print('-------------------------------------------------')
#IMPRIMINDO O ARQUIVO APÓS SER PROCESSADO
print(arquivo_processado)

ArquivoFinal.close() #FECHANDO O ARQUIVO
