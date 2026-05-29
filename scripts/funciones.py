"""..."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# leemos el archivo CSV con los resultados del torneo,
# utilizando el separador ';' y la codificación 'latin-1'
df = pd.read_csv('datos/resultados_torneo.csv',sep=';',encoding='latin-1')
# funcion para calcular las estadisticas de los equipos,
# recorriendo el CSV una sola vez y
# devolviendo un diccionario con las estadisticas necesarias para las demás funciones
def calcular_estadisticas():
    """Calcula las estadísticas de los equipos a partir de los resultados de los partidos."""
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
        # calculamos los puntos, victorias, empates y
        # derrotas para cada equipo, dependiendo del resultado del partido
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
    """Calcula y muestra la cantidad de partidos ganados por cada equipo."""
    victorias = calcular_estadisticas()
    ordenado = sorted(victorias.items(), key=lambda x: x[1]['Victorias'], reverse=True)
    for equipo, datos in ordenado:
        print(f"{equipo}: {datos['Victorias']} partidos ganados")
# funcion para calcular la tabla de posiciones,
# ordenando el diccionario de estadisticas por puntos y mostrando los resultados
def tabla_posiciones():
    """Calcula y muestra la tabla de posiciones ordenada por puntos."""
    posiciones = calcular_estadisticas()
    tabla_ordenada = sorted(posiciones.items(), key=lambda x: x[1]['Puntos'], reverse=True)
    print("Tabla de posiciones:")
    for equipo, datos in tabla_ordenada:
        print(f"{equipo}: Puntos:{datos['Puntos']},"
              f" Goles a Favor:{datos['Goles_Favor']},"
              f" Goles en Contra:{datos['Goles_Contra']}")
# funcion para calcular el promedio de goles por partido,
# sumando los goles locales y visitantes y dividiendo por la cantidad de partidos
def promedio_goles():
    """Calcula y muestra el promedio de goles por partido."""
    total_goles = df['Goles_Local'].sum() + df['Goles_Visitante'].sum()
    total_partidos = len(df)
    promedio = total_goles / total_partidos if total_partidos > 0 else 0
    print(f"Promedio de goles por partido: {promedio:.2f}")
# funciones para generar un gráfico comparativo de rendimiento entre equipos,
# utilizando el diccionario de estadisticas calculado previamente y mostrando los puntos,
# goles a favor y goles en contra de cada equipo en un gráfico de barras
def grafico_comparativo():
    """Genera un gráfico comparativo de rendimiento entre equipos."""
    estadisticas = calcular_estadisticas()
    estadisticas_ordenadas = sorted(estadisticas.items(),key=lambda x: x[1]['Puntos'],reverse=True)
    equipos = list(equipo for equipo, _ in estadisticas_ordenadas)
    puntos = [datos['Puntos'] for equipo, datos in estadisticas_ordenadas]
    goles_favor = [datos['Goles_Favor'] for _, datos in estadisticas_ordenadas]
    goles_contra = [datos['Goles_Contra'] for _, datos in estadisticas_ordenadas]
    # victorias = [datos['Victorias'] for _, datos in estadisticas_ordenadas]
    # empates = [datos['Empates'] for _, datos in estadisticas_ordenadas]
    # derrotas = [datos['Derrotas'] for _, datos in estadisticas_ordenadas]

    x = np.arange(len(equipos))
    ancho = 0.15
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Comparativa de Rendimiento entre Equipos', fontsize=16, fontweight='bold', y=1.05)
    colores = plt.colormaps['viridis'](np.linspace(0.2, 0.9, len(equipos)))
    barras  = axes[0].bar(equipos, puntos, color=colores, edgecolor='black', linewidth=0.7)
    axes[0].set_title('Puntos por Equipo', fontweight='bold')
    axes[0].set_ylabel('Puntos')
    axes[0].set_xticks(range(len(equipos)))
    axes[0].set_xticklabels(equipos, rotation=30, ha='right')
    axes[0].bar_label(barras, padding=3, fontweight='bold')
    axes[0].set_ylim(0, max(puntos) * 1.15)
    axes[0].grid(axis='y', linestyle='--', alpha=0.5)
    b1 = axes[1].bar(x - ancho / 2, goles_favor,  ancho, label='Goles a Favor',
                     color='steelblue', edgecolor='black', linewidth=0.7)
    b2 = axes[1].bar(x + ancho / 2, goles_contra, ancho, label='Goles en Contra',
                     color='tomato',    edgecolor='black', linewidth=0.7)
    axes[1].set_title('Goles a Favor vs. En Contra', fontweight='bold')
    axes[1].set_ylabel('Goles')
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(equipos, rotation=30, ha='right')
    axes[1].legend()
    axes[1].bar_label(b1, padding=2)
    axes[1].bar_label(b2, padding=2)
    axes[1].set_ylim(0, max(goles_favor + goles_contra) * 1.15)
    axes[1].grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('comparativa_rendimiento.png', dpi=300, bbox_inches='tight')
    plt.show()
def detalle_partidos():
    """Muestra el detalle de los partidos jugados."""
    ver_partidos = input("¿Desea ver el detalle de los partidos? (s/n): ").strip().lower()
    if ver_partidos == 's':
        print("\nDetalle de los partidos:")
        for _, partido in df.iterrows():
            print(f"{partido['Equipo_Local']} {partido['Goles_Local']} - "
                  f"{partido['Goles_Visitante']} {partido['Equipo_Visitante']}")