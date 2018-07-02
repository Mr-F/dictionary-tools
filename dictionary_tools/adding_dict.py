class AddingDictMixin(object):
    """
    This Mixin defined the operator which allows for the '+' operator
    to be defined to a dictionary.
    """

    def __add__(self, value):
        """
        This '+' operator override, defines exactly how to combine two
        dictionaries together.  As long as 'value' is of type 'dict'
        this function will loop through all the keys and attempt to add
        the values together.  This addition does not make any promises
        as how the key values can be added, and if it's type doesn't
        support __add__ or __radd__ then the type exception will
        propagate to the caller.

        If the type of parameter 'value' is not a dict type then this
        function will raise a new TypeError exception.

        :param value:
        :return:
        """
        if isinstance(value, dict):
            data = type(self)()
            for key in self.keys():
                data[key] = self[key] + value.get(key, 0)

            for key in value.keys():
                if key not in self:
                    data[key] = value[key]
            return data

        raise TypeError('Unsupported operand type(s) for +: {} and {}'.format(
            type(self), type(value)
        ))

    def __radd__(self, other):
        """
        If Python tries to perform a reverse add an instance of this
        class, simple call the __add__ definition.

        :param other:
        :return:
        """
        return self.__add__(other)


AddingDict = type('AddingDict', (AddingDictMixin, dict), {})
