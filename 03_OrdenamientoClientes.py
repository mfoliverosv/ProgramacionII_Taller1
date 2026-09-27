# Programa 3: ordenar clientes y buscar por cedula

clientes = [
    {
        "cedula": "1003",
        "nombre": "Carlos",
        "total": 145000
    },
    {
        "cedula": "1001",
        "nombre": "Ana",
        "total": 260000
    },
    {
        "cedula": "1002",
        "nombre": "Luis",
        "total": 90000
    }
]

print("CLIENTES ANTES DE ORDENAR")
for cliente in clientes:
    print(cliente)

# Ordenar de mayor a menor según el valor total de la atencion.
clientes_ordenados = sorted(
    clientes,
    key=lambda cliente: cliente["total"],
    reverse=True
)

print("\nCLIENTES ORDENADOS DE MAYOR A MENOR")
for cliente in clientes_ordenados:
    print(cliente)

cedula_buscada = input("\nDigite la cedula que desea buscar: ")

cliente_encontrado = None

for cliente in clientes_ordenados:
    if cliente["cedula"] == cedula_buscada:
        cliente_encontrado = cliente
        break

if cliente_encontrado is not None:
    print("\nCLIENTE ENCONTRADO")
    print("Cedula:", cliente_encontrado["cedula"])
    print("Nombre:", cliente_encontrado["nombre"])
    print("Valor total: $", format(cliente_encontrado["total"], ","))
else:
    print("\nNo se encontro un cliente con esa cedula.")
