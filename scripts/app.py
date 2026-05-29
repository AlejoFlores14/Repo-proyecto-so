"""..."""
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
from funciones import (detalle_partidos, grafico_comparativo, partidos_ganados,
                        partidos_ganados, tabla_posiciones, promedio_goles)

if __name__ == "__main__":
    detalle_partidos()
    print("\nEstadísticas del campeonato:")
    print("-" * 30)
    print("Cantidad de partidos ganados por cada equipo:")
    partidos_ganados()
    print("-" * 30)
    tabla_posiciones()
    print("-" * 30)
    promedio_goles()
    print("-" * 30)
    grafico_comparativo()
    
