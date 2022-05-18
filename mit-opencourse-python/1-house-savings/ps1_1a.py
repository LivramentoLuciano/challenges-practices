# Ejercicio 1_A
# Cuántos meses demoraria en ahorrar para pagar el depósito (down_payment)
# de una casa en funcion de ciertos parametros

# Parametros (deposito, ahorros, interes inversion)
portion_down_payment = 0.25
current_savings = 0
r = 0.04

# inputs usuario (salario anual, porcion ahorrada, costo total casa)
# con validacion de float
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

# al final del mes, mis ahorros crecen
# -> porcentaje ahorrado + los intereses de inversiones

def months_to_down_payment(annual_salary, portion_saved, total_cost):
    monthly_salary = annual_salary / 12

    num_months = 0
    savings = current_savings
    down_payment_cost = total_cost * portion_down_payment

    while savings < down_payment_cost:
        num_months += 1
        savings += (monthly_salary*portion_saved) + (savings * r/12)
    
    return num_months

months_to = months_to_down_payment(annual_salary, portion_saved, total_cost)
print(f'Número de meses: {months_to}')