#! /bin/bash

# Configuration
DB_NAME=deepdive_titles
DB_USER=czhang
DB_PASSWORD="Password is set via the PGPASSWORD environment variable"

cd `dirname $0`
BASE_DIR=`pwd`

#dropdb -U $DB_USER deepdive_titles

#createdb -U $DB_USER deepdive_titles

psql -U $DB_USER -c "drop schema if exists public cascade; create schema public;" $DB_NAME


psql -U $DB_USER -c "CREATE TABLE documents (id   bigserial primary key, \
											docid  text,                  \
											candidate_gene_mentions   text,                   \
											candidate_drug_mentions   text,                   \
											candidate_motabolite_mentions   text,                   \
											candidate_relation_mentions   text,                   \
											dependencies              text);"                $DB_NAME


psql -U $DB_USER -c "CREATE TABLE mentions (id   bigserial primary key, \
											mid          text,                  \
											type         text,                   \
											is_correct   boolean,                   \
											repr         text);"					$DB_NAME


psql -U $DB_USER -c "CREATE TABLE dependencies (id   bigserial primary key, \
											mid1          text,                  \
											mid2         text,                   \
											feature   text);"					$DB_NAME


psql -U $DB_USER -c "CREATE TABLE mention_features (id   bigserial primary key, \
											mid          text,                  \
											feature      text);"					$DB_NAME


psql -U $DB_USER -c "CREATE TABLE relations (id   bigserial primary key, \
											type             text,
											gene_id          text,                  \
											drug_id          text,                \
											is_correct       boolean);"					$DB_NAME


psql -U $DB_USER -c "CREATE TABLE relation_features (id   bigserial primary key, \
											type             text,
											gene_id          text,                  \
											drug_id          text,
											feature          text);"					$DB_NAME






















