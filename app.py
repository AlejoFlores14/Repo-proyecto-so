# Escenario D – Estadísticas de Resultados Deportivos
# El equipo analizará datos correspondientes a resultados de un campeonato deportivo.
# Objetivo
# Procesar los resultados de los partidos para generar estadísticas básicas del torneo.
# Tareas sugeridas
# ● Importar un archivo con resultados de partidos.
# ● Calcular:
# ○ cantidad de partidos ganados por cada equipo
# ○ tabla de posiciones
# ○ promedio de goles por partido
# ● Generar un gráfico comparativo de rendimiento entre equipos.

#importo el archivo con los resultados de los partidos
import pandas as pd
df = pd.read_csv('resultados_torneo.csv',sep=';',encoding='latin-1')
# print(df)
#calculo la cantidad de partidos ganados por cada equipo
victorias= {}
for _, partido in df.iterrows():
    equipo_local = partido['Equipo_Local']
    equipo_visitante = partido['Equipo_Visitante']
    goles_local = partido['Goles_Local']
    goles_visitante = partido['Goles_Visitante']
    if equipo_local not in victorias:
        victorias[equipo_local ] = 0
    if equipo_visitante not in victorias:
        victorias[equipo_visitante] = 0
    if goles_local > goles_visitante:
        victorias[equipo_local] += 1
    elif goles_visitante > goles_local:
        victorias[equipo_visitante] += 1
print(victorias)