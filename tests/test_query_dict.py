import pytest

from dictionary_tools.query_dict import QueryDict


@pytest.fixture()
def query_dict():
    return QueryDict({
        'first': '1',
        'second': {
            'sub_second': '2'
        },
        'third': {}
    })


class TestQueryDict(object):

    @pytest.mark.parametrize('path, value',[
        ('first', '1'),
        ('second/sub_second', '2'),
        ('third', {})
    ])
    def test_valid_paths(self, query_dict, path, value):
        assert query_dict.get(path) == value

    @pytest.mark.parametrize('path', [
        'a',
        'first/a',
        'second/sub_second/a',
        'a/sub_second'
    ])
    def test_invalid_paths(self, query_dict, path):
        assert query_dict.get(path) is None
