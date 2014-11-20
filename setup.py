#!/usr/bin/env python
from setuptools import setup

setup(name="SSH Unix Socket Forwarder",
      version="0.0.1",
      description="Forward a Unix socket over SSH",
      author="Ricky Cook",
      author_email="mail@thatpanda.com",
      py_modules=['forward_socket'],
      scripts=['forward_socket'],
      )
