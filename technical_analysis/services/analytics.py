# Tuodaan käytettäväksi data-analytiikan kirjasto pandas ja lyhennetään sitä kutsuttavaksi aliaksella pd
# https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe
import pandas as pd # sudo apt install python3-pandas

# Tuodaan graafiseen esittämiseen matplotlib ja sen käyttöliittymäksi pyplot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#module-matplotlib.pyplot
import matplotlib.pyplot as plt # sudo apt install python3-matplotlib && sudo apt install python3-seaborn


# Tuodaan käytettäväksi internetistä datan noutaja esim. Yahoo Financesta valuuttakursseille
# https://pydata.github.io/pandas-datareader/remote_data.html#forex
# DataReadilla noudetuissa tiedoissa on aikaleima valmiina indeksissä
import pandas_datareader as web
###sudo apt install python3-pip
###pip3 install pandas_datareader
###conda install -c anaconda pandas-datareader
###VS codessa Ctrl+P  ext install ms-python.python
### pip install pandas-datareader
#git clone https://github.com/pydata/pandas-datareader.git
#cd pandas-datareader
#sudo python3 setup.py install


import os
from pathlib import Path
# Ajan käsittelyyn tarvittavia kirjastoja
#from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


# Two level up
ROOT_DIR = Path(__file__).parent.parent

def analyze(target, short_rolling_mean, long_rolling_mean):
    print("target = ", target, "short_rolling_mean = ", short_rolling_mean,  "long_rolling_mean = ", long_rolling_mean)
    # Hae kohde-etuuden tunniste noudetettavasta kohteesta
    # https://duckduckgo.com/?q=yahoo+finance+elisa
    # https://duckduckgo.com/?q=yahoo+finance+nordea+bull+dax+10
    try:
        target_data = web.DataReader(target, start='2015-1-1', data_source='yahoo')
    except Exception as e:
        print("EXCEPTION e = ", e)

    print("target_data = ", target_data)
    # Valitaan graafinen esittäminen muotoiltavaksi tietyllä tyylillä
    plt.style.use('seaborn-whitegrid')

    #Suurennetaan esitysaluetta oletuskoostaan suuremmaksi
    target_data['Close'].plot(figsize=(14,6))
    #Satunnaisvaihtelun tasaamiseen voidaan laskea liukuva keskiarvo
    # https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp
    ##Liukuva keskiarvo voi olla singnaalina toimenpiteelle
    ##Jatkuvasti rullaava (liukuva, rolling) komento rolling() ottaa parametrikseen ajankohtien lukumäärän
    ###Lasketaan 50 viimeiselle päivälle jatkuvasti päivittyvänä (rullaavana, liukuvana) keskiarvo komennolla mean()
    target_data['Close'].rolling(int(short_rolling_mean)).mean().plot(title=target)
    #Samaan visualisointiin voidaan plotata (graafisesti esitettäväksi) useampia kaavioita samanaikaisesti
    ##Lasketaan Elisan osakkeen päätösluvulle 200 päivän liukuva keskiarvo
    target_data['Close'].rolling(int(long_rolling_mean)).mean().plot()

    #Remove old figure
    # rateanalysis = os.path.join(ROOT_DIR, 'static', 'images', 'rateanalysis.png')
    # try:
    #     os.remove(rateanalysis)
    # except Exception as e:
    #     print("EXCEPTION e = ", e)
    
    #Save figure
    ##Figure https://tilastoapu.wordpress.com/2019/07/02/kuviot-ja-kaaviot-pythonilla/
    ###Get current figure (plt.gct)
    #### https://video.haaga-helia.fi/media/Data-analytiikka+Zoom-tallenne+21.4.2021/0_xj9pcn3d
    try:
        plt.gcf().savefig(os.path.join(ROOT_DIR, 'static', 'images', 'rateanalysis.png'), bbox_inches = 'tight')
        plt.close()
    except Exception as e:
        print("EXCEPTION e = ", e)
    #Ilman lisäparametria bbox_inches='tight' saattaa kuvion reunoilta jäädä osa tallentumatta
    ## https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html


    #Usein tarkoituksenmukaisempaa on tarkastella muutosta prosentuaalisena
    ##Luodaan DataFrameen uusi sarake nimeltä "Elisa %" ja sijoitettaan sen arvoksi
    ##taulukon "Close" sarakkeesta komennolla "pct_change()" laskettu prosentuaalinen muutos
    ##Muutos on verrattuna edelliseen eli tässä tapauksessa edelliseen pörssinkäyntipäivään
    target_data['percent'] = target_data['Close'].pct_change()
    #Liitetään konkatenoinnilla juuri luodut muutosprosentti-sarakket kolmanteen taulukkoon
    #muutokset = pd.concat([elisa['Elisa %'], telia['Telia %']], axis = 1)
#changes = target_data['percent']
    #Vuosittaisen volatiliteetin muutosprosentin keskihajonta jatkuvasti rullaava (liukuva, rolling)
    ##Komento rolling() ottaa parametrikseen ajankohtien lukumäärän
    ##Lasketaan vuoden kaupantekopäivien (252 päivää) muutosprosenteille jatkuvasti päivittyvänä (rullaavana, liukuvana)
    ##keskihajonta (standard deviation) komennolla std() ja skaalataan se neliöjuurella kertomalla vuosittaiseksi
    ##sekä esitetään se plotaten graafisena visualisointina (lopulta suurennetaan esitysaluetta oletuskoostaan suuremmaksi)
#(changes['percent'].rolling(252).std() * (252**0.5)).plot(label = target, legend = True, figsize=(14,6))
    (target_data['percent'].rolling(252).std() * (252**0.5)).plot(label = target, legend = True, figsize=(14,6))

    #Remove old figure
    # rateanalysis = os.path.join(ROOT_DIR, 'static', 'images', 'volatilite.png')
    # try:
    #     os.remove(rateanalysis)
    # except Exception as e:
    #     print("EXCEPTION e = ", e)

    #Save figure
    ##Figure https://tilastoapu.wordpress.com/2019/07/02/kuviot-ja-kaaviot-pythonilla/
    ###Get current figure (plt.gct)
    #### https://video.haaga-helia.fi/media/Data-analytiikka+Zoom-tallenne+21.4.2021/0_xj9pcn3d
    try:
        plt.gcf().savefig(os.path.join(ROOT_DIR, 'static', 'images', 'volatilite.png'), bbox_inches = 'tight')
        plt.close()
    except Exception as e:
        print("EXCEPTION e = ", e)
    #Ilman lisäparametria bbox_inches='tight' saattaa kuvion reunoilta jäädä osa tallentumatta

    return "services.analytics.analyze == done"
