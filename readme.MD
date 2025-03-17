# Progetto Industriale ISTAT Data ETL Pipeline

Questa repository contiene una piccola pipeline ETL a microservizi containerizzata con docker per estrarre, pulire e caricare dei dati sul turismo ligure ricavati dall'endpoint REST esploradati dell'ISTAT.

## 📂 Struttura Progetto

├── migrations/ Contiene la configurazione e le migrazioni alembic necessarie a ricreare lo schema del database
├── clean_and_load/ Contiene script python per scaricare, pulire e caricare i dati ISTAT sul db.
├── docker/ Contiene i file docker necessari per la containerezzizazione e orchestrazione della pipeline.
│ ├── Dockerfile.migrations
│ ├── Dockerfile.clean_load
│ ├── docker-compose.yml
