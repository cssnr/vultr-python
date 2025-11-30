from vultr import Vultr


vultr = Vultr()


def test_free():
    per_page = 100
    plans = vultr.get("plans", {"type": "vc2", "per_page": per_page})
    assert len(plans["plans"]) == min(plans["meta"]["total"], per_page)
