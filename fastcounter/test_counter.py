import fastcounter

import pytest

counter_classes = (
    fastcounter.Counter,
    fastcounter.FastReadCounter,
    fastcounter.FastWriteCounter,
)


@pytest.mark.parametrize("counter_class", counter_classes)
def test_counter_init(counter_class):
    c = counter_class()
    assert c.value == 0


@pytest.mark.parametrize("counter_class", counter_classes)
def test_counter_increment_read(counter_class):
    c = counter_class()
    assert c.value == 0
    assert c.value == 0
    assert c.value == 0
    c.increment()
    assert c.value == 1
    assert c.value == 1
    c.increment()
    c.increment()
    assert c.value == 3
    assert c.value == 3
    c.increment(10)
    assert c.value == 13


@pytest.mark.parametrize("counter_class", counter_classes)
def test_counter_increment_init(counter_class):
    c = counter_class(4)
    assert c.value == 4
    assert c.value == 4
    assert c.value == 4
    c.increment()
    assert c.value == 5
    assert c.value == 5
    c.increment()
    c.increment()
    assert c.value == 7
    assert c.value == 7
    c.increment(10)
    assert c.value == 17


@pytest.mark.parametrize("counter_class", counter_classes)
def test_counter_increment_step(counter_class):
    c = counter_class(4, 3)
    assert c.value == 4
    assert c.value == 4
    assert c.value == 4
    c.increment()
    assert c.value == 7
    assert c.value == 7
    c.increment()
    c.increment()
    assert c.value == 13
    assert c.value == 13
    c.increment(10)
    assert c.value == 43
