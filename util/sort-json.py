#!/usr/bin/env python

import json
import sys
from collections import OrderedDict

DICT_DELIM = '='
LIST_DELIM = ','

def read_all():
	return "".join(sys.stdin.readlines())

def to_str(x):
	if isinstance(x, str):
		return x

	if type(x) in {int, float, bool}:
		return str(x)

	if isinstance(x, dict):
		sorted_keys = sorted("(" + to_str(k) + DICT_DELIM + to_str(x[k]) + ")" for k in x.keys())
		return LIST_DELIM.join(sorted_keys)

	if isinstance(x, list):
		sorted_values = sorted([to_str(i) for i in x])
		return  "(" + LIST_DELIM.join(sorted_values) + ")"

	return "null"


def sort_obj(obj):
	if isinstance(obj, list):
		return sorted([sort_obj(i) for i in obj], key=to_str)

	if isinstance(obj, dict):
		sorted_keys = sorted(obj.keys())
		return OrderedDict((k, sort_obj(obj[k])) for k in sorted_keys)

	return obj


print(json.dumps(sort_obj(json.loads(read_all()))))
