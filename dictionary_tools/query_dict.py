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

        if len(split_path) == 1:
            return dict.get(data_dictionary, split_path[0], default)

        if split_path[0] not in data_dictionary.keys():
            return default

        return self._get(
            data_dictionary[split_path[0]],
            split_path[1:],
            default
        )

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
