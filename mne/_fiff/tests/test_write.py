"""Run tests for writing."""

# Authors: The MNE-Python contributors.
# License: BSD-3-Clause
# Copyright the MNE-Python contributors.

import pytest

from mne._fiff.constants import FIFF
from mne._fiff.write import start_file, write_int


def test_write_int(tmp_path):
    """Test that write_int raises an error on bad values."""
    with start_file(tmp_path / "temp.fif") as fid:
        write_int(fid, FIFF.FIFF_MNE_EVENT_LIST, [2147483647])  # 2 ** 31 - 1
        write_int(fid, FIFF.FIFF_MNE_EVENT_LIST, [])  # 2 ** 31 - 1
        with pytest.raises(TypeError, match=r".*exceeds max.*EVENT_LIST\)"):
            write_int(fid, FIFF.FIFF_MNE_EVENT_LIST, [2147483648])  # 2 ** 31
        with pytest.raises(TypeError, match="Cannot safely write"):
            write_int(fid, FIFF.FIFF_MNE_EVENT_LIST, [0.0])  # float
