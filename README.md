# Documentazione Docker

## Descrizione del Progetto

In questo progetto, utilizziamo Docker per gestire i nostri contenitori e le nostre immagini. Docker è una piattaforma open-source che semplifica la creazione, la distribuzione e l'esecuzione di applicazioni all'interno di contenitori.

## Comandi Principali di Docker

Ecco alcuni dei comandi principali di Docker che potrebbero esserti utili:

- `docker run`: Avvia un contenitore partendo da un'immagine.
- `docker build`: Costruisce un'immagine da un Dockerfile.
- `docker pull`: Scarica un'immagine da Docker Hub o da un registro personalizzato.
- `docker push`: Carica un'immagine su Docker Hub o su un registro personalizzato.
- `docker images`: Visualizza l'elenco delle immagini presenti nel sistema.
- `docker ps`: Mostra l'elenco dei contenitori in esecuzione, -a per visualizzarli tutti.
- `docker exec`: Esegue un comando all'interno di un contenitore in esecuzione.
- `docker images --filter=since=ID`: Mostra l'elenco delle immagini figlie dirette o indirette
- `docker image rmi -f ID`: Eliminazione forzata dell'immagine

## Procedura creazione immagine con container
⚠️ Bisogna avere già installato python3 con pip

Installiamo virtualenv
```
pip install virtualenv
```
Attiviamo l'ambiente env
Per Linux:
```
cd venv/bin
source activate
```
Per Windows10/11:
```
cd venv
./Script/activate
```
Entrare in ambiente venv in Linux:
```
virtualenv venv
```
Entrare in ambiente venv in Windows:
```
python -m virtualenv venv
```
Installazione di Flask
```
pip install flask
```
Generiamo il file requirements.txt direttamente dal venv
```
pip freeze > requirements.txt
```
Controlliamo se il codice di app.py funziona, possiamo utilizzare anche nodemon:
```
python3 app.py
```
oppure
```
nodemon app.py
```
- 

Costruiamo la nostra immagine tramite la lettura del file Dockerfile:
```
docker build -t myapp .
```
Ora possiamo avviare la nostra immagine con il container tramite il comando:
```
docker run -it --name myapp.container -p 3200:3200 myapp
```
- myapp.container = possiamo dare qualsiasi nome al nostro container


---