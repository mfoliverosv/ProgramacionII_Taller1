# Programa 2: registro de varios clientes y estadisticas

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
    cedula = input("Cedula: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")

    print("1. Particular")
    print("2. EPS")
    print("3. Prepagada")
    opcion_cliente = input("Tipo de cliente: ")

    tipos_cliente = {
        "1": "Particular",
        "2": "EPS",
        "3": "Prepagada"
    }

    while opcion_cliente not in tipos_cliente:
        print("Opcion invalida. Intente nuevamente.")
        opcion_cliente = input("Tipo de cliente: ")

    tipo_cliente = tipos_cliente[opcion_cliente]

    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extraccion")
    print("4. Diagnostico")
    opcion_atencion = input("Tipo de atencion: ")

    tipos_atencion = {
        "1": "Limpieza",
        "2": "Calzas",
        "3": "Extraccion",
        "4": "Diagnostico"
    }

    while opcion_atencion not in tipos_atencion:
        print("Opcion invslida. Intente nuevamente.")
        opcion_atencion = input("Tipo de atencion: ")

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

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "total": total
    }

    return cliente


clientes = []

print("REGISTRO DE CLIENTES")
cantidad_clientes = int(input("¿Cuantos clientes desea registrar? "))

while cantidad_clientes <= 0:
    print("Debe registrar al menos un cliente.")
    cantidad_clientes = int(input("¿Cuantos clientes desea registrar? "))

for numero in range(cantidad_clientes):
    print("\nCliente", numero + 1)
    cliente = capturar_cliente()
    clientes.append(cliente)

total_clientes = len(clientes)
ingresos_totales = sum(cliente["total"] for cliente in clientes)
clientes_extraccion = sum(
    1 for cliente in clientes
    if cliente["tipo_atencion"] == "Extraccion"
)

print("\nESTADISTICAS")
print("Total de clientes:", total_clientes)
print("Ingresos totales recibidos: $", format(ingresos_totales, ","))
print("Clientes que solicitaron extraccion:", clientes_extraccion)

print("\nLISTA DE CLIENTES")
for cliente in clientes:
    print(cliente)
