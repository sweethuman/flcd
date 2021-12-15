import pprint
from typing import Literal, List, TextIO

from myparser.grammar import Grammar
from domain.language_symbols import symbols
import graphviz


class Node:
    def __init__(self, value, index):
        self.index = index
        self.father = -1
        self.sibling = -1
        self.value = value
        self.production = -1

    def __str__(self):
        return str(self.value) + " " + str(self.father) + " " + str(self.sibling)


class ParserRecursiveDescent:
    grammar: Grammar
    state: Literal["q", "b", "f", "e"]
    tree: List[Node]
    file: TextIO

    def __init__(self, grammar):
        self.grammar = grammar
        self.work = []
        self.input = []
        self.state = "q"
        self.index = 0
        self.iteration = 0
        self.symbols = symbols
        self.tree = []
        self.words = []
        self.debug = True
        self.file = open("parser.debug.txt", "w")
        self.file.seek(0)

    def expand(self):
        # when top of input non terminal
        non_terminal = self.input.pop(0)
        self.work.append((non_terminal, 0))

        # this probably shouldn't always be 0 but we will see, kinda fucked
        a = list(self.grammar.getProductions()[non_terminal])[0]

        self.input = a + self.input
        if self.debug:
            self.print_parser_step("expand")

    def advance(self):
        # when top of input terminal
        self.work.append(self.input.pop(0))
        self.index += 1
        if self.debug:
            self.print_parser_step("advance")

    def momentary_insuccess(self):
        # when else fails set state to back
        self.state = "b"
        if self.debug:
            self.print_parser_step("momentary_insuccess")

    def back(self):
        # only used for terminals in work list
        # when state is "b" we restore the input
        self.input = [self.work.pop()] + self.input
        self.index -= 1
        if self.debug:
            self.print_parser_step("back")

    def success(self):
        # when conditions are met set state to success
        self.state = "f"
        self.index += 1
        if self.debug:
            self.print_parser_step("success")

    def another_try(self):

        (non_terminal, last_prod_index) = self.work.pop()
        productions = self.grammar.getProductions()[non_terminal]

        if len(productions) - 1 > last_prod_index:
            self.state = "q"
            self.work.append((non_terminal, last_prod_index + 1))

            # remove previous production and add current production
            for i in productions[last_prod_index]:
                self.input.pop(0)
            aux = productions[last_prod_index + 1]
            self.input = aux + self.input

        else:
            for i in productions[last_prod_index]:
                self.input.pop(0)
            self.input = [non_terminal] + self.input

        if self.debug:
            self.print_parser_step("another_try")

    def check_word_length(self, w):
        if len(w) > self.index:
            return self.input[0] == w[self.index]
        return False

    def run(self, w):
        self.words = w
        self.state = "q"
        self.index = 0
        self.work = []
        self.input = [self.grammar.getStartingSymbol()]
        while self.state != "f" and self.state != "e":
            if (len(self.input) == 0 and self.index != len(self.words)) or (self.state == "b" and len(self.work) == 0):
                self.state = "e"
            if self.state == "q":
                if len(self.input) == 0 and self.index == len(self.words):
                    self.success()
                else:
                    if self.input[0] in self.grammar.getNonTerminals():
                        self.expand()
                    elif self.input[0] in self.grammar.getTerminals() and self.check_word_length(self.words):
                        self.advance()
                    else:
                        self.momentary_insuccess()
            elif self.state == "b":
                if self.work[len(self.work) - 1] in self.grammar.getTerminals():
                    self.back()
                # anotherTry
                else:
                    self.another_try()

        if self.state == "e":
            print("ERROR")
        else:
            print("Sequence accepted")
            print(self.work, self.input, self.index)

    def print_parser_step(self, step):
        pp = pprint.PrettyPrinter(indent=2, stream=self.file)
        pp.pprint("~~~~~~~~~~~~")
        pp.pprint(f"Current step: {step}")
        pp.pprint(f"Iteration: {self.iteration}")
        self.iteration += 1
        pp.pprint(f"Current state: {self.state}")
        pp.pprint(f'Current index: {self.index} {self.words[self.index]}')
        pp.pprint("Work:")
        pp.pprint(self.work)
        pp.pprint("Input:")
        pp.pprint(self.input)
        pp.pprint("Words:")
        pp.pprint(self.words)

    def parse_tree(self, work):
        father = -1

        for index in range(0, len(work)):
            if type(work[index]) == tuple:
                self.tree.append(Node(work[index][0], index))
                self.tree[index].production = work[index][1]
            else:
                self.tree.append(Node(work[index], index))

        for index in range(0, len(work)):
            if type(work[index]) == tuple:
                self.tree[index].father = father
                father = index
                lengthProduction = len(self.grammar.getProductions()[work[index][0]][work[index][1]])
                vectorIndex = []
                for i in range(1, lengthProduction + 1):
                    vectorIndex.append(index + i)
                for i in range(0, lengthProduction):
                    if self.tree[vectorIndex[i]].production != -1:  # if it is a nonTerminal, compute offset
                        offset = self.get_production_offset(vectorIndex[i])
                        for j in range(i + 1, lengthProduction):
                            vectorIndex[j] += offset
                for i in range(0, lengthProduction - 1):
                    self.tree[vectorIndex[i]].sibling = vectorIndex[i + 1]
            else:
                self.tree[index].father = father
                father = -1

    def get_production_offset(self, index):
        production = self.grammar.getProductions()[self.work[index][0]][self.work[index][1]]
        lengthOfProduction = len(production)
        offset = lengthOfProduction
        for i in range(1, lengthOfProduction + 1):
            if type(self.work[index + i]) == tuple:
                offset += self.get_production_offset(index + i)
        return offset

    def write_tree_to_file(self, filename):
        graph = graphviz.Digraph()
        file = open(filename + ".out", "w")
        file.write("index | value | father | sibling\n")

        for index in range(0, len(self.work)):
            node = self.tree[index]
            if node.production != -1:
                graph.node(str(index),
                           label=f"<{index} {node.value}<BR /><FONT POINT-SIZE=\"10\">{node.production}</FONT>>")
            else:
                graph.node(str(index), label=str(index) + " " + str(node.value))
            if node.father != -1:
                graph.edge(str(node.father), str(index))
            if node.father == -1:
                try:
                    currnode = node
                    while currnode.father == -1:
                        currnode = next(x for x in self.tree if x.sibling == currnode.index)
                    if currnode.father != -1 and currnode != node:
                        graph.edge(str(currnode.father), str(index), arrowhead="empty")
                except StopIteration:
                    print("For " + str(index) + " " + str(node) + " indirect father not found.")
            # if node.sibling != -1:
            #     graph.edge(str(index), str(node.sibling), arrowhead="invdot")
            file.write(str(index) + " " + str(node) + "\n")
            print(index, " ", str(node))
        file.close()
        graph.render(filename=filename + ".gv", format="png")


if __name__ == "__main__":
    with open("grammar.debug.txt", "w") as f:
        f.seek(0)
        pp = pprint.PrettyPrinter(indent=2, stream=f)
        gram = Grammar.parseFile("g1.txt")
        pp.pprint(gram.getNonTerminals())
        pp.pprint(gram.getTerminals())
        pp.pprint(gram.getStartingSymbol())
        pp.pprint(gram.getProductions())
        parser = ParserRecursiveDescent(gram)
        parser.run(['a', 'c', 'b', 'a', 'c', 'b', 'a', 'a', 'c', 'b', 'c'])
        parser.parse_tree(parser.work)
        parser.write_tree_to_file("g1")
