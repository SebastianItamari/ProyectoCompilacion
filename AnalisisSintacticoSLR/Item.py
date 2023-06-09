#standard library imports
from collections import OrderedDict
from copy import *

#local application imports
from Gramática.GLC import *


class Item:
    def __init__(self,name,originalGrammar,grammar):
        self.name = name
        self.originalGrammar = originalGrammar
        self.nonClosingGrammar = deepcopy(grammar)
        self.grammar = deepcopy(grammar)

    def closing(self,added):
        aux = self.partial_Closing(added)
        if(len(aux) > 0):
            for key in aux:
                self.addProductions(key)
            self.closing(added)

    def partial_Closing(self, added):
        toAdd = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            if (elementList[index + 1] in self.originalGrammar.productions) and (not elementList[index + 1] in added):
                                toAdd.append(elementList[index + 1])
                                added.append(elementList[index + 1])
        return self.remove_duplicates(toAdd)

    def addProductions(self,key):
        for prod in self.originalGrammar.productions[key]:
            self.grammar.add_production(key, ". " + prod)
         
    def elements(self):
        elements = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            elements.append(elementList[index + 1])
        return self.remove_duplicates(elements)

    def remove_duplicates(self, lst):
        return list(OrderedDict.fromkeys(lst))