from turtle import delay
import pygame
import os

pygame.init()

# Costante
PRETO = (0, 0, 0)
FUNDO = (255, 255, 255)
CORGRAFICO = (138, 216, 146, 1)


screen = pygame.display.set_mode((1300, 640), 0)


#função que conta quantos votos tem
def totalvotos():
    with open('votos.txt', 'r', encoding='utf-8') as votos:
        votos = votos.readlines()
    return len(votos)


#função que zera os votos
def zerarvotos(pos):
    #tem que clicar no botão de zerar votos
    if (pos[0] > 1036) and (pos[0] < (1036+233)) and (pos[1] > 25) and (pos[1] < (25+42.58)):
        with open('votos.txt', 'w', encoding='utf-8') as votos:
            votos.write('')


def contarvotos(candidatos):
    #separa os votos
    # v = [total, brancos, nulos, candidatos]
    v = [0, 0, 0]
    l = 3
    with open('votos.txt', 'r', encoding='utf-8') as votos:
        votos = votos.readlines()
        for voto in votos:
            if ((voto) == 'BRANCO\n'):
                v[1] += 1
                v[0] += 1
            else:
                if ((voto) == 'nulo\n'):
                    v[2] += 1
                    v[0] += 1
    #conta os votos de candidato por candidato
    for candidato in candidatos:
        v.append(0)
        with open('candidatos/' + candidato, 'r', encoding='utf-8') as candidatoss:
            textarquivo = candidatoss.readlines()
        if(len(textarquivo)!=0):  
            with open('votos.txt', 'r', encoding='utf-8') as votos:
                votos = votos.readlines()
                for voto in votos:
                    if ((voto) == textarquivo[0]):
                        v[l] += 1
                        v[0] += 1
        l += 1
    # v = [total de votos, votos brancos, votos nulos, votos de n candidatos(pode ser mais de 1)]
    return v

#transforma os votos em porcentagem do total de votos
def calcularporcentagem(votos):
    font = pygame.font.Font('arial.ttf', 30)
    nome = font.render(
            'Total de votos: '+ str(votos[0]), True, PRETO)
    screen.blit(nome, (17, 19))
    total = votos[0]
    tvotos = votos
    del tvotos[0]
    porcentagem = []
    for voto in tvotos:
        porcentagem.append(round(100*(int(voto)/int(total)), 2))

    # porcentagem = [%votos Brancos, %votos nulos, %n quantidade de candidatos]
    return porcentagem

#confere vencedor
def conferevencedor(tvotos, candidatos):
    font = pygame.font.Font('arial.ttf', 30)
    NeB = [tvotos[0], tvotos[0]]
    NeB = max(NeB)
    votos = tvotos
    #desconsidera nulos e brancos
    del votos[0]
    del votos[0]
    #define a maior quantidade de votos (sendo eles não nulos e não brancos)
    votos = max(votos)
    
    v = 0
    #confere se existe mais de um candidato com a mesma quantidade de votos
    for voto in tvotos:
        if voto == votos:
            v += 1

    # em caso de empate
    if (v > 1 or votos==0):
        nome = font.render(
            'Situação atual: Não é possível determinar um vencedor', True, PRETO)
        screen.blit(nome, (17, 53))

    #em caso de vencedor
    else:
        p = 0
        f = 0
        for voto in tvotos:
            if voto == votos:
                f = p
            p += 1
        #escreve o nome do candidato na tela
        with open('candidatos/'+candidatos[f], 'r', encoding='utf-8') as candidatoss:
            textarquivo = candidatoss.readlines()
        if(len(textarquivo)!=0):
            nome = font.render('Situação atual: Vitória de ' +
                                textarquivo[1]+'!', True, PRETO)
            screen.blit(nome, (17, 53))

def desenhargrafico(screen, candidatos):
    font = pygame.font.Font('arial.ttf', 10)
    zerar = pygame.image.load('botoes/zerar.png')
    screen.blit(zerar, (1036, 25))

    c = 0
    votos = contarvotos(candidatos)
    porcentagens = calcularporcentagem(votos)
    conferevencedor(votos, candidatos)

    #define o tamanho das colunas do gráfico de acordo com a quantidade de candidatos
    larguradacoluna = (1099/((len(porcentagens)*2)-1))
    for coluna in porcentagens:
        if (c == 1):
            nome = font.render('Nulos: '+str(coluna)+'%', True, PRETO)
            screen.blit(nome, ((100+(2*c)*larguradacoluna),
                        (625-((coluna/100)*490))))
        else:
            if (c == 0):
                nome = font.render('Brancos: '+str(coluna)+'%', True, PRETO)
                screen.blit(nome, ((100+(2*c)*larguradacoluna),
                            (625-((coluna/100)*490))))
            else:
                #escreve o nome dos candidatos e suas respectivas porcentagens de votos
                with open('candidatos/'+candidatos[(c-2)], 'r', encoding='utf-8') as votos:
                    textarquivo = votos.readlines()
                    if(len(textarquivo)!=0):
                        nome = font.render(
                            textarquivo[1]+': '+str(coluna)+'%', True, PRETO)
                        screen.blit(nome, ((100+(2*c)*larguradacoluna),
                                    (625-((coluna/100)*490))))
        pygame.draw.rect(screen, CORGRAFICO, pygame.Rect(
            100+((2*c)*larguradacoluna), (640-((coluna/100)*490)), larguradacoluna, ((coluna/100)*490)))
        c += 1

#exclui arquivos sem dados de candidatos
def limpa(candidatos):
    for arquivo in candidatos:
        with open('candidatos/'+arquivo, 'r', encoding='utf-8') as candidato:
            textarquivo = candidato.readlines()
        if(len(textarquivo)==0):
            os.remove('candidatos/'+arquivo)

if __name__ == '__main__':
    dir = 'candidatos'
    candidatos = []
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            candidatos.append(path)

    limpa(candidatos)

    candidatos = []
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            candidatos.append(path)
    while True:

        pygame.display.update()
        pygame.display.set_caption('Contar votos')

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                zerarvotos(pos)


        screen.fill(FUNDO)

        totaldevotos = totalvotos()
        if (totaldevotos != 0 and len(candidatos)!=0):
            desenhargrafico(screen, candidatos)

        else:
            font = pygame.font.Font('arial.ttf', 50)
            vencedor = font.render('SEM NENHUM VOTO', True, PRETO)
            screen.blit(vencedor, (401, 292))

        pygame.display.flip()
