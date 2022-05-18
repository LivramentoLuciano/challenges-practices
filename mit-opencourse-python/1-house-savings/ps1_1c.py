# Ejercicio 1_C
# En esta oportunidad, se modifica el enfoque del problema
# y se desea conocer cuánto debería ahorrar para conseguir
# mi objetivo en X cantidad de meses (3 años)

import pandas as pd

# Parametros 
# (deposito, ahorros, interes inversion, aumento semestral, costo casa)
portion_down_payment = 0.25
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
total_cost = 1000000

# inputs usuario con validacion de float
# (salario anual inicial)
annual_salary = input('Ingrese su salario anual: ')
try:
    annual_salary = float(annual_salary)
except:
    print('El dato ingresado no es un número válido. Inténtelo nuevamente!')
    exit()

# ahora quiero saber que porcentaje debo ahorrar 
# para conseguir lo necesario en un tiempo de 3 años (36 meses)
# margen de $100 se considera ok

# En funcion del porcentaje de ahorro
# calculo cuanto tendre en 3 años (36 meses)
#
# se define una precisión de decimal de % (1 sobre 10000)
# podemos hacer la busqueda con numeros entre 1 y 10000 
# (== 0.01% a 100%)
def three_year_savings(saving_rate):
    savings = current_savings
    monthly_salary = annual_salary / 12

    saving_rate = saving_rate / 10000

    month = 0
    while month < 36:
        month += 1
        if (month % 6) == 0:
            monthly_salary *= 1 + semi_annual_raise        
        savings += (monthly_salary*saving_rate) + (savings * r/12)

    return savings


savings_variants = pd.DataFrame()

# Encontrar el saving_rate, entre una lista de candidatos,
# que me permita conseguir mi objetivo de ahorro (total_cost, $1M) 
# en el período de tiempo deseado (3 años) 
#
# Usa metodo biseccion
def search_best_saving_rate(total_cost, saving_rates):
    iterations = 1
    # indices de la lista sobre entre los q busco la solucion
    left = 0
    right = len(saving_rates) - 1
    mid = (right + left) // 2
    error = False

    # valor que queremos verificar q se cumpla entre los candidatos
    target = total_cost*portion_down_payment

    # primera iteracion
    savings = three_year_savings(saving_rates[mid])
    while not (savings <= target + 100 and savings >= target - 100):
        # si no se alcanzo el objetivo (+- $100)
        # me desplazo hacia la mitad correspondiente
        # (si me pase o me quede corto) y vuelvo a iterar
        if savings < target:
            left = mid + 1
        else:
            right = mid - 1

        mid = (right + left) // 2
        savings = three_year_savings(saving_rates[mid])
        iterations += 1
        
        # detecto error, no hay match del valor buscado
        if iterations > 10000:
            error = True
            break
    
    # el saving_rate que alcanza el objetivo planteado
    best_rate = mid
    best_rate = best_rate
    return (best_rate,iterations, error)


# debo buscar entre los porcentajes desde 0.01% a 100% 
# cual me dará el resultado deseado (costo de la casa)
# Se debe realizar con metodo de biseccion 
saving_rates = range(1,10000)
best_saving_rate, search_steps, error = search_best_saving_rate(total_cost, saving_rates)

if not error:
    print(f'El mejor porcentaje de ahorro es: {best_saving_rate/10000 * 100}%')
    print(f'Pasos utilizados en la búsqueda: {search_steps}')
else:
    print(f'No será posible ahorrar el dinero deseado con un salario inicial de ${annual_salary}')