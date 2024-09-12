parser grammar shellParser;

options {
  tokenVocab=ShellLexer;
}

cmdline : commands? EOF;
commands: command (SEMICOLON command)*;
command: pipe;
pipe: call (PIPE call)*;

call: WS? (redirection WS)* argument (WS atom)* WS?;
atom: argument | redirection;
argument: (quoted | unquoted)+;
redirection: REDIRECT_INPUT WS? argument | REDIRECT_OUTPUT WS? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;
unquoted: UNQUOTED;

singleQuoted: SINGLE_QUOTE SQ_CONTENT SINGLE_QUOTE;
doubleQuoted: DOUBLE_QUOTE DQ_CONTENT DOUBLE_QUOTE;
backQuoted: BACK_QUOTE BQ_CONTENT BACK_QUOTE;
