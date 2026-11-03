import uuid
from datetime import datetime

class BaseEntity():
    def __init__(self,id,is_deleted,created_by,date_created):
        self.id:uuid=uuid.uuid4()
        self.is_deleted=is_deleted

    