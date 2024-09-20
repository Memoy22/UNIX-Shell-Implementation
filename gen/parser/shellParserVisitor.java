// Generated from D:/MEMOY/UCL/prep/Marshall Wace/UNIX-Shell-Implementation/src/parser/shellParser.g4 by ANTLR 4.13.1
package parser;
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
	 * Visit a parse tree produced by {@link shellParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(shellParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(shellParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#redirection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirection(shellParser.RedirectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#quoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuoted(shellParser.QuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#unquoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnquoted(shellParser.UnquotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#singleQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSingleQuoted(shellParser.SingleQuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#doubleQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoubleQuoted(shellParser.DoubleQuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#content}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContent(shellParser.ContentContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#backQuotedInDoubleQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBackQuotedInDoubleQuoted(shellParser.BackQuotedInDoubleQuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link shellParser#backQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBackQuoted(shellParser.BackQuotedContext ctx);
}