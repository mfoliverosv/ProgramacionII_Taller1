# Programa 1: captura de datos y cálculo de una cita

print("CONSULTORIO ODONTOLOGICO")
print("-------------------------")

cedula = input("Digite la cedula del cliente: ")
nombre = input("Digite el nombre del cliente: ")
telefono = input("Digite el telefono: ")

print("\nTipo de cliente")
print("1. Particular")
print("2. EPS")
print("3. Prepagada")
opcion_cliente = input("Seleccione una opcion: ")

tipos_cliente = {
    "1": "Particular",
    "2": "EPS",
    "3": "Prepagada"
}

if opcion_cliente not in tipos_cliente:
    print("Opcion no valida.")
else:
    tipo_cliente = tipos_cliente[opcion_cliente]

    print("\nTipo de atencion")
    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extraccion")
    print("4. Diagnostico")
    opcion_atencion = input("Seleccione una opcion: ")

    tipos_atencion = {
        "1": "Limpieza",
        "2": "Calzas",
        "3": "Extraccion",
        "4": "Diagnostico"
    }

    valores_cita = {
        "Particular": 80000,
        "EPS": 5000,
        "Prepagada": 30000
    }

    valores_atencion = {
        "Particular": {
            "Limpieza": 60000,
            "Calzas": 80000,
            "Extraccion": 100000,
            "Diagnostico": 50000
        },
        "EPS": {
            "Limpieza": 0,
            "Calzas": 40000,
            "Extraccion": 40000,
            "Diagnostico": 0
        },
        "Prepagada": {
            "Limpieza": 0,
            "Calzas": 10000,
            "Extraccion": 10000,
            "Diagnostico": 0
        }
    }

    if opcion_atencion not in tipos_atencion:
        print("Opcion no valida.")
    else:
        tipo_atencion = tipos_atencion[opcion_atencion]

        if tipo_atencion in ["Limpieza", "Diagnostico"]:
            cantidad = 1
        else:
            cantidad = int(input("Digite la cantidad: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                cantidad = 0

        if cantidad > 0:
            valor_cita = valores_cita[tipo_cliente]
            valor_atencion = valores_atencion[tipo_cliente][tipo_atencion]
            total = valor_cita + (valor_atencion * cantidad)

            print("\nRESUMEN DE LA CITA")
            print("Cedula:", cedula)
            print("Nombre:", nombre)
            print("Telefono:", telefono)
            print("Tipo de cliente:", tipo_cliente)
            print("Tipo de atencion:", tipo_atencion)
            print("Cantidad:", cantidad)
            print("Valor de la cita: $", format(valor_cita, ","))
            print("Valor de la atencion: $", format(valor_atencion, ","))
            print("Total a pagar: $", format(total, ","))
            print("Nota: el valor de la cita se suma una sola vez.")