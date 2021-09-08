from datetime import datetime
from finances_summary.models.mongo_base import MongoBase


class User(MongoBase):
    """User model.
    """
    def __init__(self):
        super().__init__()
        self.username: str
        self.email: str
        self.password: str
        self.created: datetime
        self.last_modifed: datetime
