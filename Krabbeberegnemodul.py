import requests

BASISESTIMAT = 250
GRUNNESTIMAT = 15
NEDGANG_SIDEN_2007 = 2500

def DynamiskKrabbeberegning():
    requests.get("https://www.hi.no/hi/temasider/arter/taskekrabbe").status_code * 12.5

def BeregnAntallKrabbeTonn(basisestimat=BASISESTIMAT, grunnestimat=GRUNNESTIMAT):
    return DynamiskKrabbeberegning()