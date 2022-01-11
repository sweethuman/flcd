%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define YYDEBUG 1
%}

%token AND
%token ARRAY
%token ELSE
%token BEGINN
%token FOR
%token IF
%token NUMBER
%token OR
%token READ
%token WHILE
%token XOR
%token PRINT

%token TYPE
%token STRING

%token ID

%token ATRIB
%token EQ
%token NE
%token LE
%token GE
%token LT
%token GT
%token NOT

%token DOT

%left '+' '-' '*' '/'

%token PLUS
%token MINUS
%token DIV
%token MODULO
%token MUL

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET

%token COMMA
%token SEMI_COLON
%token COLON
%token SPACE

%start program

%%

program : BEGINN cmpdstmt
	;
declaration :  TYPE ID | array_declaration
	    ;
array_declaration : TYPE ARRAY OPEN_RIGHT_BRACKET NUMBER CLOSED_RIGHT_BRACKET ID
	;
cmpdstmt : OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET
	;
stmtlist : stmt SEMI_COLON | stmt SEMI_COLON stmtlist
	;
stmt : simple_stmt | struct_stmt
	;
simple_stmt : assign_stmt | io_stmt | declaration
	;
assign_stmt : ID ATRIB expression
	;
expression : term | expression operation term
	;
condition : expression GT expression |
	 expression GE expression |
	 expression LT expression |
	 expression LE expression |
	 expression EQ expression |
	 expression NE expression
	  ;
term : ID | NUMBER
	;
operation : PLUS | DIV | MODULO | MINUS | MUL
	;
io_stmt : READ OPEN_ROUND_BRACKET ID CLOSED_ROUND_BRACKET | PRINT OPEN_ROUND_BRACKET ID CLOSED_ROUND_BRACKET
	;
struct_stmt : cmpdstmt | ifstmt | whilestmt
	;
ifstmt : IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET cmpdstmt
	;
whilestmt : WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET cmpdstmt
	;
%%
yyerror(char *s)
{
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}
