from datetime import datetime


class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __str__(self):
        proximo = f', {self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'


class ListaSimples:
    def __init__(self, tipo=None):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tipo = tipo

    def __str__(self):
        value_list = '[ '
        perc = self.inicio
        while perc.proximo:
            value_list += f'{perc.valor}, '
            perc = perc.proximo
        value_list += f'{perc.valor} ]'
        return value_list

    def __len__(self):
        return self.tamanho

    def __getitem__(self, item):
        return self.get_valor(item)

    def _get_perc(self, index):
        perc = self.inicio
        count = 0
        while count != index:
            perc = perc.proximo
            count += 1
        return perc

    def adicionar(self, valor):
        """
        Adiciona um elemento ao fim da lista
        :param valor:
        :return:
        """
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        no = _No(valor)
        if not self.final:
            self.inicio = no
            self.final = no
        else:
            self.final.proximo = no
            self.final = no
        self.tamanho += 1

    def inserir(self, index, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if index < 0:
            raise IndexError('Index inválido')

        if index >= self.tamanho:
            self.adicionar(valor)
            return
        no = _No(valor)
        if index == 0:
            no.proximo = self.inicio
            self.inicio = no
        else:
            perc = self._get_perc(index - 1)
            no.proximo = perc.proximo
            perc.proximo = no
        self.tamanho += 1

    def get_valor(self, index):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index >= self.tamanho or index < 0:
            raise IndexError('Index inválido')

        if index == self.tamanho - 1:
            return self.final.valor
        elif index == 0:
            return self.inicio.valor
        else:
            perc = self._get_perc(index)
            return perc.valor

    def editar_item(self, index, novo_valor):
        if self.tipo and type(novo_valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index > self.tamanho or index < 0:
            raise IndexError('Index inválido')

        if index == self.tamanho - 1:
            self.final.valor = novo_valor
        elif index == 0:
            self.inicio.valor = novo_valor
        else:
            perc = self._get_perc(index)
            perc.valor = novo_valor

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
            perc = self.inicio
            count = 0
            while perc.valor != valor:
                perc = perc.proximo
                count += 1
                if perc is None:
                    raise ValueError("Nenhum index com este valor foi encontrado")
            return count

    def remover_item(self, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')

        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
        elif self.final.valor == valor:
            perc = self._get_perc(self.tamanho - 2)
            perc.proximo = None
            self.final = perc
        else:
            count = 0
            aux = self.inicio
            while aux.valor != valor:
                aux = aux.proximo
                count += 1
                if aux is None:
                    raise ValueError("Item com este valor não encontrado")
            perc = self._get_perc(count - 1)
            perc.proximo = aux.proximo
        self.tamanho -= 1

    def remover_index(self, index):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        if index >= self.tamanho or index < 0:
            raise IndexError('Index inválido')

        if index == 0:
            self.inicio = self.inicio.proximo
        elif index == self.tamanho - 1:
            perc = self._get_perc(self.tamanho - 2)
            perc.proximo = None
            self.final = perc
        else:
            perc = self._get_perc(index - 1)
            perc.proximo = perc.proximo.proximo
        self.tamanho -= 1

    def buscar_valores_repetidos(self):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        lista_string = ""
        valores_repetidos = "Valores repetidos: "
        perc = self.inicio
        while perc:
            if lista_string.__contains__(f' {str(perc.valor)} ') is False:
                lista_string += f' {str(perc.valor)} '
            else:
                if valores_repetidos.__contains__(f' {str(perc.valor)} ') is False:
                    valores_repetidos += f' {str(perc.valor)} '
            perc = perc.proximo
        if valores_repetidos == "Valores repetidos: ":
            return "Sem valores repetidos nesta lista"
        else:
            return valores_repetidos

    # Método selecionado: BublleSort
    def ordernar(self, crescente=True):
        if self.tamanho == 0:
            raise IndexError('Não existe elementos na lista')
        count = 0
        if crescente is True:
            while count != self.tamanho:
                perc = self.inicio
                while perc.proximo:
                    if perc.valor > perc.proximo.valor:
                        aux_perc_valor = perc.proximo.valor
                        perc.proximo.valor = perc.valor
                        perc.valor = aux_perc_valor
                    perc = perc.proximo
                count += 1
        else:
            while count != self.tamanho:
                perc = self.inicio
                while perc.proximo:
                    if perc.valor < perc.proximo.valor:
                        aux_perc_valor = perc.proximo.valor
                        perc.proximo.valor = perc.valor
                        perc.valor = aux_perc_valor
                    perc = perc.proximo
                count += 1
