from bson.objectid import ObjectId


class MongoBase():
    """Base model for Mongo objects. Every Mongo object inherits from this.
    """
    def __init__(self):
        self._id:  ObjectId
