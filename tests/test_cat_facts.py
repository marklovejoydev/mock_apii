from unittest.mock import Mock
from lib.challenge.cat_facts import CatFacts

def test_cat_facts_api():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"Cats are not as good as dogs"
    }
    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: Cats are not as good as dogs"