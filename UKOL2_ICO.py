import requests  

ico = input("Zadejte IČO:  ")  
adresa = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"  

response = requests.get(adresa)  
data = response.json()
#print(data)

"""{'ico': '22834958', 'obchodniJmeno': 'Czechitas z.ú.', 
'sidlo': {'kodStatu': 'CZ', 'nazevStatu': 'Česká republika', 'kodKraje': 19, 
'nazevKraje': 'Hlavní město Praha', 'kodObce': 554782, 
'nazevObce': 'Praha', 'kodSpravnihoObvodu': 19, 
'nazevSpravnihoObvodu': 'Praha 1', 'kodMestskehoObvodu': 19, 
'nazevMestskehoObvodu': 'Praha 1',
 'kodMestskeCastiObvodu': 500054, 'kodUlice': 477265, 
 'nazevMestskeCastiObvodu': 'Praha 1', 'nazevUlice': 'Václavské náměstí', 
 'cisloDomovni': 837, 'kodCastiObce': 490148, 'cisloOrientacni': 11, 
 'nazevCastiObce': 'Nové Město', 'kodAdresnihoMista': 21706425, 
 'psc': 11000, 'textovaAdresa': 'Václavské náměstí 837/11, Nové Město, 11000 Praha 1',
   'typCisloDomovni': '1', 'standardizaceAdresy': True},
     'pravniForma': '161', 'financniUrad': '001', 
     'datumVzniku': '2009-09-18',
       'datumAktualizace': '2023-11-03', 'dic': 'CZ22834958', 'icoId': '22834958',
         'adresaDorucovaci': {'radekAdresy1': 'Václavské náměstí 837/11', 
         'radekAdresy2': 'Nové Město', 'radekAdresy3': '11000 Praha 1'}, 
         'seznamRegistraci': {'stavZdrojeVr': 'AKTIVNI', 'stavZdrojeRes': 'AKTIVNI', 'stavZdrojeRzp': 'NEEXISTUJICI', 'stavZdrojeNrpzs': 'NEEXISTUJICI', 'stavZdrojeRpsh': 'NEEXISTUJICI', 'stavZdrojeRcns': 'NEEXISTUJICI', 'stavZdrojeSzr': 'NEEXISTUJICI', 'stavZdrojeDph': 'AKTIVNI', 'stavZdrojeSd': 'NEEXISTUJICI', 'stavZdrojeIr': 'NEEXISTUJICI', 'stavZdrojeCeu': 'NEEXISTUJICI', 'stavZdrojeRs': 'NEEXISTUJICI', 'stavZdrojeRed': 'AKTIVNI'}, 
         'primarniZdroj': 'vr', 'czNace': ['9499']}"""

obchodni_jmeno=data['obchodniJmeno']
adresa_sidla=data['sidlo']['textovaAdresa']
#print(obchodni_jmeno)
#print(adresa_sidla)
print(f"{obchodni_jmeno}\n{adresa_sidla}")

################################


obchodni_jmeno_subjektu = input("Zadejte název subjektu: ")  
headers = {  "accept": "application/json","Content-Type": "application/json"}


data = f'{{"obchodniJmeno": "{obchodni_jmeno_subjektu}"}}'
adresa = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"  

response = requests.post(adresa, headers=headers, data=data.encode("utf-8"))  

my_data = response.json()

pocet_nalezenych = my_data["pocetCelkem"]

print (f"Nalezeno subjektů: {pocet_nalezenych}")

ekonomicke_subjekty = my_data["ekonomickeSubjekty"]
for subjekt in ekonomicke_subjekty: 
    print(f'{subjekt["obchodniJmeno"]} , {subjekt["ico"]}')
    


