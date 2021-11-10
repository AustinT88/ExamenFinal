from Personal import Personal
class Maestros(Personal):
    dpi=0
    curso=""
    salario=0
    bono=0

    def getDpi(self):
        return self.dpi
    def setDpi(self, dpi):
        self.dpi = dpi

    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
        self.curso=curso

    def getSalario(self):
        return self.salario
    def setSalario(self, salario):
        self.salario=salario

    def getBono(self):
        return self.bono
    def setBono(self, bono):
        self.bono=bono

    def getSueldoTotal(self):
        return self.salario + self.bono