// Create Collections.
db.createCollection("users")
db.createCollection("user_transactions")
db.createCollection("commodities")
db.createCollection("commodity_prices")
db.createCollection("commodity_statuses")

// Create indexes.
db.users.createIndex( { email: -1})
db.users.createIndex( { username: -1})
db.commodities.createIndex( { symbol: -1 } )