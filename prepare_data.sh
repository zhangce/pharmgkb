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


psql -U $DB_USER -c "CREATE TABLE docids (id bigserial primary key, \
										  docid text,               \
										  folder text);"     $DB_NAME

psql -U $DB_USER -c "CREATE TABLE documents (id   bigserial primary key, \
											docid  text,                  \
											document   text);"                $DB_NAME

psql -U $DB_USER -c "CREATE TABLE sentences (id   bigserial primary key, \
											docid  text,                  \
											sentid text,                   \
											sentence   text);"                $DB_NAME

psql -U $DB_USER -c "CREATE TABLE drug_mentions (id   bigserial primary key, \
											docid        text,           \
											sentid       text,
											mid          text,                  \
											start_wid    int,
											end_wid      int,
											type         text,                   \
											is_correct   boolean,                   \
											repr         text,					\
											features     text[],                \
											object       text);"					$DB_NAME

psql -U $DB_USER -c "CREATE TABLE gene_mentions (id   bigserial primary key, \
											docid        text,           \
											sentid       text,
											mid          text,                  \
											start_wid    int,
											end_wid      int,
											type         text,                   \
											is_correct   boolean,                   \
											repr         text,					\
											features     text[],                \
											object       text);"					$DB_NAME

psql -U $DB_USER -c "CREATE TABLE relations (id   bigserial primary key, \
											type             text,
											mid1          text,                  \
											mid2          text,                \
											is_correct       boolean,            \
											features       text[]);"					$DB_NAME





















