// Create Collections.
db.createCollection("users")
db.createCollection("userTransactions")
db.createCollection("commodities")

// Create indexes.
db.users.createIndex( { email: -1})
db.users.createIndex( { username: -1})
db.commodities.createIndex( { symbol: -1 } )