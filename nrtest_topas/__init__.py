# -*- coding: utf-8 -*-

# third-party imports
from numpy.testing import assert_allclose
from topas2numpy import read_ntuple, BinnedResult


def topas_binned_compare(path_test, path_ref, rtol, atol):
    res_t = BinnedResult(path_test)
    res_r = BinnedResult(path_ref)

    assert res_t.quantity == res_r.quantity
    assert res_t.unit == res_r.unit
    assert set(res_t.statistics) == set(res_r.statistics)
    assert res_t.dimensions == res_r.dimensions
    for s in res_t.statistics:
        assert_allclose(res_t.data[s], res_r.data[s], rtol, atol)

    return True


def topas_ntuple_compare(path_test, path_ref, rtol, atol):
    res_t = read_ntuple(path_test)
    res_r = read_ntuple(path_ref)

    assert res_t.dtype.names == res_r.dtype.names
    assert res_t.size == res_r.size
    for s in res_t.dtype.names:
        assert_allclose(res_t[s], res_r[s], rtol, atol)

    return True
