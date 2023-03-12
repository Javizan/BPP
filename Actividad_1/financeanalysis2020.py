import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

csvfile = sys.argv[1]

def str_to_int(x):
    if isinstance(x, str):
        try:
            x = int(x)
        except:
            print("El dato no es casteable a un tipo numérico")
            try: 
                # Algunos datos están entrecomillados, intentar suprimirlas
                x = x.strip("\'")
                x = int(x)
            except:
                # Imposible de recuperar, se fuerza a 0
                x = 0
    return x

def sum_ingresos_gastos(df):
    dict_ingresos = {}
    dict_gastos = {}
    dict_resultados = {}
    for col in df.columns:
        suma_ingresos = df[col][df[col] > 0].sum()
        suma_gastos = df[col][df[col] < 0].sum()*(-1) # Se cambia el signo para facilitar la posterior representación
        dict_ingresos[col] = suma_ingresos
        dict_gastos[col] = suma_gastos
        dict_resultados[col] = suma_ingresos - suma_gastos
    return dict_ingresos, dict_gastos, dict_resultados

try:
    df = pd.read_csv(csvfile, sep='\t')
except FileNotFoundError:
    print('The file could not be found.')
    sys.exit(1)
except pd.errors.EmptyDataError:
    print('The file is empty.')
    sys.exit(1)




df = df.applymap(str_to_int)

# Comprobamos los meses que más se ha gastado / ahorrado y estadísticas temporales

dict_ingresos, dict_gastos, dict_resultados = sum_ingresos_gastos(df)

mes_max_ingresos = max(dict_ingresos, key=dict_ingresos.get)
mes_max_gastos = max(dict_gastos, key=dict_gastos.get)
mes_max_resultado = max(dict_resultados, key=dict_resultados.get)
mes_min_resultado = min(dict_resultados, key=dict_resultados.get)

ingreso_total = sum(dict_ingresos.values())
ingreso_promedio = ingreso_total/len(dict_ingresos)

gasto_total = sum(dict_gastos.values())
gasto_promedio = gasto_total/len(dict_gastos)

balance_total = sum(dict_resultados.values())
balance_promedio = balance_total/len(dict_resultados)



print(f"El mes en el que más se ha ahorrado ha sido {mes_max_resultado} con un balance neto de {dict_resultados[mes_max_resultado]}")
print(f"El mes en el que menos se ha ahorra ha sido {mes_min_resultado} con un balance neto de {dict_resultados[mes_min_resultado]}")
print(f"El mes en el que más se ha gastado ha sido {mes_max_ingresos} con un balance neto de {dict_ingresos[mes_max_ingresos]}")
print(f"El mes en el que más se ha gastado ha sido {mes_max_gastos} con un balance neto de {dict_gastos[mes_max_gastos]}\n")

print(f"Los ingresos totales durante el año 2020 han sido de {ingreso_total}")
print(f"Los gastos totales durante el año 2020 han sido de {gasto_total}")
print(f"El balance global en el año 2020 han sido de {balance_total}\n")

print(f"El ingreso promedio mensual en 2020 ha sido de {ingreso_promedio}")
print(f"El gasto promedio mensual en 2020 ha sido de {gasto_promedio}")
print(f"El balance promedo mensual en el año 2020 han sido de {balance_promedio}\n")

### Gráficas de balance mensual con matplotlib

bar_width = 0.25

x_labels = list(dict_ingresos.keys())
x_positions = np.arange(len(x_labels))

fig, ax = plt.subplots(figsize=(12,8))

ax.bar(x_positions - bar_width, dict_ingresos.values(), width=bar_width, label='Ingresos')
ax.bar(x_positions, dict_gastos.values(), width=bar_width, label='Gastos')
ax.bar(x_positions + bar_width, dict_resultados.values(), width=bar_width, label='Balance')

ax.set_xticks(x_positions)
ax.set_xticklabels(x_labels)

ax.set_ylabel('Euros (€)')

ax.legend()
plt.show()