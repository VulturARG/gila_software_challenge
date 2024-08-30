from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class SubscribedEntity:
    ids: list[str]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
