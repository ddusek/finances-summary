// Create Collections.
db.createCollection("users")
db.createCollection("userTransactions")
db.createCollection("stocks")
db.createCollection("news")

// Create indexes.
db.users.createIndex( { email: -1})
db.users.createIndex( { username: -1})
