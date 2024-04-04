'''
test clasa Client
'''
from domeniu.client import Client
def testClient():
    client = Client("1", "Simon", "Ana", "5123123", "f", 19)

    assert client.getIdClient() == "1"
    assert client.getnumeClient() == "Simon"
    assert client.getPrenumeClient() == "Ana"
    assert client.getCNPClient() == "5123123"
    assert client.getSexClient() == "f"
    assert client.getVarstaClient() == 19


def testClientSetteri():
    client = Client("1", "Simon", "Ana", "5123123", "f", 19)

    client.setIdClient("2")
    assert client.getIdClient() == "2"

    client.setNumeClient("Dodu")
    assert client.getnumeClient() == "Dodu"

