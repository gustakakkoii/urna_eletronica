# importando bibliotecas
import datetime
from operator import le
import pygame
import os

pygame.init()

# Cores
PRETO = (0, 0, 0)
FUNDO = (255, 255, 255)
CORGRAFICO = (138, 216, 146, 1)


#definindo tela
screen = pygame.display.set_mode((1000, 640), 0)


# função que gera a caixa de criar candidato
def escrevecandidatos(screen, candidatos, nome, numero):
    font = pygame.font.Font('arial.ttf', 20)
    p = 0
    #fundo
    pygame.draw.rect(screen, (25, 26, 24, 1),pygame.Rect(502, 50, 430, 247))

    # botoes criar/excluir
    criar = pygame.image.load('botoes/criar.png')
    excluir = pygame.image.load('botoes/excluir.png')
    screen.blit(criar, (542, 250))
    screen.blit(excluir, (736, 250))

    # campos para escrever o nome/numero
    pygame.draw.rect(screen, (255, 255, 255),pygame.Rect(542, 92, 349, 37))
    pygame.draw.rect(screen, (255, 255, 255),pygame.Rect(542, 171, 349, 37))

    #definindo os campos para faciliar para o usuário
    if nome == '':
        textnome = font.render('Nome:', True, PRETO)
        screen.blit(textnome, (555, 99))
    else:
        n1 = font.render(nome, True, PRETO)
        screen.blit(n1, (555, 99))


    if numero == '':
        textnumero = font.render("Número: ", True, PRETO)
        screen.blit(textnumero, (555, 178))
    else:
        n2 = font.render(numero, True, PRETO)
        screen.blit(n2, (555, 178))

    #abrindo e lendo o arquivo de candidato por candidato
    for candidato in candidatos:
        with open('candidatos/'+candidato, 'r', encoding='utf-8') as c:
            textcandidato = c.readlines()

        #se o arquivo tiver dados de candidatos ele escrevera o numero e o nome na tela
        if(len(textcandidato)!=0):
            n1 = textcandidato[0]
            n1 = n1[:-1]
            n2 = font.render(n1+' - '+textcandidato[1], True, PRETO)
            screen.blit(n2, (15, (p*20)+50))
            p+=1

#função que analiza os eventos do teclado e guarda numeros
def escrevenumero(e, pos):
    #tem que clicar no campo de numero
    if pos[0]>542 and pos[0]<542+349 and pos[1]>171 and pos[1]<171+37:
        if e.unicode == '0':
            return '0'
        if e.unicode == '1':
            return '1'
        if e.unicode == '2':
            return '2'
        if e.unicode == '3':
            return '3'
        if e.unicode == '4':
            return '4'
        if e.unicode == '5':
            return '5'
        if e.unicode == '6':
            return '6'
        if e.unicode == '7':
            return '7'
        if e.unicode == '8':
            return '8'
        if e.unicode == '9':
            return '9'
        if e.unicode == '\x08':
            return '\x08'
    return ''

#função que analiza os eventos do teclado e guarda letras
def escreverletras(e, pos):
    #tem que clicar no campo de nome primeiro
    if pos[0]>542 and pos[0]<542+349 and pos[1]>92 and pos[1]<92+37:
        if e.unicode == ' ':
            return ' '

        if e.unicode == 'ã':
            return 'ã' 
        if e.unicode == 'á':
            return 'á' 
        if e.unicode == 'à':
            return 'à' 
        if e.unicode == 'â':
            return 'â'
        if e.unicode == 'é':
            return 'é' 
        if e.unicode == 'è':
            return 'è' 
        if e.unicode == 'ê':
            return 'ê'
        if e.unicode == 'í':
            return 'í' 
        if e.unicode == 'ì':
            return 'ì' 
        if e.unicode == 'î':
            return 'î'
        if e.unicode == 'õ':
            return 'õ' 
        if e.unicode == 'ó':
            return 'ó' 
        if e.unicode == 'ò':
            return 'ò' 
        if e.unicode == 'ô':
            return 'ô'
        if e.unicode == 'ú':
            return 'ú' 
        if e.unicode == 'ù':
            return 'ù' 
        if e.unicode == 'û':
            return 'û'

        if e.unicode == 'a':
            return 'a'
        if e.unicode == 'b':
            return 'b'
        if e.unicode == 'c':
            return 'c'
        if e.unicode == 'ç':
            return 'ç'
        if e.unicode == 'd':
            return 'd'
        if e.unicode == 'e':
            return 'e'
        if e.unicode == 'f':
            return 'f'
        if e.unicode == 'g':
            return 'g'
        if e.unicode == 'h':
            return 'h'
        if e.unicode == 'i':
            return 'i'
        if e.unicode == 'j':
            return 'j'
        if e.unicode == 'k':
            return 'k'
        if e.unicode == 'l':
            return 'l'
        if e.unicode == 'm':
            return 'm'
        if e.unicode == 'n':
            return 'n'
        if e.unicode == 'o':
            return 'o'
        if e.unicode == 'p':
            return 'p'
        if e.unicode == 'q':
            return 'q'
        if e.unicode == 'r':
            return 'r'
        if e.unicode == 's':
            return 's'
        if e.unicode == 't':
            return 't'
        if e.unicode == 'u':
            return 'u'
        if e.unicode == 'v':
            return 'v'
        if e.unicode == 'w':
            return 'w'
        if e.unicode == 'x':
            return 'x'
        if e.unicode == 'y':
            return 'y'
        if e.unicode == 'z':
            return 'z'



        if e.unicode == 'A':
            return 'A'
        if e.unicode == 'B':
            return 'B'
        if e.unicode == 'C':
            return 'C'
        if e.unicode == 'Ç':
            return 'Ç'
        if e.unicode == 'D':
            return 'D'
        if e.unicode == 'E':
            return 'E'
        if e.unicode == 'F':
            return 'F'
        if e.unicode == 'G':
            return 'G'
        if e.unicode == 'H':
            return 'H'
        if e.unicode == 'I':
            return 'I'
        if e.unicode == 'J':
            return 'J'
        if e.unicode == 'K':
            return 'K'
        if e.unicode == 'L':
            return 'L'
        if e.unicode == 'M':
            return 'M'
        if e.unicode == 'N':
            return 'N'
        if e.unicode == 'O':
            return 'O'
        if e.unicode == 'P':
            return 'P'
        if e.unicode == 'Q':
            return 'Q'
        if e.unicode == 'R':
            return 'R'
        if e.unicode == 'S':
            return 'S'
        if e.unicode == 'T':
            return 'T'
        if e.unicode == 'U':
            return 'U'
        if e.unicode == 'V':
            return 'V'
        if e.unicode == 'W':
            return 'W'
        if e.unicode == 'X':
            return 'X'
        if e.unicode == 'Y':
            return 'Y'
        if e.unicode == 'Z':
            return 'Z'

        if e.unicode == '\x08':
            return '\x08'
    return ''


#função que cria o candidato
def criarcandidato(pos, candidatos, numero, nome):
    #tem que clicar no botaõ de criar
    if pos[0]>542 and pos[0]<542+154.5 and pos[1]>250 and pos[1]<250+34:
        x=0
        #os valores não podem ser nulos
        if numero!='' and nome!='':
            print(len(candidatos))
            #se existir candidatos:
            if len(candidatos)!=0:
                for candidato in candidatos:
                    with open('candidatos/'+candidato, 'r', encoding='utf-8') as c:
                        textcandidato=c.readlines()
                        #se o arquivo tiver dados:
                        if len(textcandidato)!=0:
                            #se ja exisitir um candidato com aquele numero, ele atualizara o mesmo arquivo
                            if textcandidato[0] == numero+'\n':
                                with open('candidatos/'+candidato, 'w', encoding='utf-8') as c:
                                    c.write(numero+'\n'+nome)
                                x+=1
            
            #se não existir candidato nenhum ele cria um novo:
            if x==0 or len(candidatos)==0:
                with open('candidatos/'+gerarnome()+'.txt', 'w', encoding='utf-8') as c:
                    c.write(numero+'\n'+nome)

#função que exclui o candidato
def excluircandidato(pos, candidatos, numero, nome):
    #tem que clicar no botão de excluir
    if pos[0]>736 and pos[0]<736+154.5 and pos[1]>250 and pos[1]<250+34:
        x=0
        #ele exclui a partir d numero então o numero precisa ser informado
        if numero!='':
            for candidato in candidatos:
                with open('candidatos/'+candidato, 'r', encoding='utf-8') as c:
                    textcandidato=c.readlines()
                    if(len(textcandidato)!=0):
                        if textcandidato[0] == numero+'\n':
                            with open('candidatos/'+candidato, 'w', encoding='utf-8') as c:
                                #limpa o arquivo
                                c.write('')
                            x+=1

#funão que sempre gerará um nome sempre diferente do outro
def gerarnome():
    #guarda data e hora atual
    arquivo = str(datetime.datetime.now())
    print (arquivo)
    arquivo = arquivo.split(':')
    a=[]
    b=[]
    for texto in arquivo:
        a.append(texto.split('.'))
    for x in a:
        for y in x:
            b.append(y)
    a = ''
    for x in b:
        a = a+x
    a = a.split(' ')


    b=[]
    for x in a:
        b.append(x.split('-'))

    a = ''
    for x in b:
        for y in x:
            a = a+y
    return a

                

if __name__ == '__main__':
    numero = ''
    nome = ''
    pos=[0, 0]
    while True:
        dir = 'candidatos'
        candidatos = []
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                candidatos.append(path)


        pygame.display.update()
        pygame.display.set_caption('Definir candidatos')

        screen.fill(FUNDO)
        escrevecandidatos(screen, candidatos, nome, numero)

        pygame.display.flip()

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if(escrevenumero(e, pos)=='\x08'):
                    numero = numero[:-1]
                else:
                    numero = numero + escrevenumero(e, pos)

                if(escreverletras(e, pos)=='\x08'):
                    nome = nome[:-1]
                else:
                    nome = nome + escreverletras(e, pos)
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                criarcandidato(pos, candidatos, numero, nome)
                excluircandidato(pos, candidatos, numero, nome)

