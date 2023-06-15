#local application imports
from Gramática.GLC import GLC
from Análisis_Sintáctico_LL1.syntax_chart import * 

print("Análisis para la Gramática - LL1")
grammar = GLC('Start')
grammar.add_production("Start", "🜉 s Program 🝓")
grammar.add_production("Program", "Statement s Program")
grammar.add_production("Program", "λ")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Assignment", "🝳 identifier 🝳 🝑 Expression")
grammar.add_production("Expression", "Term Expression\'")
grammar.add_production("Expression\'", "🜂 Term")
grammar.add_production("Expression\'", "🜃 Term")
grammar.add_production("Expression\'", "🜁 Term")
grammar.add_production("Expression\'", "🜄 Term")
grammar.add_production("Expression\'", "λ")
grammar.add_production("Term", "🝳 identifier 🝳")
grammar.add_production("Term", "constant")
grammar.add_production("IfStatement", "se ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("Condition", "Expression 🜎 Expression")
grammar.add_production("Condition", "Expression 🜍 Expression")
grammar.add_production("Condition", "Expression 🜕 Expression")
grammar.add_production("Condition", "Expression 🜔 Expression")
grammar.add_production("Condition", "Expression 🜗 Expression")
grammar.add_production("Condition", "Expression 🜖 Expression")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("WhileLoop", "dum ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("Statement", "ForLoop")
grammar.add_production("ForLoop", "por ☾ Assignment ; Condition ; Assignment ☽ s 🜚 s Program 🜚")

grammar.print_productions()

print("----------------------------------")
print("First Phase")
grammar.firstPhase()
grammar.print_productions()
print("----------------------------------")
print("Second Phase")
grammar.second_phase()
grammar.print_productions()
print("----------------------------------")
print("left factoring")
grammar.left_factoring()
grammar.print_productions()
print("----------------------------------")
print("Eliminate left recursion")
grammar.eliminate_left_recursion()
grammar.print_productions()

grammar.terminals = grammar.remove_duplicates(grammar.terminals)

print("PRIMEROS")
print(grammar.get_first())
print("SIGUIENTES")
print(grammar.get_following())

if(differentFirstandFollowing(grammar.firstS, grammar.followingS) == False):
    print("Firsts and Followings have elements in common, not LL1.")
else:
    chart = createChart(grammar)
    printChart(grammar.terminals, grammar.nonTerminals, chart)
    print("\nCorrect Syntax Cases:")
    parse("🜉 s 🝳 identifier 🝳 🝑 constant s 🝳 identifier 🝳 🝑 constant s 🝓", chart, grammar)
    print()
    parse("🜉 s 🝓", chart, grammar)
    print()
    parse("🜉 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant s 🜚 s 🝓", chart, grammar)
    print()
    parse("🜉 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓", chart, grammar)
    print()
    parse("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓", chart, grammar)
    print()
    parse("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🜚 s 🜚 s 🝓", chart, grammar)
    print()
    print("\nIncorrect Syntax Cases:")
    parse("🜉 s 🝳 identifier 🝳 constant s 🝳 identifier 🝳 🝑 constant s 🝓", chart, grammar)
    print()
    parse("🜉 s 🝓 s s", chart, grammar)
    print()
    parse("🜉 s se ☾ 🝳 🝳 🜕 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant s 🜚 s 🝓", chart, grammar)
    print()
    parse("🜉 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 t s 🜚 s 🝓", chart, grammar)
    print()