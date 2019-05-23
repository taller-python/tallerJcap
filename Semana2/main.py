'''Operaciones con archivos'''
import openpyxl

def validate_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def write_file(result, filename):
    file = open('c:\\TallerPython\\Semana2\\Salidas\\'+ filename +'.txt', 'w')
    try:
        for i in result:
            file.write(str(i)+'\n')
    finally:
        file.close
#with open('c:\\TallerPython\\Semana2\\Ambiente\\Salidas\\'+ File +'.txt', 'w') as file:
#    file.write(str(result)+'\r\n')

def suma(sheet):
    total = 0
    result = []
    for filas in sheet.rows:
        number1 = filas[0].value
        number2 = filas[1].value
        if number1 != 'Numero 1' and number2 != 'Numero 2':
            if validate_number(number1) and validate_number(number2):
                try: 
                    total = number1 + number2
                except:
                    total = 'Error en la Operacion'
                result.append(total)
                #write_file(total,sheet.title)
            else:
                total = 'Error'
                result.append(total)
                #write_file(total,sheet.title)
    write_file(result, sheet.title)

def substraction(sheet):
    total = 0
    result = []
    for filas in sheet.rows:
        number1 = filas[0].value
        number2 = filas[1].value
        if number1 != 'Numero 1' and number2 != 'Numero 2':
            if validate_number(number1) and validate_number(number2):
                try: 
                    total = number1 - number2
                except:
                    total = 'Error en la Operacion'
                result.append(total)
                #write_file(total,sheet.title)
            else:
                total = 'Error'
                result.append(total)
                #write_file(total,sheet.title)
    write_file(result, sheet.title)

def multiplication(sheet):
    total = 0
    result = []
    for filas in sheet.rows:
        number1 = filas[0].value
        number2 = filas[1].value
        if number1 != 'Numero 1' and number2 != 'Numero 2':
            if validate_number(number1) and validate_number(number2):
                try: 
                    total = number1 * number2
                except:
                    total = 'Error en la Operacion'
                result.append(total)
                #write_file(total,sheet.title)
            else:
                total = 'Error'
                result.append(total)
                #write_file(total,sheet.title)
    write_file(result, sheet.title)

def division(sheet):
    total = 0
    result = []
    for filas in sheet.rows:
        number1 = filas[0].value
        number2 = filas[1].value
        if number1 != 'Numero 1' and number2 != 'Numero 2':
            if validate_number(number1) and validate_number(number2):
                try: 
                    total = number1 / number2
                except:
                    total = 'Error en la Operacion'
                result.append(total)
                #write_file(total,sheet.title)
            else:
                total = 'Error'
                result.append(total)
                #write_file(total,sheet.title)
    write_file(result, sheet.title)


DOC = openpyxl.load_workbook('c:\\TallerPython\\Semana2\\Recursos\\operaciones.xlsx')
SHEET_NAMES = DOC.sheetnames
print(SHEET_NAMES)

if 'SUMA' in SHEET_NAMES:
    suma(DOC['SUMA'])

if 'RESTA' in SHEET_NAMES:
    substraction(DOC['RESTA'])
if 'MULTIPLICACIÓN' in SHEET_NAMES:
    multiplication(DOC['MULTIPLICACIÓN'])
if 'DIVISIÓN' in SHEET_NAMES:
    division(DOC['DIVISIÓN'])
#else:
#    print('Operacion no implementada')
