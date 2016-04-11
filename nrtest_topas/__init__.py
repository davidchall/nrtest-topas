# -*- coding: utf-8 -*-

# third-party imports
from numpy.testing import assert_allclose
from topas2numpy import read_ntuple, BinnedResult


def topas_binned_compare(path_test, path_ref, rtol, atol):
    res_t = BinnedResult(path_test)
    res_r = BinnedResult(path_ref)

    if res_t.quantity != res_r.quantity:
        raise ValueError('Inconsistent quantities')
    if res_t.unit != res_r.unit:
        raise ValueError('Inconsistent units')
    if set(res_t.statistics) != set(res_r.statistics):
        raise ValueError('Inconsistent statistics')
    if res_t.dimensions != res_r.dimensions:
        raise ValueError('Inconsistent dimensions')
    for s in res_t.statistics:
        assert_allclose(res_t.data[s], res_r.data[s], rtol, atol)

    return True


def topas_ntuple_compare(path_test, path_ref, rtol, atol):
    res_t = read_ntuple(path_test)
    res_r = read_ntuple(path_ref)

    if res_t.dtype.names != res_r.dtype.names:
        raise ValueError('Inconsistent column names')
    if res_t.size != res_r.size:
        raise ValueError('Inconsistent ntuple sizes')
    for s in res_t.dtype.names:
        assert_allclose(res_t[s], res_r[s], rtol, atol)

    return True
