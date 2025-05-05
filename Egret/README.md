# Egret Power System Analysis Server

## Requirements

- [Egret](https://github.com/grid-parity-exchange/Egret)
- Python 3.10 or higher
- Gurobi or ipopt Solver for different tasks

## Available Tools

- **Solve Unit Commitment**: Solve a unit commitment problem using Egret with support for custom solvers, MIP gap, and time limits.
- **Solve AC Optimal Power Flow (AC OPF)**: Run AC OPF on Matpower or Egret JSON case files, returning detailed results.
- **Solve DC Optimal Power Flow (DC OPF)**: Run DC OPF on Matpower or Egret JSON case files, returning detailed results.
- **Quiet Logging**: All solver and library output is suppressed for cleaner logs.
- **Users can add more features based on Egret API**


## Prompt Example

- Could you solve the DC OPF of `pglib_opf_case14_ieee.m` in Egret?


## Resources
- [Egret GitHub](https://github.com/grid-parity-exchange/Egret) 
- [ipopt Document](https://coin-or.github.io/Ipopt/)