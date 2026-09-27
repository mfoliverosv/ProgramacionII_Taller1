# Programa 4: programa integrado del consultorio odontologico

def obtener_valores(tipo_cliente, tipo_atencion):
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

    return valores_cita[tipo_cliente], valores_atencion[tipo_cliente][tipo_atencion]


def capturar_cliente():
    print("\n--- Datos del cliente ---")
    cedula = input("Cedula: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    fecha_cita = input("Fecha de la cita: ")

    print("\nTipo de cliente")
    print("1. Particular")
    print("2. EPS")
    print("3. Prepagada")
    opcion_cliente = input("Seleccione: ")

    tipos_cliente = {
        "1": "Particular",
        "2": "EPS",
        "3": "Prepagada"
    }

    while opcion_cliente not in tipos_cliente:
        print("Opcion invalida.")
        opcion_cliente = input("Seleccione: ")

    tipo_cliente = tipos_cliente[opcion_cliente]

    print("\nTipo de atencion")
    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extraccion")
    print("4. Diagnostico")
    opcion_atencion = input("Seleccione: ")

    tipos_atencion = {
        "1": "Limpieza",
        "2": "Calzas",
        "3": "Extraccion",
        "4": "Diagnostico"
    }

    while opcion_atencion not in tipos_atencion:
        print("Opcion invalida.")
        opcion_atencion = input("Seleccione: ")

    tipo_atencion = tipos_atencion[opcion_atencion]

    if tipo_atencion in ["Limpieza", "Diagnostico"]:
        cantidad = 1
    else:
        cantidad = int(input("Cantidad: "))

        while cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            cantidad = int(input("Cantidad: "))

    valor_cita, valor_atencion = obtener_valores(
        tipo_cliente,
        tipo_atencion
    )

    total = valor_cita + (valor_atencion * cantidad)

    return {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": "Normal",
        "fecha_cita": fecha_cita,
        "total": total
    }


clientes = []

print("SISTEMA DE GESTION DEL CONSULTORIO ODONTOLOGICO")
cantidad_clientes = int(input("¿Cuantos clientes desea registrar? "))

while cantidad_clientes <= 0:
    print("Debe registrar al menos un cliente.")
    cantidad_clientes = int(input("¿Cuantos clientes desea registrar? "))

for numero in range(cantidad_clientes):
    print("\nCliente", numero + 1)
    clientes.append(capturar_cliente())

# Ordenamiento de mayor a menor por el valor total.
clientes.sort(key=lambda cliente: cliente["total"], reverse=True)

total_clientes = len(clientes)
ingresos_totales = sum(cliente["total"] for cliente in clientes)
clientes_extraccion = sum(
    1 for cliente in clientes
    if cliente["tipo_atencion"] == "Extraccion"
)

print("\n--- RESULTADOS GENERALES ---")
print("Total de clientes:", total_clientes)
print("Ingresos totales: $", format(ingresos_totales, ","))
print("Clientes con extraccion:", clientes_extraccion)

print("\n--- CLIENTES ORDENADOS ---")
for cliente in clientes:
    print(
        cliente["cedula"],
        "-",
        cliente["nombre"],
        "- $",
        format(cliente["total"], ",")
    )

cedula_buscada = input("\nDigite una cédula para buscar: ")
encontrado = False

for cliente in clientes:
    if cliente["cedula"] == cedula_buscada:
        print("\n--- CLIENTE ENCONTRADO ---")
        print("Cedula:", cliente["cedula"])
        print("Nombre:", cliente["nombre"])
        print("Telefono:", cliente["telefono"])
        print("Tipo de cliente:", cliente["tipo_cliente"])
        print("Tipo de atencion:", cliente["tipo_atencion"])
        print("Cantidad:", cliente["cantidad"])
        print("Prioridad:", cliente["prioridad"])
        print("Fecha de la cita:", cliente["fecha_cita"])
        print("Total: $", format(cliente["total"], ","))
        encontrado = True
        break

if not encontrado:
    print("No se encontro un cliente con esa cedula.")
