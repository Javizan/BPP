import pytest
import statistics

# En este script se encuentras los tests a aplicar al módulo "statistics.py" siguiendo la librería pytest.
# Un test es asignado a cada función en base a resultados conocidos a priori. Se recomendarían más de uno para cubrir excepciones (como divisiones por 0 u algunos
# algoritmos con bifurcaciones como el de la mediana)

def test_media():
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    media_statistics = statistics.media(datos)
    media_test = 5.5
    assert media_statistics == media_test

def test_moda():
    datos = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10]
    moda_statistics = statistics.moda(datos)
    moda_test = 4
    assert moda_statistics == moda_test

def test_mediana():
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mediana_statistics = statistics.mediana(datos)
    mediana_test = 5.5
    assert mediana_statistics == mediana_test

def test_varianza():
    datos = [2, 7, 3, 12, 9]
    varianza_statistics = statistics.varianza(datos)
    varianza_test = 13.84
    assert varianza_statistics == varianza_test

def test_desviacion_tipica():
    datos = [2, 4, 2, 4, 2, 4]
    desv_statistics = statistics.desviacion_tipica(datos)
    desv_test = 1
    assert desv_statistics == desv_test

