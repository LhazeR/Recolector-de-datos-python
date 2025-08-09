"""
Proyecto Base de empleados para el area de urgencias de un hospital
"""

class EmpleadoUrgencias:
    def __init__(self, cedula, nombre, apellido, cargo, turno, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo  # Ej: Médico, Enfermero, Técnico
        self.turno = turno  # Ej: Día, Noche
        self.edad = edad

    def actualizar(self, nombre, apellido, cargo, turno, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.turno = turno
        self.edad = edad

    def mostrar(self):
        print(f"\nCÉDULA: {self.cedula}")
        print(f"NOMBRE: {self.nombre}")
        print(f"APELLIDO: {self.apellido}")
        print(f"CARGO: {self.cargo}")
        print(f"TURNO: {self.turno}")
        print(f"EDAD: {self.edad}")


class SistemaEmpleadosUrgencias:
    def __init__(self):
        self.empleados = {}

    def buscar_empleado(self, cedula):
        if cedula == 0:
            if not self.empleados:
                print("\n⚠️ NO HAY EMPLEADOS REGISTRADOS")
            else:
                print("\n👥 LISTA DE EMPLEADOS REGISTRADOS:")
                for emp in self.empleados.values():
                    emp.mostrar()
        else:
            empleado = self.empleados.get(cedula)
            if empleado:
                empleado.mostrar()
            else:
                print("\n❌ EMPLEADO NO ENCONTRADO")
                self.validar_registro(cedula)

    def añadir_empleado(self, cedula):
        if cedula in self.empleados:
            print("\n⚠️ EMPLEADO YA REGISTRADO")
            return

        nombre = input("NOMBRE: ")
        apellido = input("APELLIDO: ")
        cargo = input("CARGO (Médico, Enfermero, Técnico, etc.): ")
        turno = input("TURNO (Día / Noche): ")

        while True:
            try:
                edad = int(input("EDAD: "))
                if edad > 0:
                    if edad >= 18:
                        break
                    else:
                        print("La edad debe ser mayor a 18")
                else:
                    print("La edad debe ser mayor que 0.")
            except ValueError as e:
                print(f"Error: {e}")

        self.empleados[cedula] = EmpleadoUrgencias(cedula, nombre, apellido, cargo, turno, edad)
        print("\n✅ EMPLEADO REGISTRADO EXITOSAMENTE")

    def actualizar_empleado(self, cedula):
        empleado = self.empleados.get(cedula)
        if not empleado:
            print("\n❌ EMPLEADO NO ENCONTRADO")
            self.validar_registro(cedula)
            return

        print("\n🔄 ACTUALIZANDO EMPLEADO...")
        nombre = input("NUEVO NOMBRE: ")
        apellido = input("NUEVO APELLIDO: ")
        cargo = input("NUEVO CARGO: ")
        turno = input("NUEVO TURNO: ")

        while True:
            try:
                edad = int(input("NUEVA EDAD: "))
                if edad > 0:
                    break
                else:
                    print("La edad debe ser mayor que 0.")
            except ValueError as e:
                print(f"Error: {e}")

        empleado.actualizar(nombre, apellido, cargo, turno, edad)
        print("\n✅ DATOS ACTUALIZADOS")

    def eliminar_empleado(self, cedula):
        if cedula in self.empleados:
            del self.empleados[cedula]
            print("\n🗑️ EMPLEADO ELIMINADO")
        else:
            print("\n❌ EMPLEADO NO ENCONTRADO")

    def validar_registro(self, cedula):
        print(f"\n¿Desea registrar al empleado con cédula {cedula}?")
        print("1. Sí\n2. No")
        while True:
            try:
                op = int(input("Seleccione una opción: "))
                if op in [1, 2]:
                    break
                else:
                    print("Ingrese 1 o 2.")
            except ValueError:
                print("Entrada inválida.")

        if op == 1:
            self.añadir_empleado(cedula)


def solicitar_cedula():
    while True:
        try:
            return int(input("Ingrese la CÉDULA del empleado: "))
        except ValueError:
            print("❌ Cédula inválida. Intente nuevamente.")


def mostrar_menu():
    opciones = [
        "1. Buscar empleado",
        "2. Registrar empleado",
        "3. Actualizar empleado",
        "4. Eliminar empleado",
        "5. Salir"
    ]
    print("\n=== MENU PRINCIPAL - URGENCIAS ===")
    for op in opciones:
        print(op)

    while True:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("❌ Entrada inválida. Intente nuevamente.")


# Bloque principal
if __name__ == "__main__":
    sistema = SistemaEmpleadosUrgencias()

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            cedula = solicitar_cedula()
            sistema.buscar_empleado(cedula)
        elif opcion == 2:
            cedula = solicitar_cedula()
            sistema.añadir_empleado(cedula)
        elif opcion == 3:
            cedula = solicitar_cedula()
            sistema.actualizar_empleado(cedula)
        elif opcion == 4:
            cedula = solicitar_cedula()
            sistema.eliminar_empleado(cedula)
        elif opcion == 5:
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n❌ Opción inválida.")
