#! /bin/bash

# Configuration
DB_NAME=deepdive_titles
DB_USER=czhang
DB_PASSWORD="Password is set via the PGPASSWORD environment variable"

psql -U $DB_USER -c "update gene_mentions t0 SET is_correct=False FROM gene_mentions t1 \
                     WHERE t0.repr=t1.repr AND t0.docid=t1.docid AND t1.is_correct=False \
                     AND t0.is_correct IS NULL;" $DB_NAME



