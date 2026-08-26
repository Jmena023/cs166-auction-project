  #! /bin/bash
  echo "creating db named ... "$USER"_DB"
  cs166_createdb $USER'_DB'
  cs166_db_status
  cs166_psql $USER'_DB' < phase3.sql
