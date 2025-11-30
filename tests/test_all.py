from vultr import Vultr


vultr = Vultr()


def test_free():
    per_page = 100
    plans = vultr.get("plans", {"type": "vc2", "per_page": per_page})
    print(f"plans: {len(plans['plans'])}")
    assert len(plans["plans"]) == min(plans["meta"]["total"], per_page)

    regions = vultr.list_regions({"per_page": per_page})
    print(f"regions: {len(regions)}")
    assert 0 < len(regions) <= per_page

    available = vultr.filter_regions(regions, plans["plans"][0]["locations"])
    print(f"available: {len(available)}")
    assert 0 < len(available) <= per_page
