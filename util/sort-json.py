#!/usr/bin/env python

import json
import sys

def read_all():
	return "".join(sys.stdin.readlines())

def to_str(x):
	if type(x) in {str, int, float, bool}:
		return json.dumps(x)

	if isinstance(x, dict):
		sorted_items = sorted(to_str(k) + ":" + to_str(x[k]) for k in x.keys())
		return "{" + ",".join(sorted_items) + "}"

	if isinstance(x, list):
		sorted_values = sorted([to_str(i) for i in x])
		return  "[" + ",".join(sorted_values) + "]"

	return "null"

obj = json.loads(read_all())
print(to_str(obj))
