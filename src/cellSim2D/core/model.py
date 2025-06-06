
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from copy import deepcopy
from os.path import isabs

import yaml

from cellSim2D.util.logger import _logger

@dataclass
class Model:
    _config: dict

    @classmethod
    def from_config(cls, config: dict) -> Self:
        
        sim_dir = Path(config['simulation_directory'])
        if not isabs(sim_dir):
            sim_dir = sim_dir.resolve

            _logger.debug(f"The simulation directory is {sim_dir}")

        return cls(_config=config)
    
    @classmethod
    def from_yaml(cls, filepath: Path) -> Model:

        with open(filepath, 'r') as f:
            config = yaml.safe_load(f)

        return cls.from_config(config=config)
    
    @classmethod
    def to_yaml(self, filepath: Path) -> Path:

        cfg_to_save = deepcopy(self._config)
        cfg_to_save['simulation_directory'] = str(self._config['simulation_directory'])

        with open(filepath, 'w') as f:
            yaml.dump(self._config, stream=f, sort_keys=False)
        
        return filepath