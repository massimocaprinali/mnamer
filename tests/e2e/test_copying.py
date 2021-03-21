from pathlib import Path

import pytest

from mnamer.const import SUBTITLE_CONTAINERS

pytestmark = pytest.mark.e2e

@pytest.mark.usefixtures("setup_test_dir")
def test_absolute_path(e2e_run, setup_test_files):
    setup_test_files("kill.bill.vol.1.mkv")
    result = e2e_run("--batch", "--copy", "--media=movie", "kill.bill.vol.1.mkv")
    assert result.code == 0
    assert "Kill Bill Vol. 1 (2003).mkv" in result.out
    assert "1 out of 1 files processed successfully" in result.out


@pytest.mark.usefixtures("setup_test_dir")
def test_batch(e2e_run, setup_test_files):
    setup_test_files(
        "Avengers Infinity War/Avengers.Infinity.War.srt",
        "Avengers Infinity War/Avengers.Infinity.War.wmv",
        "Downloads/the.goonies.1985.mp4",
        "Images/Photos/DCM0001.jpg",
        "aladdin.2019.avi",
        "archer.2009.s10e07.webrip.x264-lucidtv.mp4",
        "game.of.thrones.01x05-eztv.mp4",
        "lost s01e01-02.mp4",
    )
    result = e2e_run("--batch", "--copy", ".")
    assert result.code == 0
    assert "4 out of 4 files processed successfully" in result.out

