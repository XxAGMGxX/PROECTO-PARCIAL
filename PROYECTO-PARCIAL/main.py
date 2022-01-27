from cargo import Cargo
from departamento import Departamento
from empleados import Empleado
from helpers import Helper

import os

def buscarcargo(cod):
  car = 0
  for pos in range (0,len(Cargo.cargos)):
    cargo = Cargo.cargos[pos]
    if cargo["cargo"] == cod:
      car = cargo["cargo"]
      break
  return car

def buscardept(dep):
  dept = 0
  for pos in range (0,len(Departamento.departamentos)):
    depar = Departamento.departamentos[pos]
    if depar["nombre"] == dep:
      dept = depar["nombre"]
      break
  return dept

helper = Helper()
lista = ["1) Cargo ","2) Departamento ","3) Empleados ","4) Salir"]
opcion = ""

while opcion !="4":
  os.system("cls")
  opcion =helper.menu(lista, "Menú Ficha Personal")
  os.system("cls")
  if opcion == "1":
    opc1=""
    while opc1 !=3:
      os.system("cls")
      print("■"*20,"Mantenimiento De Cargos","■"*20)
      opc1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Cargo")
      os.system("cls")
      if opc1 == "1":
        print("■"*20,"Ingreso De Cargos","■"*20)
        nombre = input("Nombre del cargo: ")
        val = len(nombre)
        while not val >2 and val <=20:
          nombre = input("Nombre del cargo: ")
          val = len(nombre)
        crg = Cargo(nombre)
        carg = crg.registro()
        Cargo.cargos.append(carg)
        input("\n"
          "Datos ingresados correctamente, presiona una tecla para continuar:)")
      elif opc1 == "2":
        print("■"*20,"Lista De Cargos","■"*20)
        print("Codigo"," "*5,"Descripcion"," ")
        for crg in Cargo.cargos:
          codi = crg ["codigo"]
          desc= crg ["cargo"]
          codig = buscarcargo(desc)
          print(" "*2,codi," "*8,codig)
        print("■"*59)
        input("\n"
         "Presione una tecla para continuar   :")
      elif opc1 == "3":
        input("Espere porfavor " 
        "\n" "Presione una tecla para continuar   :")
        break

  elif opcion =="2":
    os.system("cls")
    opc1 = ""
    while opc1 !=3:
      os.system("cls")
      print("■"*20,"Mantenimiento De Departamentos","■"*20)
      opc1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Departamento")
      os.system("cls")
      if opc1 == "1":
        print("■"*20,"Ingreso De Departamentos","■"*20)
        nombre = input("Nombre del departamento: ")
        val = len(nombre)
        while not val >5 and val <=20:
          nombre = input("Nombre del departamento: ")
          val = len(nombre)
        dpt = Departamento(nombre)
        depa = dpt.registro()
        Departamento.departamentos.append(depa)
        input("\n"
          "Datos ingresados correctamente, presiona una tecla para continuar:)")
      elif opc1 == "2":
        print("■"*20,"Listado De Departamentos","■"*20)
        print("Departamento"," "*5,"Nombre"," ")
        for dpt in Departamento.departamentos:
          depta = dpt ["departamento"]
          dnom= dpt ["nombre"]
          nomd = buscardept(dnom)
          print(" "*4,depta," "*8,nomd)
        print("■"*66)
        input(
        "\n" "Presione una tecla para continuar  :")
      elif opc1 == "3":
        input("Espere porfavor " 
        "\n" "Presione una tecla para continuar   ")
        break
        
  elif opcion == "3":
    os.system("cls")
    opc1 = ""
    while opc1 !=3:
      os.system("cls")
      print("■"*20,"Mantenimiento De Empleados","■"*20)
      opc1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Empleados")
      os.system("cls")
      if opc1 == "1":
        print("■"*20,"Ingreso De Empleados","■"*20)
        nombre= input("Nombre del empleado: ")
        val = len(nombre)
        while not val >= 3 and val <=20:
          nombre = input("Nombre del empleado: ")
          val = len(nombre)
        cedula= input("Cédula del Empleado: ")
        val = len(cedula)
        while val != 10:
          cedula = input("Cédula del Empleado: ")
          val = len(cedula)
        codCargo= input("Cargo del Empleado: ")
        car = buscarcargo(codCargo)
        while car != codCargo:
          codCargo= input("Cargo del Empleado: ")
          car = buscarcargo(codCargo)
        codDepartamento= input("Departamento del Empleado: ")
        dept = buscardept(codDepartamento)
        while dept != codDepartamento:
          codDepartamento= input("Departamento del Empleado: ")
          dept = buscardept(codDepartamento)
        sueldo= float(input("Sueldo del Empleado: "))  
        while sueldo %1 == 0:
          sueldo= float(input("Sueldo del Empleado: "))  
        empl = Empleado(nombre,cedula,codCargo,codDepartamento,sueldo)
        empleado = empl.registro()
        Empleado.Empleados.append(empleado)
        input("\n"
        "Datos ingresados satisfactoriamente, presione una tecla para continuar...")
      elif opc1 == "2":
        print("■"*35,"Listado De Empleados","■"*35)
        print("Codigo"," "*6,"Nombre"," "*6,"Cedula"," "*6,"Cargo"," "*6,"Departamento"," "*6,"Sueldo")
        for empl in Empleado.Empleados:
          codigo = empl["codigo"]
          desno=empl["nombre"]
          ced =empl["cedula"] 
          cgo =empl["cargo"]
          bcg = buscarcargo(cgo)
          detm = empl["departamento"]
          bdp = buscardept(detm)
          suel=empl["sueldo"]
          print(" "*2,codigo," "*8,desno," "*(10-len(desno)),ced," "*(14-len(ced)),bcg," "*(11-len(bcg)), bdp," "*(18-len(bdp)), suel)
        print("■"*92)
        input("\n"
          "Presione una tecla para continuar...")
      elif opc1 == "3":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break
  elif opcion == "4":
    print("GRACIAS POR SU VISITA!!!")