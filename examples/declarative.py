#!/usr/bin/env python
from rested import Field

from rested.types import String
from rested.types import FieldType

from rested.relation import has_many
from rested.relation import has_one

from rested.broker.http import HttpBroker

from rested.ext.declarative import declarative_base

Base = declarative_base()


class ZipCode(FieldType):
    metavar = "zipcode"

    def __call__(self, value):
        return value


class Person(Base):
    __entity_args__ = dict(
        help="A single person",
        plural="people"
    )

    address = has_one("Address")
    cars = has_many("Car")


class Car(Base):
    __entity_args__ = dict(
        help="A car related to a person",
        plural="cars"
    )

    name = Field(String)


class Address(Base):
    __entity_args__ = dict(
        help="The address associated to a person",
        plural="addresses"
    )

    country = Field(String, help="Address country")
    state = Field(String, help="Address state")
    zipcode = Field(ZipCode, help="Address zipcode")


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
    entity, relations = Person.resolve()
    parser = create_restful_parser(entity, relations)
    ns = parser.parse_args()
    print ns.which
    broker.run(ns)
