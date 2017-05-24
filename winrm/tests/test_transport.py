# coding=utf-8
from winrm.transport import Transport
import os

def test_build_session():
    origEnviron = os.environ
    os.environ['REQUESTS_CA_BUNDLE'] = 'MyRequestsCA'
    transport = Transport(endpoint="Endpoint")
    # temporarily set the CA environment variable
    session = transport.build_session()
    assert(session.verify == 'MyRequestsCA')
    os.environ = origEnviron 
    os.environ['CURL_CA_BUNDLE'] = 'MyCurlCA'
    assert(session.verify == 'MyCurlCA')
    os.environ = origEnviron 
