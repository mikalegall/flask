PYTHON DEPLOYMENT
<br>
Suorita edullisella internet vuokrapalvelimella (Linodella 5e/kk Linux Debian 10) kommennot

    sudo apt-get update
    sudo apt-get -y install ufw
    sudo ufw allow 22/tcp
    sudo ufw enable
    sudo apt upgrade

    sudo adduser YOUR_NAME
    sudo adduser YOUR_NAME sudo

    ssh YOUR_NAME@YOUR_IP
    sudo apt install tree
    sudo usermod --lock root #Lukitse käyttäjä

***************************************************************

#Muodosta ryhmä, jonka jäsenet saavat suorittaa ohjelmakoodia ryhmän kotihakemistossa

    sudo adduser flaskwsgi
    sudo usermod --lock flaskwsgi #Lukitse käyttäjä

    sudo mkdir /home/flaskwsgi/public_wsgi/ #Sijainti ryhmän kotihakemistossa suoritettavalle koodille
    sudo chown flaskwsgi:flaskwsgi /home/flaskwsgi/public_wsgi/
    sudo chmod g+rwxs /home/flaskwsgi/public_wsgi/ #Ryhmän jäsenille kirjotusoikeus ryhmän kotihakemistossa alihakemistoihin 
    sudo adduser YOUR_NAME flaskwsgi
#Kirjaudu ulos ja takaisin sisään, jotta muutokset astuvat voimaan
<br>
##newgrp flaskwsgi #Ottaa käyttöön uuden shellin (ikäänkuin olisi kirjautunut välissä ulos)

    whoami
    groups
    pwd
    ls -la

#Kokeile pystytkö kirjoittamaan omalla käyttäjällä ilman sudoa ryhmän kotihakemistossa kohteeseen

    nano /home/flaskwsgi/public_wsgi/onnistuiko.txt
    ls -la /home/flaskwsgi/public_wsgi/
    cat /home/flaskwsgi/public_wsgi/onnistuiko.txt
    rm /home/flaskwsgi/public_wsgi/onnistuiko.txt

***************************************************************

#Lisää kehityskoneella koodirepon juureen tiedosto nimeltä 

    flask.wsgi
#ja tallenna sen sisällöksi

    import sys
    assert sys.version_info.major >= 3

    sys.path.insert(0, '/home/flaskwsgi/public_wsgi/')
    from app import app as application

#KOPIOI TOIMIVAN OHJELMAN KOKO SISÄLTÖ RYHMÄN KOTIHAKEMISTOON
<br>
##Siirrä kehityskoneella kaikki konfigurointiin liittyvä erilaiseksi kuin harjoituksissa on tallennettu versionhallintaan
<br>
###esim. app.secret_key jne. kuten tietokannan käyttäjän nimi (tietokannan nimi)

    scp /home/kyy/flask/technical_analysis/flask.wsgi YOUR_NAME@YOUR_IP:/home/flaskwsgi/public_wsgi/

    scp /home/kyy/flask/technical_analysis/app.py YOUR_NAME@YOUR_IP:/home/flaskwsgi/public_wsgi/

    scp -r /home/kyy/flask/technical_analysis/templates YOUR_NAME@YOUR_IP:/home/flaskwsgi/public_wsgi/

    scp -r /home/kyy/flask/technical_analysis/static/images/ YOUR_NAME@YOUR_IP:/home/flaskwsgi/public_wsgi/static/images

    scp -r /home/kyy/flask/technical_analysis/services YOUR_NAME@YOUR_IP:/home/flaskwsgi/public_wsgi/

***************************************************************

Suorita internet palvelimella kommennot

    sudo apt install python3
    sudo apt install python3-flask
    sudo apt install python3-flask-sqlalchemy
    sudo apt install python3-wtforms
    sudo apt install python3-flaskext.wtf

--X--X--

    sudo apt install python3-pandas
    sudo apt install python3-matplotlib
    sudo apt install python3-seaborn

    sudo apt install python3-pip
    pip3 install pandas_datareader

***************************************************************

    sudo apt-get -y install postgresql
    sudo systemctl restart postgresql
    sudo -u postgres createdb YOUR_NAME
    sudo -u postgres createuser YOUR_NAME
    psql
    select (1+1); #Testaa toimiikoo tietokannan hallintaohjelma Postgre
    exit

    sudo apt-get -y install python3-psycopg2

***************************************************************

    sudo apt install apache2
    sudo systemctl start apache2
    sudo ufw allow 80/tcp
    sudo /sbin/apache2ctl configtest

    sudo tail /var/log/apache2/access.log | nl
    sudo tail /var/log/apache2/error.log | nl

#Luo palvelimella tiedosto

    sudo nano /etc/apache2/sites-available/flask.conf
#ja tallenna sen sisällöksi

    <VirtualHost *:80>
            ServerName flasktest.example.com

            WSGIDaemonProcess flask.wsgi user=YOUR_NAME group=flaskwsgi threads=5
            WSGIScriptAlias / /home/flaskwsgi/public_wsgi/flask.wsgi

            <Directory /home/flaskwsgi/public_wsgi/>
                    WSGIScriptReloading On
                    WSGIProcessGroup flask.wsgi
                    WSGIApplicationGroup %{GLOBAL}
                    Require all granted
            </Directory>
    </VirtualHost>


    sudo a2dissite 000-default.conf
    sudo a2ensite flask.conf
    sudo systemctl restart apache2
    sudo apt install libapache2-mod-wsgi-py3
    sudo systemctl restart apache2
#sudo tail /var/log/apache2/error.log | nl
<br>
#sudo systemctl status apache2.service -l --no-pager
<br>
#journalctl -r
<br>
##sudo journalctl -u apache2.service --since today --no-pager

    sudo touch /home/flaskwsgi/public_wsgi/flask.wsgi

