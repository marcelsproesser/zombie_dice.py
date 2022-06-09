# Curso: Big Data e Inteligência Analítica
# Estudante: Marcel Sproesser Mathias

from random import shuffle, choice
import random
import time
from collections import namedtuple

print("Bem vinda/o/e ao Zombie Dice")
print("O zombie dice é um jogo de dados, "
      "cada jogador é um zumbi e a cada rodada joga três dados,"
      " podendo tirar: TIRO, CEREBRO, PASSO.")
print("Para vencer o jogo você precisa comer 13 cérebros (tirar cérebro 13 vezes no dado)")
print("Se você tomar 3 tiros em uma mesma rodada (tirar tiro 3 vezes no dado), "
      "você morre e os cérebros comidos na rodada não são contabilizados.")
print("Se você tirar passos, significa que a vítima fugiu.")
print("Bom jogo!")

comecar_jogo = 0
while comecar_jogo != "1":
    comecar_jogo = input("Para iniciar o jogo digite 1: ")

# Criando os dados com tupla


def dado_funcao():
    dados_disponiveis = namedtuple("Dado", ['cor', 'lados'])
    dado_verde = dados_disponiveis("Verde: ", ["CÉREBRO", "PASSO", "CÉREBRO", "TIRO", "CÉREBRO", "PASSO"])
    dado_amarelo = dados_disponiveis("Amarelo: ", ["TIRO", "PASSO", "CÉREBRO", "TIRO", "PASSO", "CÉREBRO"])
    dado_vermelho = dados_disponiveis("Vermelho: ", ["TIRO", "PASSO", "TIRO", "CÉREBRO", "PASSO", "TIRO"])

    # Colocando os dados no tubo
    tubo = []
    for i in range(6):
        tubo.append(dado_verde)
    for i in range(4):
        tubo.append(dado_amarelo)
    for i in range(3):
        tubo.append(dado_vermelho)

    # Mistura os dados e retorna com eles embaralhados
    shuffle(tubo)
    return tubo


def lista_jogadores():
    global nome
    jogadores = []
    # Função while para não permitir que inicie o jogo com menos de dois jogadores
    quantidade_jogadores = int(input("Quantas pessoas vão jogar? "))
    while quantidade_jogadores < 2:
        print("Não é permitido menos de 2 jogadores")
        quantidade_jogadores = int(input("Quantas pessoas vão jogar? "))

    for jogador in range(0, quantidade_jogadores):
        nome = input(f"Insira o nome do jogador " + str(jogador+1) + ": ")
        # dict para armazenando o nome como chave e o score como valor
        jogador = {'nome': nome, 'score': 0}
        # Adiciona os jogadores a lista
        jogadores.append(jogador)
    shuffle(jogadores)
    # imprime lista de jogadores
    print("Lista de jogadores")
    contador = 1
    for jogador in jogadores:
        print(f"{contador}. jogador {jogador}")

    return jogadores
# Inicio do jogo


print("Começando o jogo")

# Função para os turnos


def turno(jogador):
    global lado_sorteado, dado
    print(f"Jogador {jogador['nome']}! Sua vez de jogar!")

    tubo = dado_funcao()
    score_turno = {'Cérebros': 0, 'Tiros': 0}
    dados_em_jogo = []

    # Adicionei essa função para não rodar o jogo todo de uma vez
    rolar_dado = 0
    while rolar_dado != "1":
        rolar_dado = input("Para jogar digite 1: ")

    while True:
        while len(dados_em_jogo) < 3:
            # Usando pop para tirar os dados usados do tubo
            dados_em_jogo.append(tubo.pop())

        contador = 1
        for dado in reversed(dados_em_jogo):
            print(f"Jogando o {contador} dado!")
            contador += 1

            cor = dado.cor
            shuffle(dado.lados)
            lado_sorteado = choice(dado.lados)

            time.sleep(0.5)
            print(f"O dado sorteado foi o {cor}")
            time.sleep(0.5)
            print(f"O lado sorteado foi o {lado_sorteado}")

            if lado_sorteado == 'CÉREBRO':
                score_turno['Cérebros'] = score_turno['Cérebros'] + 1
                tubo.append(dados_em_jogo.pop(dados_em_jogo.index(dado)))
            elif lado_sorteado == 'TIRO':
                score_turno['Tiros'] = score_turno['Tiros'] + 1
                tubo.append(dados_em_jogo.pop(dados_em_jogo.index(dado)))

        # Mistura os dados após devolve-los
        shuffle(tubo)
        print("Pontuação")
        time.sleep(1)
        print(f"Cérebros: {score_turno['Cérebros']}")
        time.sleep(1)
        print(f"Tiros: {score_turno['Tiros']}")

        if score_turno['Tiros'] < 3:
            continuar_jogo = input("Você deseja continuar jogando? (S/N) ").strip().upper()
            if continuar_jogo == "N":
                time.sleep(0.3)
                print(f"Seu score nesse turno foi: {score_turno['Cérebros']} Cérebros")
                jogador['score'] += score_turno['Cérebros']
                break
        else:
            time.sleep(0.5)
            print("Você tomou três tiros ou mais! Por isso, você não pontuou")
            print("Tente na próxima")
            break

def pontuacao(jogadores):
    print("Score total")
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['score']} Cérebros comidos")


jogadores = lista_jogadores()

jogo_terminado = False
while not jogo_terminado:
    for jogador in jogadores:
        turno(jogador)
        if jogador['score'] >= 13:
            vencedor = jogador['nome']
            jogo_terminado = True

        if not jogo_terminado:
            pontuacao(jogadores)
        else:
            print("Jogo terminado!!")
            print(f"Parabéns {vencedor}, você ganhou o jogo!")
            exit()