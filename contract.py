"""Each tool's and task's typed input and output (see nanoagent.plugin.contract): declarations only."""

from dataclasses import dataclass
from enum import Enum
from typing import Annotated

from slimconfig import Output


class Tool(Enum):
    SAY_HELLO = "say_hello"


class Task(Enum):
    SAY_HELLO = "say-hello"


@dataclass
class HelloInput(Output):
    name: Annotated[str, "Who to greet"]


@dataclass
class HelloOutput(Output):
    greeting: Annotated[str, "The greeting"]


TOOLS = {Tool.SAY_HELLO: (HelloInput, HelloOutput)}
TASKS = {Task.SAY_HELLO: HelloInput}
