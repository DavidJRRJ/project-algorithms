from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
  
    assert encrypt_message("abcde", 2) == "bacde_edcba"
    assert encrypt_message("1234567", 3) == "321_7654"

    assert encrypt_message("abcde", 6) == "edcba"

    with pytest.raises(TypeError):
        encrypt_message("abcde", "2")

    with pytest.raises(TypeError):
        encrypt_message(12345, 2)
