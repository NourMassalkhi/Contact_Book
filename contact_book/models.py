class Contact:
    def __init__(self, id, name, phone, email, group, added):
        self.id=id
        self.name=name
        self.phone=phone
        self.email=email
        self.group=group
        self.added=added


    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "phone":self.phone,
                "email":self.email,
                "group":self.group,
                "added":self.added,
                }
    
    @classmethod
    def from_dict(cls, data):
        return Contact(
            id=data["id"],
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            group=data["group"],
            added=data["added"]

        )
