#!/usr/bin/env python
from rested import Metadata
from rested import Field
from rested import Argument
from rested import Entity
from rested import Action

from rested.types import Integer

from rested.relation import with_many
from rested.relation import has_many

from rested.brokers import HttpBroker

metadata = Metadata()

metadata.add_entity(Entity(
    "Person",
    has_many("addresses", "Address",
             help="Set addresses for {entity.name}"),
    with_many("otheraddresses", "Address",
              help="Set other addresses for {entity.name}"),
    Field("height", Integer, required=False, default=32),
    Action("merge",
           Argument("a", help="Merge person a"),
           Argument("b", help="Merge person b"),
           help="Merge this user with another",
           method="write",
           action_type="collection"),
    help="A person on a remote system",
    plural="people"
))

metadata.add_entity(Entity(
    "Address",
    Field("street", help="Street associated with address"),
    Field("country", help="Country associated with address"),
    help="An address associated to a person",
    plural="addresses"
))


class HttpEcho(object):
    def __init__(self, url):
        self.url = url

    def request(self, uri_name, method, uri, body):
        print "REQUEST({0}) {1}:{2} <{3}>".format(uri_name, method, uri, body)

if __name__ == "__main__":
    import sys
    from rested.parsers import create_restful_parser

    sys.path.insert(0, ".")
    broker = HttpBroker(impl=HttpEcho(":local:"))
    entity, relations = metadata.resolve_entity("Person")
    parser = create_restful_parser(entity, relations)
    ns = parser.parse_args()
    broker.run(ns)
