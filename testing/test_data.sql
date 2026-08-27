COPY users
FROM 'users_test.dat'
WITH DELIMITER ',';

COPY item
FROM 'item_test.dat'
WITH DELIMITER ',';

COPY auction
FROM 'auction_test.dat'
WITH DELIMITER ',';

COPY bid
FROM 'bid_test.dat'
WITH DELIMITER ',';