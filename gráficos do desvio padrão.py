#!/usr/bin/env python
# coding: utf-8

# In[14]:


# importação das bibliotecas que serão utilizadas

import pandas as pd
import plotly.offline as py
import datetime
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
py.init_notebook_mode(connected = True)

Q = pd.read_csv(r'C:\Users\raque\OneDrive\Área de Trabalho\base de dados do joao\MGB-IPH_DischargeData_AmazonBasin.txt', delimiter="\s+",engine='python',header=None)
ti='1998-01-01'  # atribui a variavel ti o a data inicial da pesquisa.
tf='2009-12-31'  # atribui a variavel tf o a data final da pesquisa.
date = pd.date_range(start=ti, end=tf, freq='D') # Cria uma lista com as datas.
Q['date'] = date # Nomeia a coluna das datas.
Q.set_index('date', inplace=True) # adiciona a lista de datas nos dados das vazões.


# In[26]:


import math
np_array= Q.to_numpy() # transforma o DataFrame em um array
lista1= [] # cria uma lista para armazenar as vazões que serão usadas no cálculo do desvio padrão 
lista12 = [] # cria uma lista para armazenar as vazões que serão plotadas
media2 = [] # cria uma lista para armazenar as médias anuais que serão usadas no cálculo do desvio padrão
mediagraf = [] #cria uma lista para as médias anuais que serão plotadas
mmf2 = [] #define uma lista para poder subtrair a média de todas as vazões anuais  
mmf22 = []#define uma lista para elevar os valores da lista mmf ao quadrado
somatoriammf22 = [] #define uma lista para aramazenar a soma de todos os valores da lista mmf2
dp2 = [] #define uma lista para dividir o resultado da lista anterior pelo total de vazões anuais 
dpf2 = [] #define uma lista para tirar a raiz dos resultados da lista anterior
dpff2 = [] #cria uma lista que armazena o resultado final do desvio padrão e multiplica por 2 para separar as vazões acima e abaixo da média depois
dpfff = [] #cria uma lista que armazena os desvio padrões que serão plotados 
va = 0 #variável que irá receber a quantidade de dias em que as vazões ficaram acima da média
vb = 0 #variável que irá receber a quantidade de dias em que as vazões ficaram abaixo da média 


dias = 0 # inicializa a variável que recebe o valor de dias
ano = [x+1 for x in range(1997,2009)] # cria um array que contém todos os anos de 1998 até 2009

   
for j in range(12): # for para cada ano a ser analizado
    for i in range(365): # for que percorre todos os dias em um ano de um rio da matriz
        lista1.append(np_array[i+dias][0]) #acrescenta as vazões anuais na lista1
        lista12.append(np_array[i+dias][0]) #acrescenta as vazões anuais na lista12 para serem plotadas depois
    media2 = [sum(lista1)/len(lista1)] # calcula a média anual das vazões na lista1
    mediagraf.append(media2[0])#acrescenta a média anual na lista das médias anuais que serão plotadas
    for l in lista1: #for que percorre a lista1
        mmf2.append(l - media2[0]) #subtrai o valor da média anual de todos os valores na lista1 como parte do cálculo do desvio padrão e joga o resultado na lista mmf2
    for l in mmf2: #for que percorre a lista mmf2
        mmf22.append(l**2) #eleva os valoreds na lista mmf2 e acrescenta o resultado na lista mmf22
    somatoriammf22 =[sum(mmf22)] #lista que recebe a soma de todos os valores na lista mmf22
    dp2 = [float(i)/len(lista1)-1 for i in somatoriammf22] #divide todos os valores na lista anterior e joga o resultado na lista dp2
    for n in dp2: #for que percorre a lista dp2
        if n > 0: #analisa se os valores  na lista dp2 são maiores que 0
            dpf2 = [math.sqrt(dp2[0])] #se forem maiores que 0, o loop retira a raiz quadrada desses valores e joga o resultado na lista dpf2 
        if n < 0:#analisa se o valor na lista dp2 são menores que 0
            dpf2.append(n)#se forem menores acrescenta esse valor sem tirar a raiz pois não existe raiz de negativos no reais
    for m in dpf2: #for que percorre a lista dpf2
        dpff2.append(m*2) #acrescenta o resultado final do desvio padrão na lista dpf2 na lista dpff2 e multiplica o desvio padrão por 2 para separar as médias depois
        dpfff.append(m)# acrescenta o resultado final do desvio padrão anual na lista dpfff para plotar esse resultados no final
    for i in range(365): #for que percorre a matriz com os dados
        if np_array[i][0] < media2[0]-dpff2[0]: #analisa se a vazão do rio é menor que a média anual vezes dois
            vb += 1 #se for menor, soma mais um ao valor inicial da variável vb, que é 0 inicialmente
        elif np_array[i][0]> media2[0]+dpff2[0]: #analisa se a vazão do rio é maior que a média anual vezes dois
            va += 1 #se a média for maior, soma mais um ao valor inicial da variável vb, que é 0 inicialmente
    if ano[j]%4==0: # verifica se o ano é bissexto
        dias += 366 # atualiza o valor dos dias se o ano for bissexto
    else:
        dias += 365 # atualiza o valor dos dias se o ano for normal
    
    media2 = [] #limpa a lista para seguir para o próximo ano
    mmf2 = [] #limpa a lista para seguir para o próximo ano
    mmf22 = [] #limpa a lista para seguir para o próximo ano
    somatoriammf22 = [] #limpa a lista para seguir para o próximo ano
    dp2 = [] #limpa a lista para seguir para o próximo ano
    dpf2 = [] #limpa a lista para seguir para o próximo ano
    dpff2 = [] #limpa a lista para seguir para o próximo ano

x = (4383 - (va+vb))

print(va,vb)
print(x)
#as variáveis va e vb irão indicar o número de dias em que as vazões dos rios ficaram abaixo ou acima da média anual levando em conta o desvio padrão anual



# In[27]:


trace3 = go.Scatter(x = ano, y = dpfff, mode = 'markers+lines', name = 'Desvios Padrões anuais', marker_color= 'blue') #define os desvios padrões anuais em y e a cor da linha 

trace2 = go.Scatter(x = ano, y = mediagraf, mode = 'markers+lines', name = 'Medias anuais das vazões', marker_color= 'grey') #define as médias anuais como sendo y e a cor da linha 

# define o título do gráfico e os títulos dos eixos

layout = go.Layout(title='Desvios padrões anuais e médias anuais',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title': 'Anos (1997-2009)'})

data = [trace3, trace2] #define as variáveis que serão plotadas

fig = go.Figure(data=data, layout=layout)

py.iplot(fig) #plota os gráficos


# In[30]:


labels = ['Acima da média anual','Abaixo da média anual', 'Vazões Restantes']  # subtítulos do gráfico.
values = [va, vb, x]   # armazena na variável values a lista dos valores obtidos.

 

night_colors = ['blue', 'purple', 'grey'] # altera as cores do gráfico de pizza de acordo com os parâmetros.

 

fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=night_colors)]) # armazena na variável fig a configuração do gráfico.
fig.update_layout(                                                         # atualiza o layout do gráfico.
    title_text="Dias em que a vazão foi menor ou maior que a média anual", # adiciona título.
    annotations=[dict(text='DVMMMA', x=0.5, y=0.5, font_size=20, showarrow=False)]) # adiciona a sigla DVMMMA no meio do gráfico. 
fig.update_traces(hole=.4, hoverinfo="label+percent+name")  # configura o tamanho da circunferência no interior do gráfico.
fig.show()  # inicia a plotagem.

        


# In[31]:


print(va,vb)
print(dpfff)
print(mediagraf)


# In[ ]:




