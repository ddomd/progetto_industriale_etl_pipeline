# Progetto Industriale ISTAT Data ETL Pipeline

Questa repository contiene una piccola pipeline ETL a microservizi containerizzata con docker per estrarre, pulire e caricare dei dati sul turismo ligure ricavati dall'endpoint REST esploradati dell'ISTAT.

## 📂 Struttura Progetto

```bash
├── migrations/ # Contiene la configurazione e le migrazioni alembic necessarie a ricreare lo schema del database
├── clean_and_load/ # Contiene script python per scaricare, pulire e caricare i dati ISTAT sul db.
├── docker/ # Contiene i file docker necessari per la containerezzizazione e orchestrazione della pipeline.
│ ├── Dockerfile.migrations
│ ├── Dockerfile.clean_load
│ ├── docker-compose.yml
```

## 🚀 Funzionamento

1. **Inizializzazione Database:**

   - Inizializza un container postgres.
   - Ferma le successive esecuzione finchè il container non è healthy.

2. **Migrazioni Schema:**

   - Una volta che il database è inizializzato ed accetta connessioni vengono caricate le migrazione Alembic per costruire schema e tavole.
   - Le migrazioni sono costruite in modo da creare uno star schema usando le codelist ISTAT come dimensioni per filtrare le tavole dei fatti.

3. **ETL:**
   - Dopo che il database è stato creato correttamente e le migrazioni sono state eseguite con successo inizia i l processo ETL.
   - I dati vengono scaricati da esploradati con più richieste asincrone e vengono ripuliti con l'uso di pandas in modo da poter essere inseriti nel db.
