// Create Collections.
db.createCollection("users")
db.createCollection("buys")
db.createCollection("sells")

// Create indexes.
db.users.createIndex( { email: -1})
db.users.createIndex( { username: -1})
