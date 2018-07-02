class QueryDictMixin(object):
    """
    Simple query based dictionary mixin.  This extends the standard
    Python dictionary objects to allow you to easily query nested
    dictionaries for a particular value.

    This is especially useful if you don't know the structure beforehand
    allowing you to dynamically receive the path and data set from an
    unknown source.
    """

    path_separator = "/"

    def _get(self, data_dictionary, split_path, default):
        key = split_path.pop(0)

        # Base termination recursion condition if we are at the end of
        # the list of keys.  Return the value or the default value
        if len(split_path) == 0:
            return dict.get(data_dictionary, key, default)

        # If the key doesn't exist then just return the default value
        if key not in data_dictionary.keys():
            return default

        new_target = data_dictionary[key]

        # Finally before we call ourselves again, make sure the value is
        # of base type dictionary.  If not then return the default as
        # we can be at the end of the path yet and we obviously are
        # being called on a non nested dictionary object.
        if not isinstance(new_target, dict):
            return default

        # If we get here start recursion on the new target
        return self._get(new_target, split_path, default)

    def get(self, key, default=None):
        """
        This function replaces python's default "get" definition with
        a custom function.

        The function takes the same arguments as before.  However,
        instead of a single key you can pass in a string which contains
        a list of keys which should be followed to get the value from a
        nested set of dictionaries.  Each key needs to be separated with
        a '/' e.g. 'first/second'.  So this would related to '2' from
        the following data structure:

            {
                "first": {
                    "second": 2
                },
                "third": {}
            }

        Args:
            key (str): The single key or set of keys to the value that
            you would like to get from your dictionary.  If the key is
            more than a single value, then each value needs to be
            separated by '/'.

            default:

        Returns:

        """
        return self._get(self, key.split(self.path_separator), default)


QueryDict = type('QueryDict', (QueryDictMixin, dict), {})
