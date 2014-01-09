#! /bin/bash

# Configuration
DB_NAME=deepdive_titles
DB_USER=czhang
DB_PASSWORD="Password is set via the PGPASSWORD environment variable"

psql -U $DB_USER -c "CREATE INDEX A ON gene_mentions (docid, sentid);" $DB_NAME
psql -U $DB_USER -c "CREATE INDEX B ON drug_mentions (docid, sentid);" $DB_NAME
