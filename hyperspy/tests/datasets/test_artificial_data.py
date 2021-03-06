# -*- coding: utf-8 -*-
# Copyright 2007-2020 The HyperSpy developers
#
# This file is part of  HyperSpy.
#
#  HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  HyperSpy.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import hyperspy.datasets.artificial_data as ad


def test_get_low_loss_eels_signal():
    s = ad.get_low_loss_eels_signal()
    assert s.metadata.Signal.signal_type == 'EELS'


def test_get_core_loss_eels_signal():
    s = ad.get_core_loss_eels_signal(add_powerlaw=False)
    assert s.metadata.Signal.signal_type == 'EELS'
    s1 = ad.get_core_loss_eels_signal(add_powerlaw=True)
    assert s1.metadata.Signal.signal_type == 'EELS'
    assert s1.data.sum() > s.data.sum()

    np.random.seed(seed=10)
    s2 = ad.get_core_loss_eels_signal()
    np.random.seed(seed=10)
    s3 = ad.get_core_loss_eels_signal()
    assert (s2.data == s3.data).all()


def test_get_core_loss_eels_model():
    m = ad.get_core_loss_eels_model(add_powerlaw=False)
    assert m.signal.metadata.Signal.signal_type == 'EELS'
    m1 = ad.get_core_loss_eels_model(add_powerlaw=True)
    assert m1.signal.metadata.Signal.signal_type == 'EELS'
    assert m1.signal.data.sum() > m.signal.data.sum()


def test_get_low_loss_eels_line_scan_signal():
    s = ad.get_low_loss_eels_line_scan_signal()
    assert s.metadata.Signal.signal_type == 'EELS'


def test_get_core_loss_eels_line_scan_signal():
    s = ad.get_core_loss_eels_line_scan_signal()
    assert s.metadata.Signal.signal_type == 'EELS'


def test_get_atomic_resolution_tem_signal2d():
    s = ad.get_atomic_resolution_tem_signal2d()
    assert s.axes_manager.signal_dimension == 2
