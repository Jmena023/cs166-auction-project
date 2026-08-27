SELECT COUNT(*)
FROM item
WHERE category = 'Electronics';

SELECT COUNT(*)
FROM auction
WHERE auction_status = 'Active';

SELECT COUNT(*)
FROM bid
WHERE auction_id = 1001;

SELECT COUNT(*)
FROM bid
WHERE buyer_login = 'buyer10';

SELECT COUNT(*)
FROM item
WHERE seller_login = 'seller10';