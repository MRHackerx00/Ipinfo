#klx2006 phonenumber info   tools python
import requests
import time
import os


y =  "\033[33m"
red = "\033[31m"
rs = "\033[0m"
g = "\033[32m"

k ="""

██╗  ██╗██╗     ██╗  ██╗██████╗  ██████╗  ██████╗ ███████╗
██║ ██╔╝██║     ╚██╗██╔╝╚════██╗██╔═████╗██╔═████╗╚════██║
█████╔╝ ██║      ╚███╔╝  █████╔╝██║██╔██║██║██╔██║    ██╔╝
██╔═██╗ ██║      ██╔██╗ ██╔═══╝ ████╔╝██║████╔╝██║   ██╔╝ 
██║  ██╗███████╗██╔╝ ██╗███████╗╚██████╔╝╚██████╔╝   ██║  
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝  
                                                          
                 api use "http://phone-number-api.com/json/"
"""
print(y + k + rs)
def data(numm): #api requests funconsan
    url = f"http://phone-number-api.com/json/?number={numm}&fields=status,message,numberType,numberValid,numberValidForRegion,numberCountryCode,numberAreaCode,formatE164,formatNational,formatInternational,dialFromCountryCode,dialFromCountryNumber,ext,carrier,continent,continentCode,countryName,country,region,regionName,city,zip,lat,lon,timezone,offset,currency,query"
    response = requests.get(url)
    data = response.json()
    return data
                                       
numm = input(red + 'enter your phone  number with countrycode  lookup +: ' + rs) # input  
data = data(numm)
print(' ')
print(g + f"phonenumber:x {data['query']}")
print(f"status: {data['status']}")
print(f"numberType: {data['numberType']}")
print(f"numberValid: {data['numberValid']}")
print(f"numberValidForRegion: {data['numberValidForRegion']}")
print(f"numberCountryCode: {data['numberCountryCode']}")
print(f"ext: {data['ext']}")
print(f"formatE164: {data['formatE164']}")
print(f"formatNational: {data['formatNational']}")
print(f"formatInternational: {data['formatInternational']}")
print(f"dialFromCountryCode: {data['dialFromCountryCode']}")
print(f"dialFromCountryNumber: {data['dialFromCountryNumber']}")
print(f"carrier: {data['carrier']}")
print(f"continent: {data['continent']}")
print(f"continentCode: {data['continentCode']}")
print(f"country: {data['country']}")
print(f"countryName: {data['countryName']}")
print(f"city: {data['city']}")
print(f"zip: {data['zip']}")
print(f"lat: {data['lat']}")
print(f"lon: {data['lon']}")
print(f"timezone: {data['timezone']}")
print(f"offset: {data['offset']}")
print(f"currency: {data['currency']}" + rs)
print(' ')
a = input(f"{y}you sava logs y/n :-  {rs}")
if a =="y":
  with open(f'{numm}.txt', "a") as file:
             file.write(f"{k}\n")
             file.write(f"phonenumber: {data['query']}\n")
             file.write(f"status: {data['status']}\n")
             file.write(f"numberType: {data['numberType']}\n")
             file.write(f"numberValid: {data['numberValid']}\n")
             file.write(f"numberValidForRegion: {data['numberValidForRegion']}\n")
             file.write(f"numberCountryCode: {data['numberCountryCode']}\n")
             file.write(f"ext: {data['ext']}\n")
             file.write(f"formatE164: {data['formatE164']}\n")
             file.write(f"formatNational: {data['formatNational']}\n")
             file.write(f"dialFromCountryCode: {data['dialFromCountryCode']}\n")
             file.write(f"dialFromCountryNumber: {data['dialFromCountryNumber']}\n")
             file.write(f"carrier: {data['carrier']}\n")
             file.write(f"continent: {data['continent']}\n")
             file.write(f"continentCode: {data['continentCode']}\n ")
             file.write(f"country: {data['country']}\n")
             file.write(f"countryName: {data['countryName']}\n")
             file.write(f"city: {data['city']}\n ")
             file.write(f"zip: {data['zip']}\n ")
             file.write(f"lat: {data['lat']}\n")
             file.write(f"lon: {data['lon']}\n")
             file.write(f"timezone: {data['timezone']}\n")
             file.write(f"offset: {data['offset']}\n")
             file.write(f"currency: {data['currency']}\n")
             file.write(f"TIME:\n")
             file.write(f"************************************* ")
  print(f"{g}savaed{rs}")
else:
    print(f"{g}ok not save {rs}")
             
