Fastcounter
===========
.. image:: https://img.shields.io/pypi/v/fastcounter.svg
    :target: https://pypi.python.org/pypi/fastcounter

.. image:: https://circleci.com/gh/jd/fastcounter.svg?style=svg
    :target: https://circleci.com/gh/jd/fastcounter

.. image:: https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg
    :target: https://saythanks.io/to/jd

.. image:: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/jd/fastcounter&style=flat
   :target: https://mergify.io
   :alt: Mergify Status

Fastcounter is an Apache 2.0 licensed fast counter library written in Python.
It aims at implementing fast incremental integer with different trade-offs on
performance depending on your use case.

It provides 3 classes:

- `Counter`, a simple integer counter that does not support any concurrency.
- `FastWriteCounter`, a counter that is thread-safe and is faster at writing
  than reading.
- `FastReadCounter`, a counter that is thread-safe and is faster at reading
  than writing.

Example::

  import fastcounter

  counter = fastcounter.Counter()

  counter.value # returns 1
  counter.increment()
  counter.value # returns 2

  counter.increment(10)
  counter.value # returns 12

