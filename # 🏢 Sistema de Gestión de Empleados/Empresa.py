from Empleado import*

class Empresa:
    contadorfinanzas = 0
    contadorInformatica = 0
    listaEmpleados = []
    def __init__(self,nombre):
        self._nombre = nombre
    @property
    def nombre (self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    def contratarEmpleados(self,nombre,departamento):
        nuevoEmpeleado = {"nombre": nombre, "departamento":departamento}
        Empresa.listaEmpleados.append(nuevoEmpeleado)
    @classmethod
    def numeroEmpleadosXDepartamento(cls):
        cls.contadorfinanzas = 0
        cls.contadorInformatica = 0
        for empleado in cls.listaEmpleados:
            depart = empleado.get("departamento").lower()
            if depart == "finanzas":
                cls.contadorfinanzas += 1
            elif depart == "informatica":
                cls.contadorInformatica +=1
        print (f'Informatica: {cls.contadorInformatica} Finanzas: {cls.contadorfinanzas}')
