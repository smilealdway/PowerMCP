# PyPSA-MCP Power System Analysis Server

## Requirements

- [PyPSA](https://pypsa.org/) (Python for Power System Analysis)
- Python 3.10 or higher
- At least one LP solver supported by PyPSA (e.g., HiGHS, CBC, GLPK, or Gurobi)

## Main Features

- **Get Network Info**: Retrieve basic information about a PyPSA network (buses, generators, loads, lines, components).
- **Run Linear Optimal Power Flow (LOPF)**: Solve a linear OPF for a given PyPSA network file, with configurable solver and formulation.
- Users can add more features based on PyPSA api.

## Example

- Get network info:
  - "Get the network info of `test_case.nc` in PyPSA."
- Run OPF:
  - "Run OPF of `test_case.nc` in PyPSA using CBC solver."

## Resources
- [PyPSA Documentation](https://pypsa.readthedocs.io/)
