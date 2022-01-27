from cargo import Cargo
class Empleado:
  secuencia=1
  Empleados= [{"codigo":1,"nombre":"And","cedula":"0606214211","cargo":"Boss","departamento":"Dece","sueldo":2500.55}]
  def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo ):
    Empleado.secuencia +=1
    self.codigo = Empleado.secuencia
    self.nombre = nombre
    self.cedula= cedula
    self.cargo = codCargo
    self.departamento = codDepartamento
    self.sueldo = sueldo
  def  registro(self):
    return {"codigo": self.codigo, "nombre": self.nombre, "cedula": self.cedula, "cargo": self.cargo, "departamento": self.departamento, "sueldo": self.sueldo}