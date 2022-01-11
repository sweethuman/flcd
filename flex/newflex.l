
%{
#include <math.h>
#include <string.h>
#include <stdio.h>
#include "y.tab.h"
%}

%option noyywrap
%option caseless

DIGIT 		[0-9]+|(-[1-9][0-9]*)
ID 		[a-z][a-z0-9]*
NOTID   [0-9][a-z0-9]*
TYPE    (number|string)
STRING  '.*'

%%

"if" {return IF; }
"and" {return AND; }
"for" {return FOR; }
"else" {return ELSE; }
"begin" {return BEGINN; }
"or" {return OR; }
"read" {return READ; }
"while" {return WHILE; }
"xor" {return XOR; }
"array" {return ARRAY; }
"print" {return PRINT; }

{TYPE} {return TYPE; }
{STRING} {return STRING; }

{DIGIT} 	{return NUMBER; }

{ID} {return ID; }
":"	{return COLON;}
";"	{ return SEMI_COLON;}
","	{return COMMA;}
"."	{ return DOT;}
"{"	{return OPEN_CURLY_BRACKET;}
"}"	{ return CLOSED_CURLY_BRACKET;}
"("	{return OPEN_ROUND_BRACKET;}
")"	{ return CLOSED_ROUND_BRACKET;}
"["	{return OPEN_RIGHT_BRACKET;}
"]"	{return CLOSED_RIGHT_BRACKET;}


"+"	{return PLUS;}
"-"	{return MINUS;}
"*"	{return MUL;}
"/"	{return DIV;}
"%"	{return MODULO;}
"<"	{return LT;}
">"	{return GT;}
"<=" {return LE;}
">=" {return GE;}
"!=" {return NE;}
"==" {return EQ;}
"="	{return ATRIB;}
"!"	{return NOT;}

"{"[^}\n]*"}" 		/* eat up one-line comments */

[ \t\n]+ 		/* eat up whitespace */

.|{NOTID} {return -1; }
