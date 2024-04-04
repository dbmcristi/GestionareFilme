from teste.testClient import testClient
from teste.testClientRepository import testAdaugaClientRepository
from teste.testClientRepository import testStergeClientRepo

def testAll():
    testClient()
    testAdaugaClientRepository()
    testStergeClientRepo()