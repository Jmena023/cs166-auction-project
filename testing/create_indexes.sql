DROP INDEX IF EXISTS idx_item_category;
DROP INDEX IF EXISTS idx_auction_status;
DROP INDEX IF EXISTS idx_bid_auction;
DROP INDEX IF EXISTS idx_bid_buyer;
DROP INDEX IF EXISTS idx_item_seller;

CREATE INDEX idx_item_category
ON item(category);

CREATE INDEX idx_auction_status
ON auction(auction_status);

CREATE INDEX idx_bid_auction
ON bid(auction_id);

CREATE INDEX idx_bid_buyer
ON bid(buyer_login);

CREATE INDEX idx_item_seller
ON item(seller_login);