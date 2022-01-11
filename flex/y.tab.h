/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    AND = 258,                     /* AND  */
    ARRAY = 259,                   /* ARRAY  */
    ELSE = 260,                    /* ELSE  */
    BEGINN = 261,                  /* BEGINN  */
    FOR = 262,                     /* FOR  */
    IF = 263,                      /* IF  */
    NUMBER = 264,                  /* NUMBER  */
    OR = 265,                      /* OR  */
    READ = 266,                    /* READ  */
    WHILE = 267,                   /* WHILE  */
    XOR = 268,                     /* XOR  */
    PRINT = 269,                   /* PRINT  */
    TYPE = 270,                    /* TYPE  */
    STRING = 271,                  /* STRING  */
    ID = 272,                      /* ID  */
    ATRIB = 273,                   /* ATRIB  */
    EQ = 274,                      /* EQ  */
    NE = 275,                      /* NE  */
    LE = 276,                      /* LE  */
    GE = 277,                      /* GE  */
    LT = 278,                      /* LT  */
    GT = 279,                      /* GT  */
    NOT = 280,                     /* NOT  */
    DOT = 281,                     /* DOT  */
    PLUS = 282,                    /* PLUS  */
    MINUS = 283,                   /* MINUS  */
    DIV = 284,                     /* DIV  */
    MODULO = 285,                  /* MODULO  */
    MUL = 286,                     /* MUL  */
    OPEN_CURLY_BRACKET = 287,      /* OPEN_CURLY_BRACKET  */
    CLOSED_CURLY_BRACKET = 288,    /* CLOSED_CURLY_BRACKET  */
    OPEN_ROUND_BRACKET = 289,      /* OPEN_ROUND_BRACKET  */
    CLOSED_ROUND_BRACKET = 290,    /* CLOSED_ROUND_BRACKET  */
    OPEN_RIGHT_BRACKET = 291,      /* OPEN_RIGHT_BRACKET  */
    CLOSED_RIGHT_BRACKET = 292,    /* CLOSED_RIGHT_BRACKET  */
    COMMA = 293,                   /* COMMA  */
    SEMI_COLON = 294,              /* SEMI_COLON  */
    COLON = 295,                   /* COLON  */
    SPACE = 296                    /* SPACE  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define AND 258
#define ARRAY 259
#define ELSE 260
#define BEGINN 261
#define FOR 262
#define IF 263
#define NUMBER 264
#define OR 265
#define READ 266
#define WHILE 267
#define XOR 268
#define PRINT 269
#define TYPE 270
#define STRING 271
#define ID 272
#define ATRIB 273
#define EQ 274
#define NE 275
#define LE 276
#define GE 277
#define LT 278
#define GT 279
#define NOT 280
#define DOT 281
#define PLUS 282
#define MINUS 283
#define DIV 284
#define MODULO 285
#define MUL 286
#define OPEN_CURLY_BRACKET 287
#define CLOSED_CURLY_BRACKET 288
#define OPEN_ROUND_BRACKET 289
#define CLOSED_ROUND_BRACKET 290
#define OPEN_RIGHT_BRACKET 291
#define CLOSED_RIGHT_BRACKET 292
#define COMMA 293
#define SEMI_COLON 294
#define COLON 295
#define SPACE 296

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
