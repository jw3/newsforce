import os

import check as checker


def passing(event, article_dir, ignores=None, categories=None, contrib_url=None) -> bool:
    os.environ["EVENT_PATH"] = f"test/{event}.json"
    return not checker.main(f"test/{article_dir}", ignores, categories, contrib_url)


def test_simple():
    assert passing("e0", "news1")
    assert not passing("e3", "news1")
    assert passing("e3", "news3")


def test_ignore():
    assert not passing("e2", "news2")
    assert passing("e2", "news2", ignores="ignore")
    assert passing("e2", "news2", ignores="ignore,foo")


def test_case():
    assert passing("e0", "news2", ignores="B00M")
    assert passing("e0", "news2", ignores="b00m")
    assert passing("e2", "news2", ignores="ignore")
    assert passing("e2", "news2", ignores="IGNORE")
