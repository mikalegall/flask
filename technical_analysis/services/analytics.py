# Tuodaan käytettäväksi internetistä datan noutaja esim. Yahoo Financesta valuuttakursseille
# https://pydata.github.io/pandas-datareader/remote_data.html#forex
# DataReadilla noudetuissa tiedoissa on aikaleima valmiina indeksissä
import pandas_datareader as web
# Tuodaan graafiseen esittämiseen matplotlib ja sen käyttöliittymäksi pyplot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#module-matplotlib.pyplot
import matplotlib.pyplot as plt
# Tuodaan käytettäväksi data-analytiikan kirjasto pandas ja lyhennetään sitä kutsuttavaksi aliaksella pd
# https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe
import pandas as pd

import os
from pathlib import Path
# Ajan käsittelyyn tarvittavia kirjastoja
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


# One level up
ROOT_DIR = Path(__file__).parent


def analyze():
    //TODO Copy+paste omasta Jupyter Notebookista

    # Valitaan graafinen esittäminen muotoiltavaksi tietyllä tyylillä
    plt.style.use('seaborn-whitegrid')


//TODO Muuttujien nimien käsittely
    # Hae kohde-etuuden tunniste noudetettavasta kohteesta
    # https://duckduckgo.com/?q=yahoo+finance+elisa
    # https://duckduckgo.com/?q=yahoo+finance+nordea+bull+dax+10
    elisa = web.DataReader('ELISA.HE', start='2015-1-1', data_source='yahoo')

    #Suurennetaan esitysaluetta oletuskoostaan suuremmaksi
    elisa['Close'].plot(figsize=(14,6))

    #Satunnaisvaihtelun tasaamiseen voidaan laskea liukuva keskiarvo
    # https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp
    ##Liukuva keskiarvo voi olla singnaalina toimenpiteelle
    ##Jatkuvasti rullaava (liukuva, rolling) komento rolling() ottaa parametrikseen ajankohtien lukumäärän
    ###Lasketaan 50 viimeiselle päivälle jatkuvasti päivittyvänä (rullaavana, liukuvana) keskiarvo komennolla mean()
    elisa['Close'].rolling(50).mean().plot()

    #Samaan visualisointiin voidaan plotata (graafisesti esitettäväksi) useampia kaavioita samanaikaisesti
    ##Lasketaan Elisan osakkeen päätösluvulle 200 päivän liukuva keskiarvo
    elisa['Close'].rolling(200).mean().plot()




    #Usein tarkoituksenmukaisempaa on tarkastella muutosta prosentuaalisena
    ##Luodaan DataFrameen uusi sarake nimeltä "Elisa %" ja sijoitettaan sen arvoksi
    ##taulukon "Close" sarakkeesta komennolla "pct_change()" laskettu prosentuaalinen muutos
    ##Muutos on verrattuna edelliseen eli tässä tapauksessa edelliseen pörssinkäyntipäivään
    elisa['%'] = elisa['Close'].pct_change()


    #Liitetään konkatenoinnilla juuri luodut muutosprosentti-sarakket kolmanteen taulukkoon
    #muutokset = pd.concat([elisa['Elisa %'], telia['Telia %']], axis = 1)
    muutokset = elisa['%']

    #Vuosittaisen volatiliteetin muutosprosentin keskihajonta jatkuvasti rullaava (liukuva, rolling)
    ##Komento rolling() ottaa parametrikseen ajankohtien lukumäärän
    ##Lasketaan vuoden kaupantekopäivien (252 päivää) muutosprosenteille jatkuvasti päivittyvänä (rullaavana, liukuvana)
    ##keskihajonta (standard deviation) komennolla std() ja skaalataan se neliöjuurella kertomalla vuosittaiseksi
    ##sekä esitetään se plotaten graafisena visualisointina (lopulta suurennetaan esitysaluetta oletuskoostaan suuremmaksi)
    (muutokset['Elisa%'].rolling(252).std() * (252**0.5)).plot(label = 'Elisa', legend = True, figsize=(14,6))


    //TODO Tallenna kuvatiedostona
    #plt.gcf().savefig(os.path.join(ROOT_DIR, 'img', 'rateanalysis.png'), bbox_inches = 'tight')
