from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message(): 
    # Testando a função com valores válidos
    assert encrypt_message("flamengo", 3) == "alf_ognem"
    assert encrypt_message("barcelona", 4) == "anole_crab"

    # Testando a função com uma chave inválida
    with pytest.raises(TypeError):
        encrypt_message("hello world", "invalid_key")

    # Testando a função com uma mensagem inválida
    with pytest.raises(TypeError):
        encrypt_message(12345, 5)

    # Testando a função com uma chave fora do intervalo válido
    assert encrypt_message("hello world", 0) == "dlrow olleh"
    assert encrypt_message("hello world", 50) == "dlrow olleh"

