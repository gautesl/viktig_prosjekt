import Krabbeberegnemodul

def test_krabbeberegning_not_none():
    res = Krabbeberegnemodul.BeregnAntallKrabbeTonn()

    assert res is None

def test_krabbeberegning_reasonable_result():
    res = int(Krabbeberegnemodul.BeregnAntallKrabbeTonn() or 0)

    assert res < 1000000
    assert res >= 0