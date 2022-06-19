import pytest
from Backend.function import validation_title_body


@pytest.mark.parametrize('title, body', [('First post', "It's first post")])
def test_validation_title_body_positive(title, body):
    assert validation_title_body(title, body)


@pytest.mark.parametrize('title, body, error', [(1, "It's first post", AssertionError)])
def test_validation_title_body_negative(title, body, error):
    with pytest.raises(error):
        assert validation_title_body(title, body)
