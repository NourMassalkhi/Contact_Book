class ContactBookError (Exception):
    pass
class ValidationError (ContactBookError):
    pass
class StorageError (ContactBookError):
    pass
