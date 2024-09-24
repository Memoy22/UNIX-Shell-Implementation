lexer grammar shellLexer;

fragment SQ: '\'';
fragment DQ: '"';
fragment BQ: '`';

WS: [ \t\n]+ -> skip;

PIPE: '|';
SEMICOLON: ';';
REDIRECT_INPUT: '<';
REDIRECT_OUTPUT: '>';

UNQUOTED : ~[\n'"`<>;|\t ]+;

SQ_START: SQ -> pushMode(SINGLE_QUOTE_MODE);
DQ_START: DQ -> pushMode(DOUBLE_QUOTE_MODE);
BQ_START: BQ -> pushMode(BACK_QUOTE_MODE);

mode SINGLE_QUOTE_MODE;
SQ_CONTENT: ~[\n']+;
SQ_END: SQ -> popMode;

mode DOUBLE_QUOTE_MODE;
DQ_CONTENT: ~[\n"`]+;
BQ_START_IN_DQ: BQ -> pushMode(BACK_QUOTE_MODE);
DQ_END: DQ -> popMode;

mode BACK_QUOTE_MODE;
BQ_CONTENT: ~[\n`]+;
BQ_END: BQ -> popMode;