from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    messages = ["qwerty", 1]
    keys = [3, 4, 9, "qwerty"]

    assert encrypt_message(messages[0], keys[0]) == "ewq_ytr"
    assert encrypt_message(messages[0], keys[1]) == "yt_rewq"
    assert encrypt_message(messages[0], keys[2]) == "ytrewq"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(messages[0], keys[3])
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(messages[1], keys[0])
