from __future__ import annotations

from pathlib import Path

import pytest

from contract import HelloInput, HelloOutput
from plugin.hello import say_hello


def test_greets_by_name(tmp_path: Path) -> None:
    assert say_hello(HelloInput(name="Mochi"), tmp_path) == HelloOutput(greeting="Hello, Mochi!")


def test_refuses_an_empty_name(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="empty"):
        say_hello(HelloInput(name=" "), tmp_path)
