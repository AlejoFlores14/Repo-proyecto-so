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
from funciones import partidos_ganados, tabla_posiciones

if __name__ == "__main__":
    partidos_ganados()
    tabla_posiciones()