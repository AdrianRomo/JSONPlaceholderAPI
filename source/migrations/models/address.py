from source.db import Model

class Address(Model):
    __table__ = 'addresses'
    __fillable__ = ['street',
                    'suite',
                    'city',
                    'zipcode',
                    'geo']
    __hidden__ = ['id']
    __casts__ = {
        'geo': 'json'
    }

    def __repr__(self):
        return '<Address id={} street={}>'.format(self.id, self.street)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    def __bool__(self):
        return bool(self.id)

    def __nonzero__(self):
        return self.__bool__()

    def __iter__(self):
        for key in self.__fillable__:
            yield (key, getattr(self, key))

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __delitem__(self, key):
        delattr(self, key)

    def __contains__(self, key):
        return key in self.__fillable__

    def __len__(self):
        return len(self.__fillable__)