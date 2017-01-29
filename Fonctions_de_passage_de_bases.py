## Passage d'un nombre base 10 en bas 2 (récursif)
def de10en2Rec(n):
    def aux(n): #precondition n strictement positif
        rep=""
        if (n!=0):
            ## version plus lisible
            reste=n%2
            if (reste==1):
                rep=aux(n/2)+"1"
            else:
                rep=aux(n/2)+"0"
            ## version condensee        
            #rep = aux(n/2)+str(n%2)
        return rep
    
    if (n>=0):
        if (n==0):
            rep="0"
        else :
            rep = aux(n)
        return rep

## Passage d'un nombre base 10 en bas 2 (Itératif)
def de10en2Iter(n):
    if (n>=0):
        rep=""
        if (n==0):
            rep="0"
        #while (n>0):
        while (n!=0):
            ## version plus lisible
            reste=n%2
            n=n/2
            if (reste==1):
                rep="1"+rep
            else:
                rep="0"+rep
            ## version condensee
            ## rep = str(n%2) + rep
            ## n=n/2
        return rep