from abc import ABC, abstractmethod


class Conta(ABC):
    def __call__(self, numero, iof, ir, valor_investido, taxa_rendimento):
        self.numero = numero
        self.iof = iof
        self.ir = ir
        self.valor_investido = valor_investido
        self.taxa = taxa_rendimento

    @abstractmethod
    def calc_rendiento(self):
        pass
