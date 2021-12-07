[GitHub - sweethuman/flcd](https://github.com/sweethuman/flcd)

# FA Documentation

How to write the input files for FiniteAutomaton Class

```ebnf
letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z" ;
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
operator = "-" | "+";
character = letter | digit | operator;
separator = ";";
newline = "\n";
states = "states",{separator,letter};
alphabet = "alphabet",{separator,character};
transitions = "transitions",{separator,transition}
transition = letter,",",character,",",letter
initial state = "initialState",separator,letter
final state = "finalState",{separator,letter}
program = states,newline,alphabet,newline,transitions,newline,
          initial state,newline,final state
```

g2.txt is missing the `||` operator because it conflicts with the `|` sign in grammar parsing. will fix later