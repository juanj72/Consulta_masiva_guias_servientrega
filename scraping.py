import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import json_normalize


url='https://mobile.servientrega.com/GreenMobile/CO/mapas/DistribucionCliente/getGuiasDistribucionCliente'


base=pd.read_excel('base.xlsx')
reporte=[]

for i in range(len(base)):
    guia=str(base['guia'][i])
    guia=guia.strip()
    datos={
    "strIdGuia":str(guia)
    

    }
    respuesta = requests.post(url, json=datos)
        # Ahora decodificamos la respuesta como json
    como_json = respuesta.json()


    print("La respuesta del servidor es:")
    #print(como_json)
    #data=json_normalize(como_json)
    reporte.append(como_json)
    
    


print(reporte)
reporte=pd.DataFrame(reporte)
reporte.to_excel('datos.xlsx')




