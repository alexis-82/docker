![flag](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/it.png)
# Documentazione Docker con Flask

## Descrizione del Progetto

In questo progetto, utilizziamo Docker per gestire i nostri contenitori e le nostre immagini. Docker è una piattaforma open-source che semplifica la creazione, la distribuzione e l'esecuzione di applicazioni all'interno di contenitori.

## Comandi Principali di Docker

Ecco alcuni dei comandi principali di Docker che potrebbero esserti utili:

- `docker run`: Avvia o aggiorna un contenitore partendo da un'immagine.
- `docker build`: Costruisce un'immagine da un Dockerfile.
- `docker pull`: Scarica un'immagine da Docker Hub o da un registro personalizzato.
- `docker push`: Carica un'immagine su Docker Hub o su un registro personalizzato.
- `docker images`: Visualizza l'elenco delle immagini presenti nel sistema.
- `docker ps`: Mostra l'elenco dei contenitori in esecuzione, -a per visualizzarli tutti.
- `docker exec`: Esegue un comando all'interno di un contenitore in esecuzione.
- `docker images --filter=since=ID`: Mostra l'elenco delle immagini figlie dirette o indirette
- `docker image rmi -f ID`: Eliminazione forzata dell'immagine
- `docker container ls`: Visualizza la lista dei container
- `docker exec -it $nomeContainer /bin/sh`: Entriamo in modalità interattiva, cioè in shell, nel container

## Comandi completi di esempio
- `docker build -t $nomeImmagine .`: Costruzione dell'immagine, il . indica il percorso del file Dockerfile
- `docker run --rm --name $nomeContainer -it $nomeImmagine`: Avviamo il container in un immagine, --rm rimuove il container una volta finito e -it sta per interattivo
- `docker run --rm --name $nomeContainer -it -e myKey=pippo $nomeImmagine`: Con il flag -e specifichiamo una variabile, molto utile per i database
- `docker build -t $nomeContainer .`: Oltre a costruire aggiorna anche il container se modifichiamo il file Dockerfile
- `docker run --rm --name $nomeContainer -it -p 3001:3000 $nomeImmagine`: Con il flag -p specifichiamo le porte host:container (dal browser porta 3001)



## Procedura creazione immagine con container
⚠️ Bisogna avere già installato python3 con pip

Installiamo virtualenv
```
pip install virtualenv
```
Attiviamo l'ambiente env per Linux:
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
![flag](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/gb.png)

# Docker Documentation with Flask

## Project Description

In this project, we use Docker to manage our containers and images. Docker is an open-source platform that simplifies the creation, distribution, and execution of applications within containers.

## Key Docker Commands

Here are some of the key Docker commands that might be useful:

- `docker run`: Starts a container based on an image.
- `docker build`: Builds an image from a Dockerfile.
- `docker pull`: Downloads an image from Docker Hub or a custom registry.
- `docker push`: Uploads an image to Docker Hub or a custom registry.
- `docker images`: Displays a list of images present in the system.
- `docker ps`: Shows the list of running containers, -a to display all.
- `docker exec`: Executes a command within a running container.
- `docker images --filter=since=ID`: Displays the list of direct or indirect child images.
- `docker image rmi -f ID`: Forced deletion of the image.

## Procedure for Creating Image with Container
⚠️ Python3 with pip must be installed beforehand.

Install virtualenv
```
pip install virtualenv
```
Activate the environment env for Linux:
```
cd venv/bin
source activate
```
For Windows 10/11:
```
cd venv
./Script/activate
```
Enter venv environment in Linux:
```
virtualenv venv
```
Enter venv environment in Windows:
```
python -m virtualenv venv
```
Install Flask
```
pip install flask
```
Generate the requirements.txt file directly from venv
```
pip freeze > requirements.txt
```
Check if the app.py code works, we can also use nodemon:
```
python3 app.py
```
or
```
nodemon app.py
```
Build our image by reading the Dockerfile:
```
docker build -t myapp .
```
Now we can start our image with the container using the command:
```
docker run -it --name myapp.container -p 3200:3200 myapp
```
myapp.container = we can give any name to our container




