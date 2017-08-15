import os
from nose.tools import assert_raises
from cykdtree.tests import scaling
try:
    from mpi4py import MPI
except ImportError:  # pragma: w/o MPI
    MPI = None


def test_stats_run():
    f = scaling.stats_run(100, 1, 2, display=True)
    f = scaling.stats_run(100, 1, 2, periodic=True,
                          fname=f, overwrite=True,
                          suppress_final_output=True)
    if MPI is None:  # pragma: w/o MPI
        assert_raises(RuntimeError, scaling.stats_run, 100, 2, 2,
                      fname=f, overwrite=True)
    else:  # pragma: w/ MPI
        f = scaling.stats_run(100, 2, 2, fname=f, overwrite=True)
    assert(os.path.isfile(f))
    os.remove(f)


def test_time_run():
    scaling.time_run(100, 1, 2)
    if MPI is None: # pragma: w/o MPI
        assert_raises(RuntimeError, scaling.time_run, 10, 2, 2)
    else: # pragma: w/ MPI
        scaling.time_run(100, 2, 2)


def test_strong_scaling():
    if MPI is None: # pragma: w/o MPI
        assert_raises(RuntimeError, scaling.strong_scaling,
                      npart=100, nproc_list=[1,2])
        f = scaling.strong_scaling(npart=100, nproc_list=[1], ndim_list=[2],
                                   periodic=True, suppress_final_output=True)
        assert(os.path.isfile(f))
        os.remove(f)
    else:  # pragma: w/ MPI
        f = scaling.strong_scaling(npart=100, nproc_list=[1,2], ndim_list=[2],
                                   periodic=True, overwrite=True,
                                   suppress_final_output=True)
        assert(os.path.isfile(f))
        os.remove(f)


def test_weak_scaling():
    if MPI is None: # pragma: w/o MPI
        assert_raises(RuntimeError, scaling.weak_scaling,
                      npart=100, nproc_list=[1,2])
        f = scaling.weak_scaling(npart=100, nproc_list=[1], ndim_list=[2],
                                   periodic=True, suppress_final_output=True)
        assert(os.path.isfile(f))
        os.remove(f)
    else:  # pragma: w/ MPI
        f = scaling.weak_scaling(npart=100, nproc_list=[1,2], ndim_list=[2],
                                 periodic=True, overwrite=True,
                                 suppress_final_output=True)
        assert(os.path.isfile(f))
        os.remove(f)
