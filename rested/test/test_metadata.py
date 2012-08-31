import unittest

from rested.relation import OneToMany
from rested import Metadata
from rested import Field
from rested import Entity

class TestRelation(unittest.TestCase):
    def setup_metadata(self):
        metadata = Metadata()

        metadata.add_entity(Entity(
            "Person",
            OneToMany("addresses", ref="Address", description="Set addresses for {entity.name}"),
            Field("height", field_type=int),
            description="Person"
        ))

        metadata.add_entity(Entity(
            "Address",
            Field("street", description="Street associated with address"),
            Field("country", description="Country associated with address"),
            description="An address associated to a person"
        ))

        return metadata

    def test_missing_entity(self):
        metadata = self.setup_metadata()
        self.assertRaises(KeyError, metadata.build, "Missing")

    def test_building_cli(self):
        metadata = self.setup_metadata()
        parser = metadata.build("Person")
        result = parser.parse_args(["create", "--height", "42"])

        print result

if __name__ == "__main__":
    unittest.main()
