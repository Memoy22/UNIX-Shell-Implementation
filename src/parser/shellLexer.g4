lexer grammar shellLexer;

fragment SINGLE_QUOTE: '\'';
fragment DOUBLE_QUOTE: '"';
fragment BACK_QUOTE: '`';

WS: [ \t\n]+ -> skip;

PIPE: '|';
SEMICOLON: ';';
REDIRECT_INPUT: '<';
REDIRECT_OUTPUT: '>';

UNQUOTED : ~[\n'"`<>;|\t ]+;

SQ_START: SINGLE_QUOTE -> pushMode(SINGLE_QUOTE_MODE);
DQ_START: DOUBLE_QUOTE -> pushMode(DOUBLE_QUOTE_MODE);
BQ_START: BACK_QUOTE -> pushMode(BACK_QUOTE_MODE);

mode SINGLE_QUOTE_MODE;
SQ_CONTENT: ~[\n']+;
SQ_END: SINGLE_QUOTE -> popMode;

mode DOUBLE_QUOTE_MODE;
DQ_CONTENT: ~[\n"`]+;
BQ_START_IN_DQ: BACK_QUOTE -> pushMode(BACK_QUOTE_MODE);
DQ_END: DOUBLE_QUOTE -> popMode;

mode BACK_QUOTE_MODE;
BQ_CONTENT: ~[\n`]+;
BQ_END: BACK_QUOTE -> popMode;