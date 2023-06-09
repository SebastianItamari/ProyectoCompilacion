class LL1Error(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


def createChart(glc):
    chart = {}
    for x in glc.nonTerminals:
        chart[x] = {}
        for y in glc.terminals:
            chart[x][y] = '#' 
        chart[x]['$'] = '#' # symbol $ 
    
    #iteration to create chart
    for nonterminal in glc.productions:
        #x is the nonterminal that calls the dictionary
        productions = glc.productions[nonterminal] #this is a list of productions
        currentfirsts = glc.firstS[nonterminal] #the list of firsts from x
        for currentfirst in currentfirsts:
            #currentfirst is one first of the nonterminal X
            if(currentfirst == 'λ'):
                currentfollows = glc.followingS[nonterminal]
                for currentfollow in currentfollows:
                    chart[nonterminal][currentfollow] = 'λ'
            else: 
                foundProduction = False
                for production in productions:
                    #now production is a single production
                    listproduction = production.split() 
                    #listproduction is each symbol of a production as a list
                    donewithFirsts = False
                    n = 0 #position in production
                    while(donewithFirsts == False and production != 'λ'):
                        donewithFirsts = True 
                        productionFirsts = glc.first(listproduction[n]) 
                        for productionFirst in productionFirsts:
                            if(productionFirst != 'λ' and productionFirst == currentfirst):
                                donewithFirsts = True 
                                foundProduction = True
                                break 
                            if(productionFirst == 'λ'):
                                donewithFirsts = False 
                        n += 1
                    if(foundProduction == True):
                        #production that generates this first from nonterminal has been found
                        #the position for nonterminal and this symbol in the chart must be filled
                        #with this production
                        chart[nonterminal][currentfirst] = production 
                        break 
    return chart 

def printChart(terminals, nonterminals, chart):
    print("  ", end="")
    for x in terminals:
        print(x+"   ", end="")
    print('$')
    for x in nonterminals:
        print(x+" ", end="")
        for y in terminals:
            print(chart[x][y], end="")
            print(" ", end = "")
        print(chart[x]['$'])

def parse(sentence, chart, glc):
    #print(sentence+": ",end="")
    parsingStack = [glc.initial]
    error = False 
    if(sentence == ""):
        error = True 
        raise Exception
    try:
        for symbol in sentence:
            character = symbol[0] #would be character in sentence.split()
            last = parsingStack.pop()
            while(character != last):
                production = chart[last][character]
                if(production == "#"):
                    error = True 
                    raise Exception
                    #break
                if(production != "λ"):
                    for char in production.split()[::-1]:
                        parsingStack.append(char)
                last = parsingStack.pop()
            if(error == True):
                raise Exception
            #sentence = " ".join(sentence.split()[1:])
        
        if(len(parsingStack)>0):
        #stack still has elements
            last = parsingStack.pop()
            while(len(parsingStack) > 0 and error == False):
                production = chart[last]['$']
                if(production == "#"):
                    #error = True 
                    raise Exception
                    #break
                if(production != "λ"):
                    for char in production.split()[::-1]:
                        parsingStack.append(char)
                last = parsingStack.pop()

        if(error == True):
            raise Exception
        else:
            print("The sentence is syntactically correct.")

    except:
        message = ""
        linewithError = ""
        for x in sentence:
            if x[2] == symbol[2] and x[1]!="\n":
                linewithError = linewithError + f"{x[1]} "
        #print(f"Syntax error, line {symbol[2]}, in {linewithError} with ", end="")
        message = f"Syntax error, line {symbol[2]}, in {linewithError} with "
        if(symbol[0] == "s"):
            #print("end of line.")
            message = message + "end of line.\n"
        else:
            #print(symbol[1])
            message = message + symbol[1] + "\n"
        #tokens _> symbol. line se encuentra en symbol[2]
        #usar tokens para imprimir toda la linea con el error
        
        #print("last:", last)
        
        #print("Instead could use ", end="")
        message = message + "Instead could use "
        possibleCharactersList = []
        if(last in glc.terminals):
            if(last=="s"):
                possibleCharactersList.append("end of line")
            else: 
                possibleCharactersList.append(last)
        else: 
            for possibleCharacter in chart[last]:
                if(chart[last][possibleCharacter]!="#"):
                    if(chart[last][possibleCharacter]=="s"):
                        possibleCharactersList.append("end of line")
                    else: 
                        possibleCharactersList.append(possibleCharacter)

        possibleCharactersList = " , ".join(possibleCharactersList)
        message = message + possibleCharactersList
        raise LL1Error(message)
        
        #quit()
    
def generateExceptionMessage(sentence, symbol, last, glc, chart):
    message = ""
    linewithError = ""
    for x in sentence:
        if x[2] == symbol[2] and x[1]!="\n":
            linewithError = linewithError + f"{x[1]} "
    print(f"Syntax error, line {symbol[2]}, in {linewithError} with ", end="")
    if(symbol[0] == "s"):
        print("end of line.")
    else:
        print(symbol[1])
        #tokens _> symbol. line se encuentra en symbol[2]
        #usar tokens para imprimir toda la linea con el error
        
        #print("last:", last)
        
    print("Instead could use ", end="")
    possibleCharactersList = []
    if(last in glc.terminals):
        possibleCharactersList.append(last)
    else: 
        for possibleCharacter in chart[last]:
            if(chart[last][possibleCharacter]!="#"):
                possibleCharactersList.append(possibleCharacter)

    possibleCharactersList = " , ".join(possibleCharactersList)
    message = possibleCharactersList
    return message 

def differentFirstandFollowing(firsts, followings):
    different = True
    for x in firsts:
        firstset = set(firsts[x])
        followingset = set(followings[x])
        if(firstset & followingset):
            different = False 
            print("Nonterminal with repeated elements: "+x)
            print("Firsts: ",firstset)
            print("Followings: ",followingset)
            break 
    return different 







                

            

        
    

