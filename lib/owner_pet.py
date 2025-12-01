class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.pet_type = pet_type
        self.owner = None 
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner")
            owner.add_pet(self) 
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    def pets(self):
        """Return all pets belonging to this owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a Pet instance to this owner."""
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self  
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return owner's pets sorted by name."""
        return sorted(self._pets, key=lambda p: p.name)