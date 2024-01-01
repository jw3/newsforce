import os

import check as checker


def check(event, ignores=None, categories=None, contrib_url=None):
    os.environ["EVENT_PATH"] = f"test/{event}.json"
    return not checker.main("test", ignores, categories, contrib_url)


def test_simple():
    assert not check("e0")


def test_ignore():
    assert not check("e2")
    assert not check("e2", ignores="ignore")
