BASISESTIMAT = 250
GRUNNESTIMAT = 15
NEDGANG_SIDEN_2007 = 2500

def BeregnAntallKrabbeTonn(basisestimat=BASISESTIMAT, grunnestimat=GRUNNESTIMAT):
    fundamentestimat = basisestimat * grunnestimat
    estimat = fundamentestimat * 2
    estimat -= NEDGANG_SIDEN_2007
    return estimat