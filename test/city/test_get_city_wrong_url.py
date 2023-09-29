import json
import requests
from assertpy import assert_that
import pytest
from setting.endpoint import API_CITY
from setting.general import api_key, max_latency
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_city import *


def test():
    head = {
        "key": api_key
    }
    req = requests.post("https://api.rajaongkir.com/starter/cities", headers=head)
    #jadi kita sengaja salahin API linknya (negative scenario). trs kita taro di assertnya
    #di assertnya ini kita taro status code equal to 404, jadi kalo statusnya 404 brati testnya passed

    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds

    # ASSERT
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)