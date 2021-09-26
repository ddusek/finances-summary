from dataclasses import dataclass, asdict


@dataclass
class BaseResponse():
    """Class inherited for all response models.
    """
    def as_dict(self):
        """Convert dataclass to dict
        """
        return asdict(self)
