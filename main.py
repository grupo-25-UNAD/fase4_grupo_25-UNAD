"""
SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ
Curso: Programación - UNAD
Fase 4 - Prácticas simuladas

Desarrollado por:
Javid Daniel vega iseda
Alejandro javier De Angel luquez
Kevid Andres Ordosgoitia herrera
MIGUEL EDUARDO PACHECO SAUCEDO

Descripción:
Sistema orientado a objetos para gestión de
clientes, servicios y reservas, implementando:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones
- Logs de eventos

"""
# IMPORTACIONES


from modelos.cliente import Cliente

from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from modelos.reserva import Reserva

from excepciones.excepciones_personalizadas import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)

from utils.logger import registrar_log


print("\n=== SISTEMA SOFTWARE FJ ===\n")


# Registro automático de clientes del sistema
clientes = []

datos_clientes = [

    (
        "Javid Daniel Vega Iseda",
        "3242578214",
        "jisedavega@gmail.com"
    ),

    (
        "Alejandro Javier De Angel Luquez",
        "3014066011",
        "alejandro76406@gmail.com"
    ),

    (
        "Kevin Andres Ordosgoitia Herrera",
        "3024654560",
        "kevinherrerapro18@gmail.com"
    ),

    (
        "MIGUEL EDUARDO PACHECO SAUCEDO",
        "3242056541",
        "migueleduardopachecosaucedo@gmail.com"
    )
]


# Creación y validación de clientes
for nombre, documento, correo in datos_clientes:

    try:

        cliente = Cliente(
            nombre,
            documento,
            correo
        )

        clientes.append(cliente)

        print(cliente.mostrar_informacion())
        print("\n")

    except ErrorCliente as e:

        print(
            f"Error registrando cliente: {e}"
        )


# Simulación de cliente inválido
try:

    cliente_error = Cliente(
        "",
        "ABC123",
        "correo_malo"
    )

    print(cliente_error.mostrar_informacion())

except ErrorCliente as e:

    print(
        f"Error cliente inválido: {e}"
    )


# Creación de servicios disponibles
try:

    servicio1 = ReservaSala(
        "Sala Premium",
        50000,
        4
    )

    print(servicio1.describir_servicio())
    print("\n")

except ErrorServicio as e:

    print(f"Error servicio 1: {e}")


try:

    servicio2 = AlquilerEquipo(
        "Laptop Gamer",
        80000,
        3
    )

    print(servicio2.describir_servicio())
    print("\n")

except ErrorServicio as e:

    print(f"Error servicio 2: {e}")


try:

    servicio3 = AsesoriaEspecializada(
        "Asesoría IA",
        100000,
        "avanzada"
    )

    print(servicio3.describir_servicio())
    print("\n")

except ErrorServicio as e:

    print(f"Error servicio 3: {e}")


# Simulación de servicio inválido
try:

    servicio_error = ReservaSala(
        "Sala Error",
        30000,
        -5
    )

    print(servicio_error.describir_servicio())

except ErrorServicio as e:

    print(
        f"Error servicio inválido: {e}"
    )


# Reservas realizadas por los clientes
try:

    reserva1 = Reserva(
        clientes[0],
        servicio1,
        4
    )

    print(reserva1.mostrar_reserva())

    print(
        reserva1.procesar_reserva()
    )

    print(
        reserva1.mostrar_reserva()
    )

    print("\n")

except ErrorReserva as e:

    print(f"Error reserva 1: {e}")


try:

    reserva2 = Reserva(
        clientes[1],
        servicio2,
        3
    )

    print(reserva2.mostrar_reserva())

    print(
        reserva2.procesar_reserva()
    )

    print(
        reserva2.mostrar_reserva()
    )

    print("\n")

except ErrorReserva as e:

    print(f"Error reserva 2: {e}")


try:

    reserva3 = Reserva(
        clientes[2],
        servicio3,
        2
    )

    print(reserva3.mostrar_reserva())

    print(
        reserva3.procesar_reserva()
    )

    print(
        reserva3.mostrar_reserva()
    )

    print("\n")

except ErrorReserva as e:

    print(f"Error reserva 3: {e}")


try:

    reserva4 = Reserva(
        clientes[3],
        servicio1,
        5
    )

    print(reserva4.mostrar_reserva())

    print(
        reserva4.procesar_reserva()
    )

    print(
        reserva4.mostrar_reserva()
    )

    print("\n")

except ErrorReserva as e:

    print(f"Error reserva 4: {e}")


# Simulación de reserva inválida
try:

    reserva_error = Reserva(
        clientes[0],
        servicio1,
        -10
    )

    print(
        reserva_error.mostrar_reserva()
    )

    print(
        reserva_error.procesar_reserva()
    )

except ErrorReserva as e:

    print(
        f"Error reserva inválida: {e}"
    )


finally:

    registrar_log(
        "El sistema finalizó correctamente"
    )

    print("=== FIN DEL SISTEMA ===")
