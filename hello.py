#!/usr/bin/env python

import ctypes

if __name__ == "__main__":
	libhello = ctypes.CDLL("hello.so")

	# setup return type, ctypes assumes int as default
	# (https://docs.python.org/2/library/ctypes.html#return-types)
	libhello.hello.restype = ctypes.c_char_p

	print libhello.hello()
