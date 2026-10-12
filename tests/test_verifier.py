from __future__ import annotations

from pathlib import Path

from slimconfig import build_output, plain_output

import verifier
from contract import HelloInput, HelloOutput
from plugin.hello import say_hello


# The verifier gets contract instances, as NanoAgent's sandbox builds them from JSON.
def test_approves_a_greeting(tmp_path: Path) -> None:
    given = build_output({"name": "Mochi"}, HelloInput)
    made = build_output(plain_output(say_hello(given, tmp_path)), HelloOutput)
    assert verifier.verify_input("say_hello", given)["valid"] is True
    assert verifier.verify_output("say_hello", given, made, str(tmp_path))["valid"] is True
    assert verifier.verify_task("say-hello", given, None, str(tmp_path))["valid"] is True


def test_refuses_a_wrong_greeting(tmp_path: Path) -> None:
    given = build_output({"name": "Mochi"}, HelloInput)
    made = build_output({"greeting": "Hi"}, HelloOutput)
    assert verifier.verify_output("say_hello", given, made, str(tmp_path))["valid"] is False
    assert verifier.verify_input("say_hello", build_output({"name": ""}, HelloInput))["valid"] is False
