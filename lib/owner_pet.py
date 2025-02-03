class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner's list of pets."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

        if isinstance(owner, Owner):
            owner.add_pet(self)


# Example usage
owner1 = Owner("Alice")
pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Max", "cat", owner1)

# Adding another pet
owner1.add_pet(Pet("Charlie", "bird", owner1))

# Getting sorted list of pets by name
sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)