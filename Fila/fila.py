from ListaLigada.no import No
class Fila:
  def __init__(self):
        self._primeiro: No = None
        self._ultimo: No = None
        self._tamanho = 0

  def enqueue(self, item): #Enfileirar
        """ Adiciona no fim da lista """

        novo_no = No(item)
        if self.vazia():
            self._primeiro = novo_no
            self._ultimo = novo_no
        else:
            self._ultimo.proximo = novo_no
            self._ultimo = novo_no
        self._tamanho += 1

  def dequeue(self): #Desenfileirar
        """ Remove o primeiro item da lista e o retorna """

        if self.vazia():
            return None
        
        item_removido = self._primeiro.item
        self._primeiro = self._primeiro.proximo
        self._tamanho -= 1
        if self.vazia():
            self._ultimo = None

        return item_removido
    
  def peek(self): #Primeiro No(item)
        if self.vazia():
          return None
        return self._elementos._primeiro.item
    
  def vazia(self):
        return self._tamanho == 0

  def tamanho(self):
        return self._tamanho
  
