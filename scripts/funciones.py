import pandas as pd
import matplotlib.pyplot as plt
# leemos el archivo CSV con los resultados del torneo, utilizando el separador ';' y la codificación 'latin-1'
df = pd.read_csv('datos/resultados_torneo.csv',sep=';',encoding='latin-1')
# funcion para calcular las estadisticas de los equipos, recorriendo el CSV una sola vez y devolviendo un diccionario con las estadisticas necesarias para las demás funciones
def calcular_estadisticas():
    estadisticas= {}
# recorremos el CSV una sola vez, utilizando iterrows() para obtener cada fila como un diccionario
    for _, partido in df.iterrows():
        equipo_local = partido['Equipo_Local']
        equipo_visitante = partido['Equipo_Visitante']
        goles_local = partido['Goles_Local']
        goles_visitante = partido['Goles_Visitante']
        # para cada equipo, si no está en el diccionario de estadisticas, lo inicializamos con 0  
        for equipo in [equipo_local, equipo_visitante]:
            if equipo not in estadisticas:
                estadisticas[equipo] = {'Puntos': 0,
                                        'Goles_Favor': 0,
                                        'Goles_Contra': 0,
                                        'Victorias': 0,
                                        'Empates': 0,
                                        'Derrotas': 0}
        # calculamos los puntos, victorias, empates y derrotas para cada equipo, dependiendo del resultado del partido
        if goles_local > goles_visitante:
            estadisticas[equipo_local]['Puntos'] += 3
            estadisticas[equipo_local]['Victorias'] += 1
            estadisticas[equipo_visitante]['Derrotas'] += 1
        elif goles_visitante > goles_local:
            estadisticas[equipo_visitante]['Victorias'] += 1
            estadisticas[equipo_local]['Derrotas'] += 1
            estadisticas[equipo_visitante]['Puntos'] += 3
        else:
            estadisticas[equipo_local]['Puntos'] += 1           
            estadisticas[equipo_visitante]['Puntos'] += 1
            estadisticas[equipo_local]['Empates'] += 1
            estadisticas[equipo_visitante]['Empates'] += 1

        estadisticas[equipo_local]['Goles_Favor'] += goles_local
        estadisticas[equipo_local]['Goles_Contra'] += goles_visitante
        estadisticas[equipo_visitante]['Goles_Favor'] += goles_visitante
        estadisticas[equipo_visitante]['Goles_Contra'] += goles_local
    return estadisticas
# funcion para calcular la cantidad de partidos ganados por cada equipo,
# utilizando el diccionario de estadisticas calculado previamente
def partidos_ganados():
    victorias = calcular_estadisticas()
    ordenado = sorted(victorias.items(), key=lambda x: x[1]['Victorias'], reverse=True)
    for equipo, datos in ordenado:
        print(f"{equipo}: {datos['Victorias']} partidos ganados")
# funcion para calcular la tabla de posiciones, ordenando el diccionario de estadisticas por puntos y mostrando los resultados
def tabla_posiciones():
    posiciones = calcular_estadisticas()
    tabla_ordenada = sorted(posiciones.items(), key=lambda x: x[1]['Puntos'], reverse=True)
    print("Tabla de posiciones:")
    for equipo, datos in tabla_ordenada:
        print(f"{equipo}: Puntos:{datos['Puntos']}, Goles a Favor:{datos['Goles_Favor']}, Goles en Contra:{datos['Goles_Contra']}")
# funcion para calcular el promedio de goles por partido, sumando los goles locales y visitantes y dividiendo por la cantidad de partidos
def promedio_goles():
    total_goles = df['Goles_Local'].sum() + df['Goles_Visitante'].sum()
    total_partidos = len(df)
    promedio = total_goles / total_partidos if total_partidos > 0 else 0
    print(f"Promedio de goles por partido: {promedio:.2f}")
