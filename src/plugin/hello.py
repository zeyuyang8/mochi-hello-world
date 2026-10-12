from __future__ import annotations

from pathlib import Path

from contract import HelloInput, HelloOutput


def say_hello(hello: HelloInput, workspace: Path) -> HelloOutput:
    if not hello.name.strip():
        raise ValueError("name must not be empty")
    return HelloOutput(greeting=f"Hello, {hello.name}!")
