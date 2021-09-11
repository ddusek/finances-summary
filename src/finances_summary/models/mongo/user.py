from datetime import datetime
from mongoengine import Document, StringField, EmailField, DateTimeField


class User(Document):
    """User model.
    """
    current_time = datetime.now()
    username = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    created = DateTimeField(default=current_time)
    last_modified = DateTimeField(default=current_time)

    @classmethod
    def create_new(cls, username: str, email: str, password: str):
        """Create new user.
        """
        user = cls()
        user.username = username
        user.email = email
        user.password = password
        return user
