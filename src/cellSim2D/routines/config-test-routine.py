
from __future__ import annotations

from dataclasses import dataclass
from os.path import isabs
from pathlib import Path
import time

import cellSim2D
from cellSim2D.util import DefaultHelpParser
from cellSim2D.util.types import FloatArray

from cellSim2D.util.logger import _logger, configure_logger

@dataclass
class SimulationResult:
    sim_dir: str

@dataclass
class TestingRoutine:
    model: cellSim2D.Model

    def run_func(self, num_cpu: int = 1):
        
        start_time = time.time()
        _logger.info("Entered the testing routine, cool")

        sim_dir = model._config['simulation_directory']

        _logger.info(f"I'm reading one config of {sim_dir} within TestingRoutine")

        _logger.info(f"I'm reading one config of {model._config['test_param']} within TestingRoutine")

        out = SimulationResult(
            sim_dir = sim_dir
        )

        _logger.info(f"Elpased time: {time.time() - start_time:.5f} seconds")

        return out

# region - Main

if __name__ == "__main__":
    """
    This will be a CLI routine. This particular routine will be continuously 
    used throughout initial development to identify configuration imports.
    """

    # region - Parse Arguments
    
    parser = DefaultHelpParser()

    parser.add_argument(
        '--simulation-config', '-m', type=str, required=True,
        help = "Configuration file for the model to be simulated."
    )

    parser.add_argument(
        '--output-dir', '-o', type=str, required=True, 
        help = "Location for saving all outputs."
    )

    args = parser.parse_args()

    sim_yaml: Path = Path(args.simulation_config)
    out_dir: Path = Path(args.output_dir)

    if not isabs(sim_yaml):
        sim_yaml = sim_yaml.resolve()
    if not isabs(out_dir):
        out_dir = out_dir.resolve()
    
    # endregion    

    # region - Creating tester routine

    configure_logger(print_level='info', logfile=out_dir / 'cellSim2D.log')

    model = cellSim2D.Model.from_yaml(sim_yaml)

    routine = TestingRoutine(
        model=model
    )
    result = routine.run_func()

    out_file = out_dir / 'output_results.pkl'
    _logger.info(f"Saving results to {str(out_file)}")
    # result.save(out_file)

    # endregion

# endregion