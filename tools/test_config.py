#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os,sys

def test_json(json_file="branchs.json"):
    status = None
    if not os.path.exists(json_file):
        status="File not exists!"
    else:
        try:
            json.load(open(json_file))
        except Exception as e:
            print(e)
            status="File is Illegal!"
    return status

if __name__ == "__main__":
    result = test_json()
    if result:
        print(result)
        sys.exit(1)
    else:
        print("Seems all good!")
        sys.exit(0)
