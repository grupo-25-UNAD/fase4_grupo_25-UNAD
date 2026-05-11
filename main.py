"""
SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ
Curso: Programación - UNAD
Fase 4 - Prácticas simuladas

Desarrollado por:
Javid Daniel vega iseda
Alejandro javier De Angel luquez
Kevid Andres Ordosgoitia herrera


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


# CLIENTE 1


try:

    cliente1 = Cliente(
        "Javid Daniel vega iseda",
        "3242578214",
        "jisedavega@gmail.com"
    )

    print(cliente1.mostrar_informacion())

except ErrorCliente as e:

    print(f"Error cliente 1: {e}")


# CLIENTE 2


try:

    cliente2 = Cliente(
        "Alejandro Javier De Angel Luquez",
        "3014066011",
        "alejandro76406@gmail.com"
    )

    print("\n")
    print(cliente2.mostrar_informacion())

except ErrorCliente as e:

    print(f"Error cliente 2: {e}")


# CLIENTE 3


try:

    cliente3 = Cliente(
        "Kevin Andres Ordosgoitia Herrera",
        "3024654560",
        "kevinherrerapro18@gmail.com"
    )

    print("\n")
    print(cliente3.mostrar_informacion())

except ErrorCliente as e:

    print(f"Error cliente 3: {e}")


# CLIENTE INVÁLIDO


try:

    cliente_error = Cliente(
        "",
        "ABC123",
        "correo_malo"
    )

    print(cliente_error.mostrar_informacion())

except ErrorCliente as e:

    print(f"\nError cliente inválido: {e}")


# SERVICIO 1


try:

    servicio1 = ReservaSala(
        "Sala Premium",
        50000,
        4
    )

    print("\n")
    print(servicio1.describir_servicio())

except ErrorServicio as e:

    print(f"Error servicio 1: {e}")


# SERVICIO 2


try:

    servicio2 = AlquilerEquipo(
        "Laptop Gamer",
        80000,
        3
    )

    print("\n")
    print(servicio2.describir_servicio())

except ErrorServicio as e:

    print(f"Error servicio 2: {e}")


# SERVICIO 3


try:

    servicio3 = AsesoriaEspecializada(
        "Asesoría IA",
        100000,
        "avanzada"
    )

    print("\n")
    print(servicio3.describir_servicio())

except ErrorServicio as e:

    print(f"Error servicio 3: {e}")


# SERVICIO INVÁLIDO


try:

    servicio_error = ReservaSala(
        "Sala Error",
        30000,
        -5
    )

    print(servicio_error.describir_servicio())

except ErrorServicio as e:

    print(f"\nError servicio inválido: {e}")


# RESERVA 1


try:

    reserva1 = Reserva(
        cliente1,
        servicio1,
        4
    )

    print("\n")
    print(reserva1.mostrar_reserva())

    print(reserva1.procesar_reserva())

    print(reserva1.mostrar_reserva())

except ErrorReserva as e:

    print(f"Error reserva 1: {e}")


# RESERVA 2


try:

    reserva2 = Reserva(
        cliente2,
        servicio2,
        3
    )

    print("\n")
    print(reserva2.mostrar_reserva())

    print(reserva2.procesar_reserva())

    print(reserva2.mostrar_reserva())

except ErrorReserva as e:

    print(f"Error reserva 2: {e}")



# RESERVA 3


try:

    reserva3 = Reserva(
        cliente3,
        servicio3,
        2
    )

    print("\n")
    print(reserva3.mostrar_reserva())

    print(reserva3.procesar_reserva())

    print(reserva3.mostrar_reserva())

except ErrorReserva as e:

    print(f"Error reserva 3: {e}")



# RESERVA INVÁLIDA


try:

    reserva_error = Reserva(
        cliente1,
        servicio1,
        -10
    )

    print("\n")
    print(reserva_error.mostrar_reserva())

    print(reserva_error.procesar_reserva())

except ErrorReserva as e:

    print(f"\nError reserva inválida: {e}")



# FINAL DEL SISTEMA


finally:

    registrar_log(
        "El sistema finalizó correctamente"
    )

    print("\n=== FIN DEL SISTEMA ===")