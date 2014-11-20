#!/usr/bin/env python
from setuptools import setup

setup(name="ssh-forward-unix-socket",
      version="0.0.1",
      description="Forward a Unix socket over SSH",
      author="Ricky Cook",
      author_email="mail@thatpanda.com",
      scripts=['forward_socket'],
      )
