#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ciclo_anual_graph(rio):
    [Rows, Columns] = Q.shape   # Extrair número de fila (dias) e colunas (rios) da base de dados
    Nmonth = 12                 # Número de mêses num ano
    Qmonth=np.zeros(Nmonth)     # Aloca lista com média de cada mês 
    Count_days=np.zeros(Nmonth) # Aloca lista com No. de dias de cada mês
    # for river in range(Columns):  # Laço de Rios
    for i in range(Rows):     # Laço de dias
        mi = month[i]-1       # Indice do mes 'month[i]'
        Qmonth[mi] = Qmonth[mi] + Q[i,rio] # Acumula a vazão do mês 'month[i]'
        Count_days[mi]+= 1                         # Contador do número de dias do mês 'month[i]'     

    for m in range(Nmonth):             # Faz a média 
        Qmonth[m] = Qmonth[m]/Count_days[m]

    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    ciclo_anual = go.Figure([go.Bar(x=meses, y=Qmonth)])
    
    ciclo_anual.update_layout(
        title='Ciclo Anual',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Vazão (m³/s)',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # espaço entre barras de coordenadas de localização adjacentes.
        bargroupgap=0.1 # espaço entre as barras da mesma coordenada de localização.
    )
    
    
    
    return  ciclo_anual
    
ciclo_anual_graph(0).show()

