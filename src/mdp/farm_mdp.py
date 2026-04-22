"""
Definición del Proceso de Decisión de Markov para la granja
Estados: condiciones de la granja, clima, enfermedades
Acciones: plantación, riego, fertilización, tratamientos
Transiciones: probabilidades de cambio de estado
"""

ACCIONES = ["fertilizar", "fungicida", "podar", "cosechar_temprano", "replantar"]

ESTADOS = {
    # (salud_cultivo, presupuesto, temporada, riesgo_roya)
    # salud: 0=malo, 1=regular, 2=bueno
    # presupuesto: 0=bajo, 1=medio, 2=alto
    # temporada: 0=seca, 1=lluvia
    # riesgo_roya: 0=bajo, 1=alto
}

def recompensa(estado, accion):
    salud, presupuesto, temporada, riesgo = estado
    
    costos = {
        "fertilizar": -200,
        "fungicida": -150,
        "podar": -100,
        "cosechar_temprano": -50,
        "replantar": -500
    }
    
    ganancia_base = salud * 800  # Q por hectárea según salud
    penalizacion_roya = -600 if riesgo == 1 and accion != "fungicida" else 0
    
    return ganancia_base + costos[accion] + penalizacion_roya

def transicion(estado, accion):
    """Retorna dict {nuevo_estado: probabilidad}"""
    # Simplificado — calibrar con datos FAO después
    salud, presupuesto, temporada, riesgo = estado
    # ...
    pass