from datetime import datetime


class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        proximo = f', {self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'


class DoublyLinkedList:
    def __init__(self, tipo=None):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tipo = tipo

    def __str__(self):
        value_list = '['
        perc = self.inicio
        while perc.proximo:
            value_list += f' {perc.valor}, '
            perc = perc.proximo
        value_list += f'{perc.valor} ]'
        return value_list

    def __len__(self):
        return self.tamanho

    def _percorrer(self, perc, count, proximo):
        if proximo:
            for i in range(count):
                perc = perc.proximo
        else:
            for i in range(count):
                perc = perc.anterior
        return perc

    def _get_perc_index(self, index):
        metade_lista = int(self.tamanho - 1) / 2
        if index <= metade_lista:
            return self._percorrer(self.inicio, index, proximo=True)
        else:
            new_index = (self.tamanho - 1) - index
            return self._percorrer(self.final, new_index, proximo=False)

    def _get_perc_valor(self, valor):
        perc_inicio = self.inicio
        perc_final = self.final
        metade = int(self.tamanho - 1) / 2
        count = 0
        # NÃO TÁ PERCORRENDO DIRETO
        while perc_inicio.valor is not valor and perc_final.valor is not valor:
            perc_inicio = perc_inicio.proximo
            perc_final = perc_final.anterior
            count += 1
            if perc_inicio.valor == valor:
                return count
            elif perc_final.valor == valor:
                return (self.tamanho - 1) - count
            if count > metade:
                raise ValueError("Item com este valor não encontrado")

    def get_valor(self, index):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index < 0 or index >= self.tamanho:
            raise IndexError('Index inválido')

        if index == 0:
            return self.inicio.valor
        if index == self.tamanho - 1:
            return self.final.valor
        else:
            perc = self._get_perc_index(index)
            return perc.valor

    def get_index(self, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')

        if self.inicio.valor == valor:
            return 0
        elif self.final.valor == valor:
            return self.tamanho - 1
        else:
            return self._get_perc_valor(valor)

    def adicionar(self, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        no = _No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.final = no
        else:
            aux = self.final
            self.final = no
            self.final.anterior = aux
            aux.proximo = self.final
        self.tamanho += 1

    def inserir(self, index, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if index < 0 or index >= (self.tamanho + 1):
            raise IndexError('Index inválido')

        if index == self.tamanho:
            self.adicionar(valor)
            return
        no = _No(valor)
        if index == 0:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no
        else:
            perc = self._get_perc_index(index - 1)
            no.proximo = perc.proximo
            perc.proximo.anterior = no
            perc.proximo = no
            no.anterior = perc
        self.tamanho += 1

    def editar_item(self, index, novo_valor):
        if self.tipo and type(novo_valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index < 0 or index >= self.tamanho:
            raise IndexError('Index inválido')

        if index == 0:
            self.inicio.valor = novo_valor
        elif index == self.tamanho - 1:
            self.final.valor = novo_valor
        else:
            perc = self._get_perc_index(index)
            perc.valor = novo_valor

    def remover_item(self, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')

        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
        elif self.final.valor == valor:
            self.final = self.final.anterior
            self.final.proximo = None
        else:
            count = self._get_perc_valor(valor)
            perc = self._get_perc_index(count - 1)
            aux = perc.proximo.proximo
            perc.proximo = perc.proximo.proximo
            aux.anterior = aux.anterior.anterior
        self.tamanho -= 1

    def remover_index(self, index):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index < 0 or index >= self.tamanho:
            raise IndexError('Index inválido')

        if index == 0:
            self.inicio = self.inicio.proximo
        elif index == self.tamanho - 1:
            self.final = self.final.anterior
            self.final.proximo = None
        else:
            perc = self._get_perc_index(index - 1)
            aux = perc.proximo.proximo
            perc.proximo = perc.proximo.proximo
            aux.anterior = aux.anterior.anterior
        self.tamanho -= 1

    def buscar_valores_repetidos(self):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')

        lista_string = ""
        valores_repetidos = "Valores repetidos: "
        perc_inicio = self.inicio
        perc_final = self.final
        count = 0
        metade = int(self.tamanho - 1) / 2
        while metade > count:
            if lista_string.__contains__(f' {str(perc_inicio.valor)} ') is False:
                lista_string += f' {str(perc_inicio.valor)} '
            else:
                if valores_repetidos.__contains__(f' {str(perc_inicio.valor)} ') is False:
                    valores_repetidos += f' {str(perc_inicio.valor)} '

            if lista_string.__contains__(f' {str(perc_final.valor)} ') is False:
                lista_string += f' {str(perc_final.valor)} '
            else:
                if valores_repetidos.__contains__(f' {str(perc_final.valor)} ') is False:
                    valores_repetidos += f' {str(perc_final.valor)} '

            perc_inicio = perc_inicio.proximo
            perc_final = perc_final.anterior
            count += 1
        if valores_repetidos == "Valores repetidos: ":
            return "Sem valores repetidos nesta lista"
        else:
            return valores_repetidos

    def ordernar(self, crescente=True):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')

        if crescente is True:
            count = 1
            for i in range(self.tamanho - 1):
                perc = self._get_perc_index(count)
                aux = self._get_perc_index(i)
                while perc:
                    if aux.valor > perc.valor:
                        valor_aux = aux.valor
                        aux.valor = perc.valor
                        perc.valor = valor_aux
                    perc = perc.proximo
                count += 1
        else:
            count = 1
            for i in range(self.tamanho - 1):
                perc = self._get_perc_index(count)
                aux = self._get_perc_index(i)
                while perc:
                    if aux.valor < perc.valor:
                        valor_aux = aux.valor
                        aux.valor = perc.valor
                        perc.valor = valor_aux
                    perc = perc.proximo
                count += 1
