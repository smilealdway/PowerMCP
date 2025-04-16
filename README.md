# PowerMCP ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

PowerMCP is an open-source collection of MCP (Model Context Protocol) tools and servers for power system software like PowerWorld and pandapower. These tools enable LLMs to directly interact with power system applications, facilitating intelligent coordination, simulation, and control in the energy domain.

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

## 🚀 Getting Started with MCP

### Basic MCP Concepts

MCP defines three core primitives that servers can implement:

| Primitive | Control                | Description                                       | Example Use                  |
| --------- | ---------------------- | ------------------------------------------------- | ---------------------------- |
| Prompts   | User-controlled        | Interactive templates invoked by user choice      | Slash commands, menu options |
| Resources | Application-controlled | Contextual data managed by the client application | Power system data, API responses |
| Tools     | Model-controlled       | Functions exposed to the LLM to take actions      | Power flow analysis, control actions |

### Example MCP Server

Here's a simple example of a power system MCP server:

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("PowerSystem")

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

### Using with LLMs

To use these MCP tools with an LLM:

1. Install the MCP Python SDK:
```bash
pip install mcp-server-git
```

2. Run your MCP server:
```bash
python your_server.py
```

3. Configure your LLM application (e.g., Claude Desktop) to use the MCP server:
```json
{
  "mcpServers": {
    "power": {
      "command": "python",
      "args": ["your_server.py"]
    }
  }
}
```

## 📚 Documentation

For detailed documentation about MCP, please visit:
- [Model Context Protocol documentation](https://modelcontextprotocol.io/docs)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The MCP Protocol team for their groundbreaking work
- The open-source community for their continuous support
- All contributors who help make this project better
