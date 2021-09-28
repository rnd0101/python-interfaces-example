"""
From Fluent Python book By Luciano Ramalho 2nd ed., 5. Data Class Builders

+ pyserde
"""
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import fields
from datetime import datetime

from serde.de import deserialize
from serde.json import from_json
from serde.json import to_json
from serde.se import serialize
from serde.toml import to_toml
from serde.yaml import to_yaml


@deserialize
@serialize
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float
    time: datetime
    mode: str = "esri"

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}, {self.mode}'


if __name__ == "__main__":
    c1 = Coordinate(12.2, 12.45, time=datetime.utcnow())
    print(c1)
    print(asdict(c1))
    print([(f.default, bool(f.default)) for f in fields(Coordinate)])
    print(Coordinate.__annotations__)

    # print(json.dumps(c1))
    print("JSON=", to_json(c1))
    print("YAML=", to_yaml(c1))
    print("TOML=", to_toml(c1))

    c3 = from_json(Coordinate, '{"lat": 12.2, "lon": -12.45, "time": "2021-09-26T10:28:42.247940", "mode": "esri"}')
    print(c3)
