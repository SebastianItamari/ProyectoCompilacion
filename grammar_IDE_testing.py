#local application imports
from Gramática.GLC import GLC
from IDE.CodechemyIDE import CodechemyIDE

grammar = GLC('Start')
grammar.add_production("Start", "🜉 s Program 🝓")
grammar.add_production("Program", "Statement s")
grammar.add_production("Program", "Statement s Program")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")
grammar.add_production("Statement", "Print")
grammar.add_production("Assignment", "🝳 identifier 🝳 🝑 Expression")
grammar.add_production("Expression", "Term Expression'")
grammar.add_production("Expression", "Term")
grammar.add_production("Expression'", "🜂 Term")
grammar.add_production("Expression'", "🜃 Term")
grammar.add_production("Expression'", "🜁 Term")
grammar.add_production("Expression'", "🜄 Term")
grammar.add_production("Term", "🝳 identifier 🝳")
grammar.add_production("Term", "constant")
grammar.add_production("IfStatement", "se ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("Condition", "Expression 🜎 Expression")
grammar.add_production("Condition", "Expression 🜍 Expression")
grammar.add_production("Condition", "Expression 🜕 Expression")
grammar.add_production("Condition", "Expression 🜔 Expression")
grammar.add_production("Condition", "Expression 🜗 Expression")
grammar.add_production("Condition", "Expression 🜖 Expression")
grammar.add_production("WhileLoop", "dum ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("ForLoop", "por ☾ Assignment ; Condition ; Assignment ☽ s 🜚 s Program 🜚")
grammar.add_production("Print", "presi ☾ Term ☽")

IDE = CodechemyIDE(grammar, "CLR")