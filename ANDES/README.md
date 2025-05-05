# ANDES MCP Python Integration

> **Note:**
> This MCP server is under active development and still needs further modification to handle some internal code output and ensure full compatibility with all ANDES features.

## Requirements

- [ANDES](https://andes.readthedocs.io/) (Python-based power system dynamic analysis)
- Python 3.10+
- All dependencies listed in your project requirements

## Available Tools

- **test_run_power_flow()**: Test the power flow analysis tool on a sample case.
  - Returns: Dictionary containing test results.

- **run_power_flow(file_path: str)**: Run power flow analysis on a power system case.
  - Args: `file_path` (Path to the case file)
  - Returns: Dictionary containing power flow results and output information.

- **run_time_domain_simulation(step_size: float = 0.01, t_end: float = 10.0)**: Run time domain simulation on the currently loaded power system.
  - Args:
    - `step_size`: Time step size in seconds (default 0.01)
    - `t_end`: End time in seconds (default 10.0)
  - Returns: Dictionary containing simulation results and output information.

- **run_eigenvalue_analysis(file_path: str)**: Run eigenvalue analysis on a power system case.
  - Args: `file_path` (Path to the case file)
  - Returns: Dictionary containing the eigenvalue analysis results.

- **get_system_info()**: Get information about the currently loaded power system.
  - Returns: Dictionary containing system information.

- **Users can add more features based on ANDES API**


## Development Notes

- This MCP server is still being improved. Some internal code output and error handling may not be fully integrated or user-friendly yet.
- Contributions and suggestions are welcome!

## Resources
- [ANDES Documentation](https://andes.readthedocs.io/) 