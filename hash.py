#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import hashlib

if __name__ == "__main__":
    message = b"hello"
    print(hashlib.sha256(message).hexdigest())


