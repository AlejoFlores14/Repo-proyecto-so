import pandas as pd
df = pd.read_csv('datos/resultados_torneo.csv',sep=';',encoding='latin-1')
def partidos_ganados():
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
    print("Cantidad de partidos ganados por cada equipo:")
    print(victorias)

def tabla_posiciones():
    posiciones = {}
    for _, partido in df.iterrows():
        equipo_local = partido['Equipo_Local']
        equipo_visitante = partido['Equipo_Visitante']
        goles_local = partido['Goles_Local']
        goles_visitante = partido['Goles_Visitante']
        for equipo in [equipo_local, equipo_visitante]:
            if equipo not in posiciones:
                posiciones[equipo] = {'Puntos': 0, 'Goles_Favor': 0, 'Goles_Contra': 0}
        if goles_local > goles_visitante:
            posiciones[equipo_local]['Puntos'] += 3
        elif goles_visitante > goles_local:
            posiciones[equipo_visitante]['Puntos'] += 3
        else:
            posiciones[equipo_local]['Puntos'] += 1
            posiciones[equipo_visitante]['Puntos'] += 1
        posiciones[equipo_local]['Goles_Favor'] += goles_local
        posiciones[equipo_local]['Goles_Contra'] += goles_visitante
        posiciones[equipo_visitante]['Goles_Favor'] += goles_visitante
        posiciones[equipo_visitante]['Goles_Contra'] += goles_local
    tabla_ordenada = dict(sorted(posiciones.items(), key=lambda item:(item[1]['Puntos'], item[1]['Goles_Favor']- item[1]['Goles_Contra']), reverse=True))
    print("Tabla de posiciones:")
    for equipo, datos in tabla_ordenada.items():
        print(f"{equipo}: Puntos={datos['Puntos']}, Goles a Favor={datos['Goles_Favor']}, Goles en Contra={datos['Goles_Contra']}")
def promedio_goles():
    total_goles = df['Goles_Local'].sum() + df['Goles_Visitante'].sum()
    total_partidos = len(df)
    promedio = total_goles / total_partidos if total_partidos > 0 else 0
    print(f"Promedio de goles por partido: {promedio:.2f}")
