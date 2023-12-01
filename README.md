# Programació per a la ciència de dades

Aquest paquet conté la solució a PAC4.

El paquet es divideix en 2 carpetes principals i un fitxer:

- `src` Conté tots els exercicis amb els seus corresponents codis.
- `tests` Conté tots els tests de cada exercici.
- `main` És el fitxer principal i el que s'ha d'executar.

ATENCIÓ: Un cop executat el `main` a partir de l'exercici 5, quan es carregui 
el primer plot i ja s'hagi revisat, és necessari tancar la pestanya
per poder obrir el següent plot, d'igual manera en l'exercici 6 pels histogrames.

## Com executar el codi:
A través de la terminal, podem executar diferents ordres a través de comandes.

És possible crear un nou entorn virtual executant:
```
virtualenv venv
```

Per instal·lar els mòduls necessaris s'executa:
```
pip install -r requirements.txt
```

Per executar tots els exercicis, un darrere l'altre s'executa:
```
python3 main.py
```
phyton3 -m venv 


### Proves 
Les proves es poden executar executant:
```
pytest
```

Primer creem un ".coverage" executant:
```
coverage run -m pytest
```

Per veure una vista ràpida dels resultats dels testos s'executa:
```
coverage report
```

Per veure una solució més detallada, s'executa:
```
coverage html
```

Això crearà una carpeta nova, anomenada "htmlcov", amb un resum dels resultats. 
Dins la carpeta ens dirigirem al document anomenat "index.html", 
donarem clic dret i l'obrirem amb el navegador. 
D'aquesta forma serà possible veure amb més detall els resultats.

#### Comandes Addicionals:

Si es dona el cas que no s'executen els plots o histogrames de l'exercici 5/6, s'executa:
```
sudo apt-get install python3-tk
```

Si es dona el cas que no deixa executar directament un coverage, s'executa:
```
python3 -m coverage run --source=src -m pytest
```

Si es dona el cas que no deixa veure una vista ràpida dels resultats, s'executa:
```
python3 -m coverage report
```
