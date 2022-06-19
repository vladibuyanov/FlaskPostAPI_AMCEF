import pytest
from Backend.function import validation_post_id_user_id


@pytest.mark.parametrize('post_id, user_id, title, body', [
    (1, 1, 'First post', "It's first post"),
    (2, 1, 'Second post', "It's second post")
])
def test_validation_post_id_user_id_positive(post_id, user_id, title, body):
    assert validation_post_id_user_id(post_id, user_id, title, body)


@pytest.mark.parametrize('post_id, user_id, title, body, error', [
    (1, '1', 'First post', "It's first post", AssertionError),
    (1, True, 'First post', "It's first post", AssertionError)
])
def test_validation_post_id_user_id_negative(post_id, user_id, title, body, error):
    with pytest.raises(error):
        assert validation_post_id_user_id(post_id, user_id, title, body)
