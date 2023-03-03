import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import json_normalize


informe=[]
base=pd.read_excel('base_guia_detalle.xlsx')



url='https://mobile.servientrega.com/Services/ShipmentTracking/api/ControlRastreovalidaciones'

for i in range(len(base)):

    guia=base['guia'][i]

    datos = {"datoRespuestaUsuario"
    : 
    "0",
    "idValidacionUsuario"
    : 
    "0",
    "idpais"
    : 
    "1",
    "lenguaje"
    : 
    "es",
    "numeroGuia"
    : 
    f"{guia}",
    "tipoDatoValidar"
    : 
    "0"}

    respuesta = requests.post(url, json=datos)
    datos=respuesta.json()

    datos=pd.DataFrame(datos)

    #print(datos['Results'])

    

    #guia_detalle=pd.DataFrame(datos_completos)
    informe.append(datos['Results'])



# guia_detalle.to_excel('guia detalle.xlsx')
#print(informe)
data=pd.DataFrame(informe)
resultado=json_normalize(data[0])
datos_tot=pd.DataFrame(resultado)
print(datos_tot)
#resultado.to_excel('guia detalle.xlsx')
#data.to_excel('guia detalle.xlsx')






