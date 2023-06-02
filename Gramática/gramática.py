import GLC
print("--------------------------------------")
print("NUESTRA GRAMÁTICA")
grammar4 = GLC('A')

grammar4.add_production("A", "🜉 Y 🝓")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar4.add_production("B", "🝰")
grammar4.add_production("B", "🝯")
grammar4.add_production("B", "🝮")
grammar4.add_production("C", "B")
grammar4.add_production("C", "🜸")
grammar4.add_production("D", "🝳 K 🝳")
grammar4.add_production("E", "🜛 K ☾ I' ☽ 🜛")
grammar4.add_production("F", "B e D")
grammar4.add_production("G", "D e 🝑 e H")
grammar4.add_production("H", "B'")
grammar4.add_production("H", "E'")
grammar4.add_production("I", "D")
grammar4.add_production("I", "M")
grammar4.add_production("J", "🜂")    
grammar4.add_production("J", "🜄")
grammar4.add_production("J", "🜁")
grammar4.add_production("J", "🜃")
grammar4.add_production("K", "L K")  
grammar4.add_production("K", "M K")
grammar4.add_production("K", "λ")
grammar4.add_production("L", "'a'")  
grammar4.add_production("L", "'b'")
grammar4.add_production("L", "'c'")
grammar4.add_production("L", "'d'")
grammar4.add_production("L", "'A'")
grammar4.add_production("L", "'B'")
grammar4.add_production("L", "'C'")
grammar4.add_production("L", "'D'")
grammar4.add_production("M", "N")
grammar4.add_production("M", "N M") 
grammar4.add_production("N", "0")  
grammar4.add_production("N", "1")  
grammar4.add_production("N", "2")  
grammar4.add_production("N", "3")  
grammar4.add_production("N", "4")  
grammar4.add_production("N", "5")  
grammar4.add_production("N", "6")  
grammar4.add_production("N", "7")  
grammar4.add_production("N", "8")
grammar4.add_production("N", "9")    
grammar4.add_production("O", "🝱")
grammar4.add_production("P", "🜓")
grammar4.add_production("P", "🝘")
grammar4.add_production("Q", "🜔")
grammar4.add_production("Q", "🜕")
grammar4.add_production("Q", "🜖")
grammar4.add_production("Q", "🜗")
grammar4.add_production("Q", "🜎")
grammar4.add_production("Q", "🜍")
grammar4.add_production("R", "v")
grammar4.add_production("R", "m")
grammar4.add_production("R", "D")
grammar4.add_production("S", "s e ☾ E' ☽ n 🜚 n Y 🜚 n T")
grammar4.add_production("T", "i n 🜚 n Y n 🜚")  
grammar4.add_production("T", "λ")
grammar4.add_production("U", "d e ☾ E' ☽ n 🜚 n V n 🜚")
grammar4.add_production("V", "Y")
grammar4.add_production("V", "Y n V")
grammar4.add_production("V", "a n")
grammar4.add_production("W", "Y")
grammar4.add_production("W", "Y n W")
grammar4.add_production("W", "r e D n")
grammar4.add_production("X", "I Q I")
grammar4.add_production("Y", "Z")
grammar4.add_production("Y", "Z n Y")
grammar4.add_production("Z", "F") 
grammar4.add_production("Z", "A'")
grammar4.add_production("Z", "U")
grammar4.add_production("Z", "S")
grammar4.add_production("Z", "n")
grammar4.add_production("Z", "J'")
grammar4.add_production("Z", "H'")
grammar4.add_production("Z", "G")
grammar4.add_production("A'", "B'")
grammar4.add_production("A'", "E'")
grammar4.add_production("B'", "B' 🜂 C'")
grammar4.add_production("B'", "B' 🜄 C'")
grammar4.add_production("B'", "C'")
grammar4.add_production("C'", "C' 🜁 D'")
grammar4.add_production("C'", "C' 🜃 D'")
grammar4.add_production("C'", "D'")
grammar4.add_production("D'", "☾ B' ☽")
grammar4.add_production("D'", "I")
grammar4.add_production("E'", "E' 🝘 F'")
grammar4.add_production("E'", "F")
grammar4.add_production("E'", "X")
grammar4.add_production("F'", "F' 🜓  G'")
grammar4.add_production("F'", "G'")
grammar4.add_production("G'", "🝱 G'")
grammar4.add_production("G'", "G'")
grammar4.add_production("G'", "R")
grammar4.add_production("H'", "f e C e E ☾ I' ☽ n 🜚 n W n 🜚")
grammar4.add_production("I'", "F")
grammar4.add_production("I'", "F c I'")
grammar4.add_production("I'", "λ")
grammar4.add_production("J'", "K'")
grammar4.add_production("J'", "L'")
grammar4.add_production("K'", "🜌 Z n")
grammar4.add_production("K'", "🜌 a")
grammar4.add_production("K'", "🜌 r")
grammar4.add_production("L'", "🜋 W 🜋")
grammar4.add_production("L'", "🜋 V 🜋")

#grammar4.print_productions()

print("----------------------------------")

grammar4.firstPhase()
grammar4.second_phase()
grammar4.left_factoring()
#grammar4.eliminate_indirect_left_recursion()
grammar4.eliminate_left_recursion()
grammar4.print_productions()

"""
grammar4.print_productions()
print("PRIMEROS")
print(grammar4.get_first())
print("SIGUIENTES")
print(grammar4.get_following())
"""