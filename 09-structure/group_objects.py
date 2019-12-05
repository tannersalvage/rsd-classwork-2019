# Creates a dictionary structure to describe relationships
# between a group pof people.
# Object oriented way.


class Person:
    """A class to represent an individual."""
    def __init__(self, name, age, job):
        """Create a new Person with the given name, age and job."""
        self.name = name
        self.age = age
        self.job = job


class Group:
    """A class that represents a group of individuals and their connections."""
    def __init__(self):
        """Create an empty group."""
        self.members = []
        self.connections = {}

    def size(self):
        """Return how many people are in the group."""
        return len(self.members)

    def add_person(self, name, age, job):
        """Add a new person with the given characteristics to the group."""
        self.members.append(Person(name, age, job))
        self.connections[name] = {}

    def connect(self, name1, name2, relation):
        """Connect two given people in a particular way."""
        self.connections[name1][name2] = relation

    def forget(self, name1, name2):
        """Remove the connection between two people."""
        self.connections[name1][name2] = None

    def average_age(self):
        """Compute the average age of the group's members."""
        all_ages = [person.age for person in self.members]
        return sum(all_ages) / self.size()


if __name__ == "__main__":
    # Start with an empty group...
    my_group = Group()
    # ...then add the group members one by one...
    my_group.add_person("Jill", 26, "biologist")
    # ...then their connections
    my_group.connect("Jill", "Zalika", "friend")

    print("The group has {} members with an average age of {}".format(
        my_group.size(),
        my_group.average_age()))