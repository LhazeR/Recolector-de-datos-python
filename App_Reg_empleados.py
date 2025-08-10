"""
Proyecto Base de empleados para un hospital con búsqueda por área y turno
"""

class Empleado:
    def __init__(self, cedula, nombre, apellido, cargo, turno, edad, area):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.turno = turno  # "Día" o "Noche"
        self.edad = edad
        self.area = area

    def actualizar(self, nombre, apellido, cargo, turno, edad, area):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.turno = turno
        self.edad = edad
        self.area = area

    def mostrar(self):
        print(f"\nCÉDULA: {self.cedula}")
        print(f"NOMBRE: {self.nombre}")
        print(f"APELLIDO: {self.apellido}")
        print(f"CARGO: {self.cargo}")
        print(f"TURNO: {self.turno}")
        print(f"EDAD: {self.edad}")
        print(f"ÁREA: {self.area}")


class EmpleadoUrgencias(Empleado):
    def __init__(self, cedula, nombre, apellido, cargo, turno, edad):
        super().__init__(cedula, nombre, apellido, cargo, turno, edad, area="Urgencias")


class SistemaEmpleados:
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

    def buscar_por_area(self, area):
        encontrados = [emp for emp in self.empleados.values() if emp.area.lower() == area.lower()]
        if encontrados:
            print(f"\n📌 Empleados en el área {area}:")
            for emp in encontrados:
                emp.mostrar()
        else:
            print(f"\n❌ No hay empleados en el área {area}")

    def buscar_por_turno(self, turno):
        encontrados = [emp for emp in self.empleados.values() if emp.turno.lower() == turno.lower()]
        if encontrados:
            print(f"\n📌 Empleados disponibles en turno {turno}:")
            for emp in encontrados:
                emp.mostrar()
        else:
            print(f"\n❌ No hay empleados en el turno {turno}")

    def añadir_empleado(self, cedula):
        if cedula in self.empleados:
            print("\n⚠️ EMPLEADO YA REGISTRADO")
            return

        nombre = input("NOMBRE: ")
        apellido = input("APELLIDO: ")
        cargo = input("CARGO (Médico, Enfermero, Técnico, etc.): ")
        turno = input("TURNO (Día / Noche): ")
        area = input("ÁREA: ")

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

        self.empleados[cedula] = Empleado(cedula, nombre, apellido, cargo, turno, edad, area)
        print("\n✅ EMPLEADO REGISTRADO EXITOSAMENTE")

    def actualizar_empleado(self, cedula):
        empleado = self.empleados.get(cedula)
        if not empleado:
            print("\n❌ EMPLEADO NO ENCONTRADO")
            self.validar_registro(cedula)
            return

        print("\n🔄 ACTUALIZANDO EMPLEADO...")
        nombre = input(f"NUEVO NOMBRE ({empleado.nombre}): ") or empleado.nombre
        apellido = input(f"NUEVO APELLIDO ({empleado.apellido}): ") or empleado.apellido
        cargo = input(f"NUEVO CARGO ({empleado.cargo}): ") or empleado.cargo
        turno = input(f"NUEVO TURNO ({empleado.turno}): ") or empleado.turno
        area = input(f"NUEVA ÁREA ({empleado.area}): ") or empleado.area

        while True:
            try:
                edad_input = input(f"NUEVA EDAD ({empleado.edad}): ")
                edad = int(edad_input) if edad_input else empleado.edad
                if edad > 0:
                    break
                else:
                    print("La edad debe ser mayor que 0.")
            except ValueError as e:
                print(f"Error: {e}")

        empleado.actualizar(nombre, apellido, cargo, turno, edad, area)
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
        "5. Buscar por área",
        "6. Buscar por turno",
        "7. Salir"
    ]
    print("\n=== MENU PRINCIPAL ===")
    for op in opciones:
        print(op)

    while True:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("❌ Entrada inválida. Intente nuevamente.")


# Bloque principal
if __name__ == "__main__":
    sistema = SistemaEmpleados()

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
            area = input("Ingrese el área a buscar: ")
            sistema.buscar_por_area(area)
        elif opcion == 6:
            turno = input("Ingrese el turno a buscar (Día / Noche): ")
            sistema.buscar_por_turno(turno)
        elif opcion == 7:
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n❌ Opción inválida.")
