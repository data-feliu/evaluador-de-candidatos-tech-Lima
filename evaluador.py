# =============================================
# Evaluador de Candidatos Tech — Lima
# Autor: Luis Fernando Capacoila Copa
# Semana 2 - Nivel 0 Python
# =============================================

def separador(simbolo="=", largo=54):
    print(simbolo * largo)

separador()
print("  EVALUADOR DE CANDIDATOS TECH — LIMA".center(54))
print("  Para roles en Data & MLOps".center(54))
separador()
print()

# ---- RECOPILACIÓN DE DATOS ----
print("Responde con datos reales. El sistema es honesto.")
print()

nombre        = input("Nombre completo: ").strip()
edad          = int(input("Edad: "))
ciudad        = input("Ciudad: ").strip().lower()
sueldo_actual = float(input("Sueldo actual (S/, pon 0 si no trabajas): "))
años_exp      = int(input("Años de experiencia laboral (cualquier área): "))

print()
print("Habilidades técnicas (responde si/no):")
sabe_python   = input("  ¿Sabes Python básico?: ").strip().lower() == "si"
sabe_sql      = input("  ¿Sabes SQL?: ").strip().lower() == "si"
sabe_excel    = input("  ¿Manejas Excel/Google Sheets bien?: ").strip().lower() == "si"
tiene_github  = input("  ¿Tienes GitHub con proyectos?: ").strip().lower() == "si"
sabe_ingles   = input("  ¿Entiendes inglés técnico (leer docs)?: ").strip().lower() == "si"

print()
print("Disponibilidad:")
horas_dia     = float(input("  ¿Horas disponibles para estudiar por día?: "))
tiene_pc      = input("  ¿Tienes PC/laptop propia?: ").strip().lower() == "si"
tiene_internet= input("  ¿Tienes internet estable en casa?: ").strip().lower() == "si"

# ---- SISTEMA DE PUNTAJE ----
puntaje = 0
max_puntaje = 100

# Habilidades técnicas (50 puntos)
if sabe_python:   puntaje += 20
if sabe_sql:      puntaje += 15
if sabe_excel:    puntaje += 5
if tiene_github:  puntaje += 7
if sabe_ingles:   puntaje += 3

# Experiencia (20 puntos)
if años_exp == 0:     puntaje += 0
elif años_exp == 1:   puntaje += 8
elif años_exp <= 3:   puntaje += 14
else:                 puntaje += 20

# Disponibilidad (20 puntos)
if horas_dia >= 2:    puntaje += 20
elif horas_dia >= 1:  puntaje += 12
elif horas_dia >= 0.5:puntaje += 5
else:                 puntaje += 0

# Recursos (10 puntos)
if tiene_pc and tiene_internet:   puntaje += 10
elif tiene_pc or tiene_internet:  puntaje += 5
else:                             puntaje += 0

porcentaje = (puntaje / max_puntaje) * 100

# ---- CLASIFICACIÓN POR ROL ----
apto_analyst    = sabe_excel or sabe_sql or sabe_python
apto_scientist  = sabe_python and (sabe_sql or tiene_github)
apto_mlengineer = sabe_python and sabe_sql and tiene_github and años_exp >= 1
apto_mlops      = sabe_python and sabe_sql and tiene_github and años_exp >= 3

# ---- REPORTE FINAL ----
print()
separador()
print(f"  REPORTE DE EVALUACIÓN".center(54))
separador()

ciudad_display = ciudad.title()
if ciudad == "lima":
    ciudad_display += " (mercado principal)"
elif ciudad in ["arequipa", "trujillo", "cusco"]:
    ciudad_display += " (mercado regional)"
else:
    ciudad_display += " (considera trabajo remoto)"

print(f"  Ciudad:     {ciudad_display}")
print(f"  Sueldo:     S/ {sueldo_actual:,.0f}/mes actual")
print()

# Puntaje visual
barra_llena  = int(porcentaje / 5)
barra_vacia  = 20 - barra_llena
barra        = "█" * barra_llena + "░" * barra_vacia
print(f"  Puntaje:    {puntaje}/{max_puntaje} pts")
print(f"  [{barra}] {porcentaje:.0f}%")
print()

# Nivel general
separador("-", 54)
if porcentaje >= 80:
    nivel   = "SENIOR LISTO"
    color   = "Perfil muy sólido para el mercado tech"
elif porcentaje >= 60:
    nivel   = "INTERMEDIO"
    color   = "Buen perfil, algunas brechas por cerrar"
elif porcentaje >= 40:
    nivel   = "EN DESARROLLO"
    color   = "Vas por buen camino, sigue construyendo"
elif porcentaje >= 20:
    nivel   = "PRINCIPIANTE"
    color   = "Recién empiezas, enfócate en lo básico"
else:
    nivel   = "PUNTO DE PARTIDA"
    color   = "Cero no es malo, todos empezaron aquí"

print(f"  Nivel:      {nivel}")
print(f"  Estado:     {color}")

# Roles disponibles
print()
separador("-", 54)
print("  ROLES PARA LOS QUE PUEDES APLICAR HOY:")
separador("-", 54)

algun_rol = False
if apto_mlops:
    print("  MLOps Engineer       S/ 10,000–18,000/mes")
    algun_rol = True
if apto_mlengineer:
    print("  ML Engineer          S/ 8,000–12,000/mes")
    algun_rol = True
if apto_scientist:
    print("  Data Scientist       S/ 5,000–8,000/mes")
    algun_rol = True
if apto_analyst:
    print("  Data Analyst         S/ 3,000–5,000/mes")
    algun_rol = True
if not algun_rol:
    print("  Ninguno aún — pero eso cambia en semanas")

# Recomendaciones priorizadas
print()
separador("-", 54)
print("  PRÓXIMOS PASOS PRIORIZADOS:")
separador("-", 54)

paso = 1
if not tiene_pc or not tiene_internet:
    print(f"  {paso}. Consigue PC e internet estable — es urgente")
    paso += 1
if not sabe_python:
    print(f"  {paso}. Aprende Python — es la base de todo")
    paso += 1
if not sabe_sql:
    print(f"  {paso}. Aprende SQL — todo trabajo en datos lo pide")
    paso += 1
if not tiene_github:
    print(f"  {paso}. Crea tu GitHub y sube proyectos esta semana")
    paso += 1
if not sabe_ingles:
    print(f"  {paso}. Trabaja tu inglés técnico — abre el 80% de ofertas")
    paso += 1
if horas_dia < 1:
    print(f"  {paso}. Reorganiza tu agenda — necesitas mínimo 1h/día")
    paso += 1
if paso == 1:
    print(f"  1. Mantén el ritmo y busca proyectos reales")
    print(f"  2. Construye red de contactos en LinkedIn")

# Proyección temporal
print()
separador("-", 54)
horas_mes   = horas_dia * 30
if horas_mes > 0:
    meses_analist  = round(6   * (1.5 / max(horas_dia, 0.5)))
    meses_mlops    = round(36  * (1.5 / max(horas_dia, 0.5)))
    print(f"  Estudias ~{horas_mes:.0f}h/mes")
    print(f"  Data Analyst:   ~{meses_analist} meses")
    print(f"  MLOps Engineer: ~{meses_mlops} meses")
else:
    print("  Define cuántas horas estudiarás para proyectar")

sueldo_meta = 14000
if sueldo_actual > 0:
    incremento = sueldo_meta - sueldo_actual
    print(f"  Incremento salarial esperado: +S/ {incremento:,.0f}/mes")

separador()
print("  Evaluación generada con Python — Semana 2".center(54))
separador()