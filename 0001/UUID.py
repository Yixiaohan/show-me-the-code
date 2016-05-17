#!/usr/bin/env python3
import uuid
result = set()
for i in range(0,200):
    result.add(uuid.uuid4())

print(len(result))
