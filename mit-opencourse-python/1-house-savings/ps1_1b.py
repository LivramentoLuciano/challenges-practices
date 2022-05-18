# Ejercicio 1_B
# Cuántos meses demoraria en ahorrar para pagar el depósito (down_payment)
# de una casa en funcion de ciertos parametros
#
# Ahora, el salario aumentará con el paso del tiempo

# Parametros (deposito, ahorros, interes inversion)
portion_down_payment = 0.25
current_savings = 0
r = 0.04

# inputs usuario con validacion de float
# (salario anual, porcion ahorrada, costo total casa, aumento semestral)
annual_salary = input('Ingrese su salario anual: ')
try:
    annual_salary = float(annual_salary)
except:
    print('El dato ingresado no es un número válido. Inténtelo nuevamente!')
    exit()

portion_saved = input('Ingrese el \% de su sueldo que ahorra (decimal): ')
try:
    portion_saved = float(portion_saved)
except:
    print('El dato ingresado no es un número válido. Inténtelo nuevamente!')
    exit()

total_cost = input('Ingrese el costo total de la casa: ')
try:
    total_cost = float(total_cost)
except:
    print('El dato ingresado no es un número válido. Inténtelo nuevamente!')
    exit()

semi_annual_raise = input('Ingrese su aumento semestral: ')
try:
    semi_annual_raise = float(semi_annual_raise)
except:
    print('El dato ingresado no es un número válido. Inténtelo nuevamente!')
    exit()

# al final del mes, mis ahorros crecen
# -> porcentaje ahorrado + los intereses de inversiones
# + cada 6 meses, aumento porcentual

def months_to_down_payment():
    monthly_salary = annual_salary / 12
    down_payment_cost = total_cost * portion_down_payment

    num_months = 0
    savings = current_savings

    while savings < down_payment_cost:
        num_months += 1
        if (num_months % 6) == 0:
            monthly_salary *= 1 + semi_annual_raise
        savings += (monthly_salary*portion_saved) + (savings * r/12)
    
    return num_months

months_to = months_to_down_payment()
print(f'Número de meses: {months_to}')