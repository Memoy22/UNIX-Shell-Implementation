parser grammar shellParser;

options {
  tokenVocab=shellLexer;
}

cmdline: commands? EOF;
commands: command (SEMICOLON command)*;
command: pipe;
pipe: call (PIPE call)*;

call: (redirection)* argument (atom)* ;
argument: quoted | unquoted;
atom: redirection | argument;
redirection: REDIRECT_INPUT argument | REDIRECT_OUTPUT argument;

quoted: singleQuoted | doubleQuoted | backQuoted;
unquoted: UNQUOTED;

singleQuoted: SQ_START SQ_CONTENT SQ_END;

doubleQuoted: DQ_START content DQ_END;
content: (DQ_CONTENT | backQuotedInDoubleQuoted)*;
backQuotedInDoubleQuoted: BQ_START_IN_DQ BQ_CONTENT BQ_END;

backQuoted: BQ_START BQ_CONTENT BQ_END;
