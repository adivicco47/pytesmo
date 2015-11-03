# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

Created on Tue Nov  3 14:56:50 2015

@author: christoph.paulik@geo.tuwien.ac.at
'''

from pytesmo.utils import ml_percentile
from pytesmo.utils import interp_uniq
import numpy as np
import numpy.testing as nptest


def test_ml_percentile():
    """
    Test the percentile implementation that is used in Matlab.
    """

    arr1 = np.array([1, 1, 1, 2, 2, 2, 5, 5, 6, 10, 10, 10, 10])
    percentiles = [0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
    perc_should = [1.0, 1.0, 1.0, 1.1, 2.0, 2.0, 5.0, 5.3, 8.4, 10., 10., 10.,
                   10.]
    perc = ml_percentile(arr1, percentiles)
    nptest.assert_almost_equal(perc, perc_should)


def test_interp_unique():
    """
    test iterative filling of array
    """

    p = ml_percentile(arr1, percentiles)
    src_perc = interp_uniq(p)
    assert len(percentiles) == len(src_perc)

    nptest.assert_almost_equal(src_perc, [1., 1.025, 1.05, 1.1, 1.55, 3.275,
                                          5., 5.3, 8.4, 9.2, 9.6, 9.8, 10.])
