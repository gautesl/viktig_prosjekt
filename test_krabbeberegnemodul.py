import Krabbeberegnemodul

def test_krabbeberegning_not_none():
    res = Krabbeberegnemodul.BeregnAntallKrabbeTonn()

    assert res is not None

def test_krabbeberegning_reasonable_result():
    res = Krabbeberegnemodul.BeregnAntallKrabbeTonn()

    assert res < 1000000
    assert res > 0