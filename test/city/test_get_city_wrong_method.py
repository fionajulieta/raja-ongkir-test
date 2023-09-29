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
    req = requests.post(API_CITY, headers=head)
    #jadi kita sengaja salahin methodnya (negative scenario) dari hrsnya post jadi get. trs kita taro di assertnya
    #di assertnya ini kita taro status code equal to 400, jadi kalo statusnya 400 brati negative scenarionya passed
    #print(req.json())

   # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    print(description)

    # ASSERT
    assert_that(status_code).is_equal_to(400)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("Unknown method. Method tidak ditemukan, harap baca dokumentasi dengan baik.")