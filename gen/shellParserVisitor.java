// Generated from C:/Users/MemoyMishra/Documents/UCL/year2_2023/softwareEngineering_COMP0010/comp0010-shell-python-p26/src/shellParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link shellParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface shellParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link shellParser#cmdline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdline(shellParser.CmdlineContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#commands}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommands(shellParser.CommandsContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommand(shellParser.CommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#pipe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPipe(shellParser.PipeContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall(shellParser.CallContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#cmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmd(shellParser.CmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#subcommand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubcommand(shellParser.SubcommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(shellParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(shellParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#unquoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnquoted(shellParser.UnquotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#quoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuoted(shellParser.QuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirection(shellParser.RedirectionContext ctx);
}