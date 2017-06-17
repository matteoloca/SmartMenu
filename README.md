# SmartMenu
### Per installare le dipendenze
```bash
pip install -r requirements.txt
```
------
### Inizializzare il database
```bash
python manage.py migrate
```
------
### Per creare un utente amministratore
```bash
python manage.py createsuperuser
```
------
### Per avviare il server di debug
```bash
python manage.py runserver
```
------
### Per popolare il db con dati di prova:
##### Svuotare il contenuto del db (opzionale)
```bash
python manage.py flush
```
##### Inserire i dati demo
```bash
python manage.py shell < populate_db.py
```

