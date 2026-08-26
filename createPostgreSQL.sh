#! /bin/bash
echo "creating db named ... auction_db"
createdb -h localhost -p $PGPORT auction_db
pg_ctl status

echo "Initializing tables ..."
sleep 1
psql -h localhost -p $PGPORT auction_db < phase3.sql