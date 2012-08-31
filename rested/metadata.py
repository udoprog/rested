__all__ = ["Metadata"]


class Metadata(object):
    def __init__(self):
        self.entities = dict()

    def add_entity(self, entity, extra=None):
        if entity.name in self.entities:
            raise ValueError(
                "Entity already registered '{0}' ({1})".format(
                    entity.name, extra))

        self.entities[entity.name] = (entity, extra)

    def resolve_entity(self, entity_name):
        entity_data = self.entities.get(entity_name)

        if entity_data is None:
            raise KeyError("No entity registered with name '{0}'".format(
                entity_name))

        entity, extra = entity_data

        entity.check()

        relations = list()

        for relation in entity.relations:
            relations.append((relation, self.resolve_entity(relation.ref)))

        return entity, relations
