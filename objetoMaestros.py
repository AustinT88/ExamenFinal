from Maestros import Maestros

listaMaestro=[]

for i in range(2):
    Doc1 = Maestros()
    Doc1.setNombre(input("Ingrese el nombre: " ))
    Doc1.setApellido(input("Ingrese el apellido: "))
    Doc1.setSalario(int(input("Ingrese el salario: ")))
    Doc1.setBono(int(input("Ingrese el Bono:  ")))
    listaMaestro.append(Doc1)

for doc in listaMaestro:
    print("Los datos guardados son ")
    print(doc.getNombre())
    print(doc.getApellido())
    print(doc.getSalario())
    print(doc.getBono())
    print(doc.getSueldoTotal())