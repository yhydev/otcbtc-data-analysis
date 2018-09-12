#!/usr/bin/env python
import logging,db


logging.basicConfig(filename = "test.log",level = logging.INFO,datefmt = "%Y-%m-%d %H:%M:%S",format = "%(asctime)s %(levelname)s\t: %(message)s")

logging.info("test")