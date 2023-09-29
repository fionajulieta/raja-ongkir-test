import json
import requests
from assertpy import assert_that
from jsonschema import validate as validate_json_schema

from jsonschemas.schema_cost import *
from setting.endpoint import API_COST
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    payload = {
    "origin" : "1",
    "destination" : "60",
    "weight" : 1000,
    "courier" : "tiki"
    }
    req = requests.post("https://api.rajaongkir.com/starter/costtttt", headers=head, json=payload)


    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds

    # ASSERT
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)

