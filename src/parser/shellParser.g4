parser grammar shellParser;

options {
  tokenVocab=ShellLexer;
}

// Entry point
cmdline : commands? EOF;

commands : command (SEMICOLON command?)*;

command : pipe;
// Pipe command
pipe : call (PIPE call)*;

// Call command
//call : CMD WS* redirection? (argument | atom | subcommand)* WS*;
//call : cmd WS* (argument | atom | subcommand)* WS*;
call : (cmd | redirection) WS* (argument | atom | subcommand)* WS*;

cmd: SINGLE_QUOTED | DOUBLE_QUOTED | BACKQUOTED | UNQUOTED;// | redirection;

subcommand : BACKQUOTED;// commands BACKQUOTED;

atom : redirection | argument;

argument : (quoted | unquoted)+;

unquoted : UNQUOTED;

quoted : SINGLE_QUOTED | DOUBLE_QUOTED | BACKQUOTED;

redirection : REDIRECT_INPUT WS* argument | REDIRECT_OUTPUT WS* argument;