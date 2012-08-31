#!/usr/bin/python

from rested.relation import OneToMany
from rested import Metadata
from rested import Field
from rested import Entity

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

if __name__ == "__main__":
    import sys
    sys.path.insert(".")

    parser = metadata.build("Person")
    result = parser.parse_args()
