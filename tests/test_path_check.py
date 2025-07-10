# tests/path_check.py
import pytest

pytest.importorskip("yaml")           # yaml 未インストールで skip

@pytest.mark.xfail(reason="Stage-1 移行作業中")
def test_path_check_placeholder():
    assert False, "TODO: implement"
