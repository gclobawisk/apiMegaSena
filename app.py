from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import CORS
import json

# CRIANDO O APP
app = Flask(__name__)
CORS(app, resources={r"/*": {"crossOrigin": "*"}})
app.config['JSON_AS_ASCII'] = False

def dictResultados():
    # abre o arquivo
    arq = open("resultadosmegasena.txt", encoding="utf-8")
    linhas = arq.readlines()
    todosResultados = {}
    resultado = {}
    # faz a leitura linha a linha e configura o dicionario
    for linha in linhas:
        linha = linha.strip("\n")
        linha = linha.split("\t")
        resultado['nSorteio'] = int(linha[0])
        resultado['dSorteio'] = linha[1]
        resultado['bola1'] = int(linha[2])
        resultado['bola2'] = int(linha[3])
        resultado['bola3'] = int(linha[4])
        resultado['bola4'] = int(linha[5])
        resultado['bola5'] = int(linha[6])
        resultado['bola6'] = int(linha[7])
        todosResultados[int(linha[0])] = resultado
        resultado = {}

    # retornando um dicionário
    return todosResultados


@app.route('/api/resultados', methods=['GET'])
def obterTodos():
    todosResultados = dictResultados()

    # retorna um json do dicionário acima
    return jsonify(todosResultados)


# Consultar por id'
@app.route('/api/resultados/id/<int:id>', methods=['GET'])
def resultadoPorId(id):
    todosResultados = dictResultados()
    for i in todosResultados:
        if i == id:
            return jsonify(todosResultados.get(id))
    if TypeError:
        return ('ID inválido')

# Quantas vezes cada numero se repete
@app.route('/api/totalrepeticoes', methods=['GET'])
def totalRepeticoes():
    todosResultados = dictResultados()
    maisSorteados = {}
    for id, sorteio in todosResultados.items():
        bola1 = int(sorteio['bola1'])
        bola2 = int(sorteio['bola2'])
        bola3 = int(sorteio['bola3'])
        bola4 = int(sorteio['bola4'])
        bola5 = int(sorteio['bola5'])
        bola6 = int(sorteio['bola6'])

        if bola1 not in maisSorteados.keys():
            maisSorteados[bola1] = 1
        else:
            maisSorteados[bola1] += 1

        if bola2 not in maisSorteados.keys():
            maisSorteados[bola2] = 1
        else:
            maisSorteados[bola2] += 1

        if bola3 not in maisSorteados.keys():
            maisSorteados[bola3] = 1
        else:
            maisSorteados[bola3] += 1

        if bola4 not in maisSorteados.keys():
            maisSorteados[bola4] = 1
        else:
            maisSorteados[bola4] += 1

        if bola5 not in maisSorteados.keys():
            maisSorteados[bola5] = 1
        else:
            maisSorteados[bola5] += 1

        if bola6 not in maisSorteados.keys():
            maisSorteados[bola6] = 1
        else:
            maisSorteados[bola6] += 1

    ##Ordenando um dicionario
    return jsonify(maisSorteados)


# Top 6 que mais cgaíram
@app.route('/api/maissorteados', methods=['GET'])
def maisSorteados():
    todosResultados = dictResultados()
    maisSorteados = {}
    resultadosOrdenados = {}

    for id, sorteio in todosResultados.items():
        bola1 = int(sorteio['bola1'])
        bola2 = int(sorteio['bola2'])
        bola3 = int(sorteio['bola3'])
        bola4 = int(sorteio['bola4'])
        bola5 = int(sorteio['bola5'])
        bola6 = int(sorteio['bola6'])

        if bola1 not in maisSorteados.keys():
            maisSorteados[bola1] = 1
        else:
            maisSorteados[bola1] += 1

        if bola2 not in maisSorteados.keys():
            maisSorteados[bola2] = 1
        else:
            maisSorteados[bola2] += 1

        if bola3 not in maisSorteados.keys():
            maisSorteados[bola3] = 1
        else:
            maisSorteados[bola3] += 1

        if bola4 not in maisSorteados.keys():
            maisSorteados[bola4] = 1
        else:
            maisSorteados[bola4] += 1

        if bola5 not in maisSorteados.keys():
            maisSorteados[bola5] = 1
        else:
            maisSorteados[bola5] += 1

        if bola6 not in maisSorteados.keys():
            maisSorteados[bola6] = 1
        else:
            maisSorteados[bola6] += 1

    count = 1
    for i in sorted(maisSorteados, key = maisSorteados.get, reverse=True):
        if count >= 7:
            break
        else:
            resultadosOrdenados[i] = maisSorteados[i]
            count += 1

    return resultadosOrdenados


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True,
            threaded=True, use_reloader=True)