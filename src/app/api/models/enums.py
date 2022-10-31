from enum import Enum, unique


@unique
class DroneEnumModel(Enum):
    Lightweight = "Lightweight"
    Middleweight = "Middleweight"
    Cruiserweight = "Cruiserweight"
    Heavyweight = "Heavyweight"


@unique
class DroneEnumState(Enum):
    IDLE = "IDLE"
    LOADING = "LOADING"
    LOADED = "LOADED"
    DELIVERING = "DELIVERING"
    DELIVERED = "DELIVERED"
    RETURNING = "RETURNING"
