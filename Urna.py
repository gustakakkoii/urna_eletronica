from turtle import delay
import pygame
import os

pygame.init()

# Costante
PRETO = (0, 0, 0)
FUNDO = (232, 225, 209)


screen = pygame.display.set_mode((1300, 640), 0)


def pintar_urna():
    # Pintando urna
    color = (253, 253, 253)
    borda = (96, 97, 85)
    fundon = (39, 40, 34)
    justicatext = pygame.image.load('justicaeleitoraltext.png')
    pygame.draw.rect(screen, color, pygame.Rect(70, 70, 650, 500))
    pygame.draw.rect(screen, borda, pygame.Rect(70, 70, 650, 500), 2)
    pygame.draw.rect(screen, fundon, pygame.Rect(800, 124, 429, 474))
    screen.blit(justicatext, (800, 42))

    # Pintando numeros

    # buscando na pasta

    n1 = pygame.image.load('botoes/1.png')
    n2 = pygame.image.load('botoes/2.png')
    n3 = pygame.image.load('botoes/3.png')
    n4 = pygame.image.load('botoes/4.png')
    n5 = pygame.image.load('botoes/5.png')
    n6 = pygame.image.load('botoes/6.png')
    n7 = pygame.image.load('botoes/7.png')
    n8 = pygame.image.load('botoes/8.png')
    n9 = pygame.image.load('botoes/9.png')
    n0 = pygame.image.load('botoes/0.png')
    corrige = pygame.image.load('botoes/corrige.png')
    branco = pygame.image.load('botoes/branco.png')
    confirma = pygame.image.load('botoes/confirma.png')

    # definindo posição

    screen.blit(n1, (871, 192))
    screen.blit(n2, (976, 192))
    screen.blit(n3, (1081, 192))
    screen.blit(n4, (871, 268))
    screen.blit(n5, (976, 268))
    screen.blit(n6, (1081, 268))
    screen.blit(n7, (871, 344))
    screen.blit(n8, (976, 344))
    screen.blit(n9, (1081, 344))
    screen.blit(n0, (976, 420))
    screen.blit(corrige, (966, 510))
    screen.blit(branco, (852, 510))
    screen.blit(confirma, (1081, 484))


def marcarbotoes(pos):
    # ao passar em cima do botão 1
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(871, 192, 78, 45), 2, 5)
    # ao passar em cima do botão 2
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(976, 192, 78, 45), 2, 5)
    # ao passar em cima do botão 3
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(1081, 192, 78, 45), 2, 5)
    # ao passar em cima do botão 4
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(871, 268, 78, 45), 2, 5)
    # ao passar em cima do botão 5
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(976, 268, 78, 45), 2, 5)
    # ao passar em cima do botão 6
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(1081, 268, 78, 45), 2, 5)
    # ao passar em cima do botão 7
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(871, 344, 78, 45), 2, 5)
    # ao passar em cima do botão 8
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(976, 344, 78, 45), 2, 5)
    # ao passar em cima do botão 9
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(1081, 344, 78, 45), 2, 5)
    # ao passar em cima do botão 0
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 420) and (pos[1] < (420+45))):
        pygame.draw.rect(screen, (25, 26, 24, 1),
                         pygame.Rect(976, 420, 78, 45), 2, 5)
    # ao passar em cima do botão branco
    if ((pos[0] > 852) and (pos[0] < (852+97)) and (pos[1] > 510) and (pos[1] < (510+45))):
        pygame.draw.rect(screen, (181, 181, 181, 1),
                         pygame.Rect(852, 510, 97, 45), 2, 5)
    # ao passar em cima do botão corrije
    if ((pos[0] > 976) and (pos[0] < (976+97)) and (pos[1] > 510) and (pos[1] < (510+45))):
        pygame.draw.rect(screen, (126, 65, 31, 1),
                         pygame.Rect(966, 510, 97, 45), 2, 5)
    # ao passar em cima do botão confirma
    if ((pos[0] > 1081) and (pos[0] < (1081+97)) and (pos[1] > 484) and (pos[1] < (484+71))):
        pygame.draw.rect(screen, (9, 90, 33, 1),
                         pygame.Rect(1081, 484, 97, 71), 2, 5)


def escrevervoto(pos):
    # evento click do botão 1
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '1'
    # evento click do botão 2
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '2'
    # evento click do botão 3
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 192) and (pos[1] < (192+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '3'
    # evento click do botão 4
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '4'
    # evento click do botão 5
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '5'
    # evento click do botão 6
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 268) and (pos[1] < (268+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '6'
    # evento click do botão 7
    if ((pos[0] > 871) and (pos[0] < (871+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '7'
    # evento click do botão 8
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '8'
    # evento click do botão 9
    if ((pos[0] > 1081) and (pos[0] < (1081+77.73)) and (pos[1] > 344) and (pos[1] < (344+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '9'
    # evento click do botão 0
    if ((pos[0] > 976) and (pos[0] < (976+77.73)) and (pos[1] > 420) and (pos[1] < (420+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return '0'
    return ''


def tela(screen, voto, candidatos):
    if (voto == ''):
        justicaimg = pygame.image.load('justicaeleitoral.png')
        screen.blit(justicaimg, (219, 126))

    if (voto == 'negado'):
        font = pygame.font.Font('arial.ttf', 50)
        text = font.render(('DEFINA SEU VOTO'), True, PRETO)
        candidato = font.render('NEGADO', True, PRETO)

        screen.blit((text), (169, 292))
        screen.blit(candidato, (287, 114))

    if (voto != '' and voto != 'negado'):
        x = 0
        font = pygame.font.Font('arial.ttf', 50)
        text = font.render(('Voto: '+voto), True, PRETO)
        candidato = font.render('CANDIDATO(A)', True, PRETO)

        screen.blit((text), (121, 243))
        screen.blit(candidato, (217, 114))

        for arquivo in candidatos:
            with open('./candidatos/'+arquivo, 'r', encoding='utf-8') as candidatoss:
                textarquivo = candidatoss.readlines()
            if(len(textarquivo)!=0):
                if ((voto + '\n') == textarquivo[0]):
                    font = pygame.font.Font('arial.ttf', 30)
                    nome = font.render(
                        ('Candidato: ' + textarquivo[1]), True, PRETO)
                    x += 1
                    screen.blit(nome, (121, 300))

        if (x == 0):
            if (voto != 'BRANCO'):
                font = pygame.font.Font('arial.ttf', 30)
                nome = font.render(('Voto nulo'), True, PRETO)

                screen.blit(nome, (121, 300))


def botoes(pos, voto, candidatos):
    if ((pos[0] > 1081) and (pos[0] < (1081+97)) and (pos[1] > 484) and (pos[1] < (484+71))):
        if ((voto == 'negado') or (voto == '')):
            pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
            pygame.mixer.music.play(1)
            return 'negado'

        else:
            if ((voto) == "BRANCO"):
                with open('votos.txt', 'a', encoding='utf-8') as votos:
                    votos.write("BRANCO\n")

            else:
                x = 0
                for arquivo in candidatos:
                    with open('./candidatos/'+arquivo, 'r', encoding='utf-8') as candidatoss:
                        textarquivo = candidatoss.readlines()
                    if(len(textarquivo)!=0):
                        if ((voto + '\n') == textarquivo[0]):
                            with open('votos.txt', 'a', encoding='utf-8') as votos:
                                votos.write(voto+'\n')
                                x += 1
                if (x == 0):
                    with open('votos.txt', 'a', encoding='utf-8') as votos:
                        votos.write("nulo\n")

            pygame.mixer.music.load('botoes/sons/concluido.wav')
            pygame.mixer.music.play(1)
            pygame.time.delay(1000)
            exit()

    # limpa o voto
    if ((pos[0] > 966) and (pos[0] < (966+97)) and (pos[1] > 510) and (pos[1] < (510+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return ''

    # define voto branco
    if ((pos[0] > 852) and (pos[0] < (852+97)) and (pos[1] > 510) and (pos[1] < (510+45))):
        pygame.mixer.music.load('botoes/sons/apertarbotao.wav')
        pygame.mixer.music.play(1)
        return 'BRANCO'
    else:
        if (voto == 'BRANCO'):
            voto = ''
            return voto + escrevervoto(pos)
        if (voto == 'negado'):
            voto = ''
            return voto + escrevervoto(pos)
        else:
            return voto + escrevervoto(pos)


if __name__ == '__main__':
    pos = (0, 0)
    voto = ''

    dir = 'candidatos'
    candidatos = []
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            candidatos.append(path)

    while True:

        pygame.display.update()
        pygame.display.set_caption('Urna Eletrônica')

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                voto = botoes(pos, voto, candidatos)

        screen.fill(FUNDO)
        pintar_urna()
        mouse = pygame. mouse. get_pos()
        marcarbotoes(mouse)
        tela(screen, voto, candidatos)
        pygame.display.flip()
