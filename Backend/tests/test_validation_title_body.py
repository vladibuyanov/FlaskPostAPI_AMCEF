import pytest
from Backend.function import validation_title_body


@pytest.mark.parametrize('title, body', [('First post', "It's first post")])
def test_validation_title_body(title, body):
    assert validation_title_body(title, body)


# @pytest.mark.parametrize('title, body, error', [('First post', "It's first post")])
