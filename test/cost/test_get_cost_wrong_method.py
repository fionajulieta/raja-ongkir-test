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
    req = requests.get(API_COST, headers=head, json=payload)


    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    print(description)

    # ASSERT
    assert_that(status_code).is_equal_to(400)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("Unknown method. Method tidak ditemukan, harap baca dokumentasi dengan baik.")
