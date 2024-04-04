lexer grammar shellLexer;

// Whitespace
WS : [ \t\r\n]+ -> skip;

// Keywords
PIPE : '|';
SEMICOLON : ';';

// Command substitution
SINGLE_QUOTED : '\'' (~['\n])* '\'';
DOUBLE_QUOTED : '"' (~["\n`] | '\\' .)* '"';
BACKQUOTED : '`' (~[`\n] | '\\' .)* '`';

// Redirection
REDIRECT_INPUT : '<';
REDIRECT_OUTPUT : '>';

// Call command
//UNQUOTED : UNQUOTED;

// Unquoted text
UNQUOTED : ~[\n|<> ; \t`]+;

fragment BACKSLASH : '\\';
fragment LETTER: [a-zA-Z];
fragment UNSAFE: '_';