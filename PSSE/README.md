# PSSE MCP Python Integration

> **Note:**
> Because the embedded Python for PSSE is not compatible with the current MCP Python requirement (> Python 3.10), this MCP server still needs further modification and improvement to ensure full functionality and integration.

## Requirements

- PSSE v33 (or compatible version)
- Access to the PSSE installation directory (e.g., `C:\Program Files (x86)\PTI\PSSE33`)

## Prompt Example

- Could you solve the power flow for `savnw.sav` in PSSE?

## Available Tools

- **load_and_solve_case(case_path: str)**: Load and solve a power flow case.
  - Args: `case_path` (Path to the .sav case file)
  - Returns: Dictionary containing solution status and messages.

- **run_dynamic_simulation(sav_case: str, dyr_case: str, fault_bus: int, fault_duration_cycles: float = 3.0, total_simulation_time: float = 10.0, output_file: Optional[str] = None)**: Run a dynamic simulation with a bus fault.
  - Args: 
    - `sav_case`: Path to .sav case file
    - `dyr_case`: Path to .dyr dynamics file
    - `fault_bus`: Bus number for fault application
    - `fault_duration_cycles`: Fault duration in cycles (default 3.0)
    - `total_simulation_time`: Total simulation time in seconds (default 10.0)
    - `output_file`: Optional path for output file
  - Returns: Dictionary containing simulation status and results.

- **export_results_to_excel(channel_file: str, excel_file: str = "out.xls", sheet_name: str = "")**: Export channel results to Excel.
  - Args:
    - `channel_file`: Path to the channel output file
    - `excel_file`: Path for the Excel output file
    - `sheet_name`: Name of the sheet in Excel
  - Returns: Dictionary containing export status.

- Users can add more features based on PSSE python api.


## Resources
- [PSSE Documentation](https://www.siemens.com/us/en/products/energy/grid-software/planning/pss-software.html)
