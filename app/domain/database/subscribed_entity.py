from dataclasses import dataclass


@dataclass(frozen=True)
class SubscribedEntity:
    ids: list[str]
