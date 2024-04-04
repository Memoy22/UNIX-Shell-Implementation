// Generated from C:/Users/MemoyMishra/Documents/UCL/year2_2023/softwareEngineering_COMP0010/comp0010-shell-python-p26/src/shellParser.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by {@link shellParser#cmd}.
	 * @param ctx the parse tree
	 */
	void enterCmd(shellParser.CmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#cmd}.
	 * @param ctx the parse tree
	 */
	void exitCmd(shellParser.CmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link shellParser#subcommand}.
	 * @param ctx the parse tree
	 */
	void enterSubcommand(shellParser.SubcommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#subcommand}.
	 * @param ctx the parse tree
	 */
	void exitSubcommand(shellParser.SubcommandContext ctx);
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
	 * Enter a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(shellParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(shellParser.RedirectionContext ctx);
}