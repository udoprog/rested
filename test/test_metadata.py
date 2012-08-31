import unittest

from rested import Metadata

from mock import Mock

class TestMetadata(unittest.TestCase):
    def setup_metadata(self):
        metadata = Metadata()
        return metadata

    def test_add_entity(self):
        m = self.setup_metadata()
        entity = Mock()
        m.add_entity(entity)
        self.assertTrue(entity.name in m.entities)
