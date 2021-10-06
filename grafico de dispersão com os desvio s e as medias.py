#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math #importa as bibliotecas
import numpy as np
def desvio_padrao(list): #define a função que calcula o desvio padrão
    media = [] 
    x = [] 
    media = [(sum(list)/len(list))] #calcula a media da lista que vc escolhe
    for l in list:
        x.append((l-media[0])**2) #subtrai a media e eleva ao quadrado todos os valores na lista que você joga nessa função
    for l in x:
        y = (math.sqrt(sum(x)/len(list)-1)) #variável que tira a média dos valores na lista x, e tira a raíz quadrada do resultado
    return y #retorna o valor de y que é o desvio padrão final da lista que você jogou na função
def desvio_media(rio):
    np_array = Q #transforma os dados em array
    dias = 0 #variavel para os dias que percorrem as linhas do array
    ano = [x+1 for x in range(1997,2009)] # cria um array que contém todos os anos de 1998 até 2009
    mediagraf = [] #lista que armazenas as medias que serão plotadas
    lista1 = [] #lista que armazena as vazões do rio para calcular o desvio 
    dpf = [] #lista que armazena os desvios que serão plotados
    for j in range(len(ano)): #for que divide as vazões em anos e jogas as vazões do rio na lista1 um ano por vez, para calcular o desvio e a media de cada ano
        for i in range(365):
            lista1.append(np_array[i+dias][rio])
        list = lista1 #define os valores na lista1 como a variável da função que calcula o devio padrão
        dp = desvio_padrao(list) #calcula os desvios padrões das vazões do rio
        dpf.append(dp) #adiciona o desvio daquele ano na lista dos desvio que serão plotados
        mediagraf.append(sum(lista1)/len(lista1)) #calcula a media das vazões do rio naquele ano e joga o resultado na lista das medias que serão plotadas
        if ano[j]%4==0: # verifica se o ano é bissexto
            dias += 366 # atualiza o valor dos dias se o ano for bissexto
        else:
            dias += 365 # atualiza o valor dos dias se o ano for normal
        dp = 0 #zera a variavel desvio daquele parqa poder calcular o desvio do ano seguinte
    
    #inicia a plotagem das medias e desvios
    trace3 = go.Scatter(x = ['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'], y = dpf, mode = 'markers+lines', name = 'Desvios Padrões anuais', marker_color= 'blue') #define os desvios padrões anuais em y e a cor da linha 
    trace2 = go.Scatter(x = ['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'], y = mediagraf, mode = 'markers+lines', name = 'Medias anuais das vazões', marker_color= 'grey') #define as médias anuais como sendo y e a cor da linha 
    # define o título do gráfico e os títulos dos eixos
    layout = go.Layout(title='Desvios padrões anuais e médias anuais',
                       yaxis={'title':'Vazão (m³/s)'},
                       xaxis={'title': 'Anos (1997-2009)'})
    data = [trace3, trace2] #define as variáveis que serão plotadas
    desvio = go.Figure(data=data, layout=layout)
    return desvio
desvio_media(0).show()

