# OpenDSS MCP Python Integration

## Requirements

- Python 3.10 or higher
- [py_dss_interface](https://github.com/PauloRadatz/py_dss_interface)


## Available Tools

- **compile_and_solve(dss_file: str)**: Compile an OpenDSS file and solve the circuit.
- **get_total_power()**: Get the total power from the current circuit ([P, Q] in kW and kVAr).
- **set_load_multiplier(load_mult: float)**: Set the load multiplier and solve the circuit.
- **get_bus_voltages()**: Get per-unit voltages for all nodes in the circuit.
- **run_daily_energy_meter(meter_name: str = 'Feeder', hours: int = 24)**: Run a daily simulation and return total energy (kWh) from the specified energy meter for each hour.
- **get_harmonic_results(load_name: str, harmonic: int)**: Get the magnitude and angle of current and voltage for a specific load and harmonic order.
- **Users can add more features based on py_dss_interface API**


## Prompt Example

- Could you solve the bus voltage of `IEEE13Nodeckt.dss` in OpenDSS?


## Resources
- [OpenDSS](https://opendss.epri.com/IntroductiontoOpenDSS.html)
- [py_dss_interface Documentation](https://py-dss-interface.readthedocs.io/en/latest/py-dss-interface.html)
