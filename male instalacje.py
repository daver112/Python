from copy import copy
from optparse import Values
from sqlite3 import Row
import requests
import pandas as pd

plik=requests.get("https://api.ure.gov.pl/api/MIOZERegistry")

dane=plik.json()


df=pd.DataFrame(data=dane)
df.sort_values("dkn", inplace=True)
df["Nazwa i adres wytwórcy"]=df["nazwa"]+", "+df["adres"]+" "+df["kod"]+" "+df["miejscowosc"]
#filtr1=df["rodzajKoncesji"]=="WEE"
df.rename(columns={"dkn":"DKN", 
"nazwa":"Nazwa", 
"nip":"NIP", 
"adres":"Adres", 
"kod":"Kod pocztowy", 
"miejscowosc":"Miejscowość", 
"nrWpisu":"Numer MIOZE", 
"poczta":"Poczta", 
"dataWpisu":"Data wpisu", 
"iloscPozycji":"Liczba źródeł", 
"miejscowoscInstalacji":"Miejscowość instalacji", 
"wojewodztwoInstalacji":"Wojewódzctwo instalacji", 
"dataRozpoczeciaDzialalnosci": "Data rozpoczecia dzialalności", 
"rodzajInstalacji":"Rodzaj instalacji", 
"mocEEInstalacji":"Moc instalacji", 
"rodzajIZakres":"Rodzaj i zakres"}, inplace=True)

rodzaje={'BGM':'BG',
'BGO':'BG',
'BGS':'BG',
'BMG':'BM',
'BMM':'BM',
'PVA':'PV',
'WIL':'WI',
'WOA':'WO',
'WOB':'WO',
'WOC':'WO'}

df["Rodzaj instalacji dla URE"]=df["Rodzaj instalacji"]
df.replace({"Rodzaj instalacji dla URE":rodzaje}, inplace=True)

kolejnosc_kolumn=['DKN','Nazwa','Nazwa i adres wytwórcy','NIP',	'Adres','Kod pocztowy',	'Miejscowość','Numer MIOZE','Poczta','Data wpisu','Liczba źródeł','Miejscowość instalacji','Wojewódzctwo instalacji','Data rozpoczecia dzialalności','Rodzaj instalacji','Rodzaj instalacji dla URE','Moc instalacji','Rodzaj i zakres']
df=df.reindex(columns=kolejnosc_kolumn)

#df.to_excel("Małe instalacje.xlsx", sheet_name="Małe instalacje", index=False)


tabela_przestawna=df.pivot_table(index="Rodzaj instalacji", columns="Rodzaj instalacji dla URE", values=['DKN','Miejscowość'], aggfunc=['sum'], dropna=True, fill_value=0)
print(tabela_przestawna)