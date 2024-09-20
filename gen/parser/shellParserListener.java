// Generated from D:/MEMOY/UCL/prep/Marshall Wace/UNIX-Shell-Implementation/src/parser/shellParser.g4 by ANTLR 4.13.1
package parser;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link shellParser}.
 */
public interface shellParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link shellParser#cmdline}.
	 * @param ctx the parse tree
	 */
	void enterCmdline(shellParser.CmdlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#cmdline}.
	 * @param ctx the parse tree
	 */
	void exitCmdline(shellParser.CmdlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#commands}.
	 * @param ctx the parse tree
	 */
	void enterCommands(shellParser.CommandsContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#commands}.
	 * @param ctx the parse tree
	 */
	void exitCommands(shellParser.CommandsContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(shellParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(shellParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(shellParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(shellParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(shellParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(shellParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(shellParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(shellParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(shellParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(shellParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(shellParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(shellParser.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(shellParser.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(shellParser.QuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#unquoted}.
	 * @param ctx the parse tree
	 */
	void enterUnquoted(shellParser.UnquotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#unquoted}.
	 * @param ctx the parse tree
	 */
	void exitUnquoted(shellParser.UnquotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterSingleQuoted(shellParser.SingleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitSingleQuoted(shellParser.SingleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterDoubleQuoted(shellParser.DoubleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitDoubleQuoted(shellParser.DoubleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#content}.
	 * @param ctx the parse tree
	 */
	void enterContent(shellParser.ContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#content}.
	 * @param ctx the parse tree
	 */
	void exitContent(shellParser.ContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#backQuotedInDoubleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterBackQuotedInDoubleQuoted(shellParser.BackQuotedInDoubleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#backQuotedInDoubleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitBackQuotedInDoubleQuoted(shellParser.BackQuotedInDoubleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void enterBackQuoted(shellParser.BackQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void exitBackQuoted(shellParser.BackQuotedContext ctx);
}