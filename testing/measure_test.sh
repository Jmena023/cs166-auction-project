#!/bin/bash

cp -a *.dat $PGDATA/

cs166_psql $USER'_DB' < ../phase3.sql
cs166_psql $USER'_DB' < test_data.sql

psql -h localhost -p $PGPORT $USER'_DB' <<EOF > /dev/null
DROP INDEX IF EXISTS idx_item_category;
DROP INDEX IF EXISTS idx_auction_status;
DROP INDEX IF EXISTS idx_bid_auction;
DROP INDEX IF EXISTS idx_bid_buyer;
DROP INDEX IF EXISTS idx_item_seller;
EOF

echo "Query time without indexes"

cat <(echo '\timing') queries.sql | \
psql -h localhost -p $PGPORT $USER'_DB' | \
grep Time | \
awk -F "Time" '{print "Query" FNR $2;}'

psql -h localhost -p $PGPORT $USER'_DB' < create_indexes.sql > /dev/null

echo "Query time with indexes"

cat <(echo '\timing') queries.sql | \
psql -h localhost -p $PGPORT $USER'_DB' | \
grep Time | \
awk -F "Time" '{print "Query" FNR $2;}'