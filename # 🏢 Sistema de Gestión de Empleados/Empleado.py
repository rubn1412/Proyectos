class Empleado:
    contadorEmpleado = 0
    def __init__(self,nombre,departamento):
        Empleado.contadorEmpleado += 1
        self._nombre = nombre
        self._departamento = departamento
    @property
    def nombre(self):
        return self._nombre
    @property
    def departamento(self):
        return self._departamento

    @nombre.setter
    def nombre (self,nombre):
        self._nombre = nombre

    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
    @classmethod
    def contadorTotal(cls):
        return cls.contadorEmpleado
