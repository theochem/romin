# -*- coding: utf-8 -*-
# RoMin is a robust minimizer.
# Copyright (C) 2011-2015 Toon Verstraelen
#
# This file is part of RoMin.
#
# RoMin is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# RoMin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#--


from romin import *
from romin.test.test_objectives import Rosenbrock, Atoms
from romin.test.random_seed import numpy_random_seed


def test_min_ntr_rosenbrock():
    for b in xrange(3, 100, 10):
        fn = Rosenbrock(1, b, np.array([2.0, 5.0]))
        minimize_objective_ntr(fn)
        assert rms(fn.gradient()) < 1e-7
        assert abs(fn.x - 1.0).max() < 1e-7


def test_min_ntr_noble_atoms_sr1():
    for irep in xrange(10):
        with numpy_random_seed(irep):
            fn = Atoms(1.0, 1.0, 1, 10, np.random.normal(0, 2, 30))
            hm = SR1HessianModel()
            wr = HessianModelWrapper(fn, hm)
            minimize_objective_ntr(wr, maxiter=5125)
            assert rms(fn.gradient()) < 1e-7


def test_min_ntr_noble_atoms_lsr1():
    for irep in xrange(10):
        with numpy_random_seed(irep):
            fn = Atoms(1.0, 1.0, 1, 10, np.random.normal(0, 2, 30))
            hm = LSR1HessianModel(7)
            wr = HessianModelWrapper(fn, hm)
            minimize_objective_ntr(wr, maxiter=5125)
            assert rms(fn.gradient()) < 1e-7
