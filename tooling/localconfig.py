# SPDX-License-Identifier: Unlicense
"""My Headset's settings in .env (MYHEADSET_ keys; env.example lists them).

What every Qualcomm Android headset names (serials, the EDL backup, the Firehose loader, the tools) is
overpressure's DeviceSettings; the headset adds only its own fields here. Its private files are in its own
folders, backup/myheadset/ and assets/myheadset/ (CODENAME), so that other headsets share the computer.
"""

from __future__ import annotations

from dataclasses import dataclass

from overpressure.api.v1 import localconfig as _base


@dataclass
class Settings(_base.DeviceSettings):
    """One headset's settings: its serials, its backup and the private files its workflow uses."""

    PREFIX = "MYHEADSET_"
    CODENAME = "myheadset"  #: its backups and private files in backup/myheadset/ and assets/myheadset/


def load() -> Settings:
    """Return the settings from .env and the environment."""
    return _base.load(Settings)
