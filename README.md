# PowerMCP ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/powermcp/badge/?version=latest)](https://powermcp.readthedocs.io/en/latest/?badge=latest)

PowerMCP is an open-source framework for orchestrating AI agents across power system software like PowerWorld and pandapower using the Model Context Protocol (MCP). It enables intelligent coordination, simulation, and control in the energy domain.

## 🌟 What is MCP?

The Model Context Protocol (MCP) is a revolutionary standard that enables AI applications to seamlessly connect with various data sources and tools. Think of MCP as a universal adapter for AI applications, similar to what USB-C is for physical devices. It provides:

- Standardized connections to power system software and data sources
- Secure and efficient data exchange between AI agents and power systems
- Reusable components for building intelligent power system applications
- Interoperability between different AI models and power system tools

## 🤝 Our Community Vision

We're building an open-source community focused on accelerating AI adoption in the power domain through MCP. Our goals are:

- **Collaboration**: Bring together power system experts, AI researchers, and software developers
- **Innovation**: Create and share MCP servers for various power system applications
- **Education**: Provide resources and examples for implementing AI in power systems
- **Standardization**: Develop best practices for AI integration in the energy sector

## 🚀 Getting Started with Python

### Installation

```bash
pip install powermcp
```

### Basic Usage

```python
from powermcp import PowerMCP

# Initialize the MCP server
mcp = PowerMCP("PowerSystem")

# Add a power flow analysis tool
@mcp.tool()
def run_power_flow(bus_data: dict, line_data: dict) -> dict:
    """Run power flow analysis"""
    # Your power flow implementation here
    return results

# Add a dynamic resource for system data
@mcp.resource("system://{component_id}")
def get_system_data(component_id: str) -> dict:
    """Get real-time system data"""
    return {"voltage": 1.0, "power": 100.0}
```

### Example: Power System Monitoring

```python
from powermcp import PowerMCP
import pandas as pd

mcp = PowerMCP("PowerMonitor")

@mcp.tool()
def analyze_power_quality(data: pd.DataFrame) -> dict:
    """Analyze power quality metrics"""
    return {
        "voltage_deviation": calculate_deviation(data),
        "frequency_stability": check_frequency(data),
        "power_factor": compute_power_factor(data)
    }
```

## 📚 Documentation

For detailed documentation, please visit our [documentation site](https://powermcp.readthedocs.io/).

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The MCP Protocol team for their groundbreaking work
- The open-source community for their continuous support
- All contributors who help make this project better
