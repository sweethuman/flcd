from typing import Set, Dict, List

from ordered_set import OrderedSet


class Grammar:
    non_terminals: OrderedSet[str]
    terminals: OrderedSet[str]
    productions: Dict[str, List[List[str]]]
    starting_symbol: str

    def __init__(self, non_terminals, terminals, productions, starting_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.starting_symbol = starting_symbol

    @staticmethod
    def parseFile(filename):
        with open(filename, "r") as file:
            non_terminals = OrderedSet([nt.strip() for nt in file.readline().strip().split(' ')])
            terminals = OrderedSet([nt.strip() for nt in file.readline().strip().split(' ')])
            starting_symbol = file.readline().strip()
            productions = {}
            for line in file:
                symbol, rules = [el.strip() for el in line.strip().split('->')]
                rules = OrderedSet([rule.strip() for rule in rules.split('|')])
                # validation
                for rule in rules:
                    for res in rule.split(' '):
                        if res not in terminals and res not in non_terminals:
                            raise SyntaxError(
                                "Rule element not present in either terminals or non terminals element:" + res)
                # if no error add to productions
                productions[symbol] = [rule.split(' ') for rule in rules]
            return Grammar(non_terminals, terminals, productions, starting_symbol)

    def getNonTerminals(self):
        return list(self.non_terminals)

    def getTerminals(self):
        return list(self.terminals)

    def getProductions(self):
        return self.productions

    def getStartingSymbol(self):
        return self.starting_symbol
