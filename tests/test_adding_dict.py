import pytest

from dictionary_tools.adding_dict import AddingDict


@pytest.fixture()
def adding_dict():
    return AddingDict({
        'a': 1,
        'b': 2,
        'c': 3
    })


class TestAddingDict(object):

    def test_simple_numbers(self, adding_dict):
        result = adding_dict + AddingDict({'a':1, 'b': 1, 'c': 1})
        assert result['a'] == 2
        assert result['b'] == 3
        assert result['c'] == 4

    def test_adding_to_self(self, adding_dict):
        result = adding_dict + adding_dict

        assert adding_dict['a'] == 1
        assert adding_dict['b'] == 2
        assert adding_dict['c'] == 3

        assert result['a'] == 2
        assert result['b'] == 4
        assert result['c'] == 6

    def test_adding_strings(self):
        result = AddingDict({'a': 'hello, '}) + AddingDict({'a': 'world!'})
        assert result['a'] == 'hello, world!'

    def test_adding_missing_keys(self):
        result = AddingDict({'a': 1}) + AddingDict({'b': 2})
        assert len(result.keys()) == 2
        assert result['a'] == 1
        assert result['b'] == 2

    def test_adding_nested_dictionaries(self):
        first = AddingDict({
            'a': AddingDict({'b': 1})
        })

        second = AddingDict({
            'a': AddingDict({'b': 3})
        })

        result = first + second

        assert result['a']['b'] == 4

    def test_radd(self, adding_dict):

        result = {} + adding_dict
        assert result['a'] == adding_dict['a']
        assert result['b'] == adding_dict['b']
        assert result['c'] == adding_dict['c']

    def test_unsupported_addition(self, adding_dict):
        with pytest.raises(TypeError):
            'string' + adding_dict
