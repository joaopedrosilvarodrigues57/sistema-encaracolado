#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math  #importa as bibliotecas
import numpy as np
def vazoes_extremas(rio): #define a função do dash
    np_array = Q #transforma a tabela de dados em array
    lista = [] #cria uma lista para armazenar as vazões do rio
    va = 0  # cria a variavel das vazoões acima da média
    vb = 0  #cria a variaveldas vazões abaixo da média
    for i in range(4383): #for que seleciona as vazões do rio
        lista.append(np_array[i][rio])  #jogas as vazões do rio na lista
    list = lista #define a lista como variavel da função que calcula o desvio padrão
    dp = desvio_padrao(list) #calcula o desvio padrão com a função definida no bloco anterio
    media = sum(lista)/len(lista) #calcula a media das vazões
    for i in range(4383): # laço de repetição para percorrer as colunas e separar os dias das vazões acima e abaixo da média.
        if np_array[i][rio] > media + dp*2: # condicional para separar os dias de vazão acima da média mais duas vezes o desvio padrão.
            va += 1    # armazena a quantidade de dias que a vazão foi maior que média.
        elif np_array[i][rio] < media - dp: # condicional para separar os dias de vazão abaixo da média.
            vb +=1      # armazena a quantidade de dias que a vazão foi menor que média menos  o desvio padrão.
    x = (len(Q) - (va+vb)) # subtrai a soma entre va e vb do total de vazões par saber quantas vazões não estão acima ou abaixo da média com o desvio padrão
    
    #o gráfico de pizza irá mostrar o total de vazões acima e abaixo da média levando em conta o desvio padrão e também as vazõews que não ficaram nem acima e nem abaixo em cinza
    labels = ['Acima da média anual','Abaixo da média anual', 'Vazões Restantes']  # subtítulos do gráfico.
    values = [va, vb, x]   # armazena na variável values a lista dos valores obtidos.
    night_colors = ['blue', 'purple', 'grey'] # altera as cores do gráfico de pizza de acordo com os parâmetros.
    vazoes_ext = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=night_colors)]) # armazena na variável fig a configuração do gráfico.
    vazoes_ext.update_layout(                                                         # atualiza o layout do gráfico.
        title_text="Dias em que a vazão foi menor ou maior que a média anual", # adiciona título.
        annotations=[dict(text='DVMMMA', x=0.5, y=0.5, font_size=20, showarrow=False)]) # adiciona a sigla DVMMMA no meio do gráfico. 
    vazoes_ext.update_traces(hole=.4, hoverinfo="label+percent+name")  # configura o tamanho da circunferência no interior do gráfico.
    return vazoes_ext
vazoes_extremas(0).show()


            

