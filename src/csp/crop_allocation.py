"""
Módulo CSP: Asignación de variedades de café a parcelas
"""

from constraint import Problem

def solve_farm_csp(parcelas):
    """
    parcelas: lista de dicts con altitud, ph, sombra
    Ej: [{"id": "A1", "altitud": 1500, "ph": 6.2, "sombra": 0.4}]
    """
    problem = Problem()
    variedades = ["Arabica", "Robusta", "Bourbon", "Caturra", "Catuai"]
    
    for p in parcelas:
        pid = p["id"]
        # Solo agregar variedades válidas para esa parcela
        opciones_validas = _variedades_validas(p, variedades)
        problem.addVariable(pid, opciones_validas)
    
    # Constraint: parcelas adyacentes no pueden ser incompatibles
    # (definir lista de adyacencias como parámetro)
    
    return problem.getSolution()

def _variedades_validas(parcela, variedades):
    validas = []
    for v in variedades:
        if _cumple_altitud(parcela["altitud"], v) and \
           _cumple_ph(parcela["ph"], v):
            validas.append(v)
    return validas if validas else variedades  # fallback

def _cumple_altitud(alt, variedad):
    rangos = {
        "Arabica":  (1200, 2000),
        "Robusta":  (0,    800),
        "Bourbon":  (1200, 1800),
        "Caturra":  (1000, 1700),
        "Catuai":   (1000, 1800),
    }
    lo, hi = rangos[variedad]
    return lo <= alt <= hi

def _cumple_ph(ph, variedad):
    # Café en general: 6.0–6.5 óptimo, tolera 5.5–7.0
    return 5.5 <= ph <= 7.0