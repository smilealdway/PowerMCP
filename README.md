# PowerMCP ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

PowerMCP is an open-source collection of MCP servers for power system software like PowerWorld and OpenDSS. These tools enable LLMs to directly interact with power system applications, facilitating intelligent coordination, simulation, and control in the energy domain.

## 🌟 What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is a revolutionary standard that enables AI applications to seamlessly connect with various external tools. Think of MCP as a universal adapter for AI applications, similar to what USB-C is for physical devices. It provides:

- Standardized connections to power system software and data sources
- Secure and efficient data exchange between AI agents and power systems
- Reusable components for building intelligent power system applications
- Interoperability between different AI models and power system tools

## 🤝 Our Community Vision

We're building an open-source community focused on accelerating AI adoption in the power domain through MCP. Our goals are:

- **Collaboration**: Bring together power system experts, AI researchers, and software developers
- **Innovation**: Create and share MCP servers for various power system software and tools
- **Education**: Provide resources and examples for implementing AI in power systems
- **Standardization**: Develop best practices for AI integration in the energy sector

## 🚀 Getting Started with MCP

### Video Demos

Check out these demos showcasing PowerMCP in action:

- [**Contingency Evaluation Demo**](https://www.youtube.com/watch?v=MbF-SlBI4Ws): An LLM automatically operates power system software, such as PowerWorld and pandapower, to perform contingency analysis and generate professional reports.

- [**Loadgrowth Evaluation Demo**](https://www.youtube.com/watch?v=euFUvhhV5dM): An LLM automatically operates power system software, such as PowerWorld, to evaluate different load growth scenarios and generate professional reports with recommendations.

### Useful MCP Tutorials

MCP follows a client-server architecture where:

* **Hosts** are LLM applications (like Claude Desktop or IDEs) that initiate connections
* **Clients** maintain 1:1 connections with servers, inside the host application
* **Servers** provide context, tools, and prompts to clients

Check out these helpful tutorials to get started with MCP:

- [**Getting Started with MCP**](https://modelcontextprotocol.io/introduction): Official introduction to the Model Context Protocol fundamentals.
- [**Core Architecture**](https://modelcontextprotocol.io/docs/concepts/architecture): Detailed explanation of MCP's client-server architecture.
- [**Building Your First MCP Server**](https://modelcontextprotocol.io/build/server): Step-by-step guide to creating a basic MCP server.
- [**Anthropic MCP Tutorial**](https://docs.anthropic.com/claude/docs/model-context-protocol): Learn how to use MCP with Claude models.
- [**Cursor MCP Tutorial**](https://docs.cursor.com/context/model-context-protocol): Learn how to use MCP with Cursor.
- [**Other Protocol**](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): Open AI Function Calling Tool

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

3. Configure your LLM application (e.g., [Claude Desktop](https://claude.ai/download), [Cursor](https://www.cursor.com/)) to use the MCP server:
```json
{
  "mcpServers": {
    "servername": {
      "command": "python",
      "args": ["your_server.py"]
    }
  }
}
```

## 📚 Documentation

For detailed documentation about MCP, please visit:
- [Model Context Protocol documentation](https://modelcontextprotocol.io/introduction)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Other General MCP Servers](https://smithery.ai/)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://power-agent.github.io/) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

### Core Team
- [Qian Zhang](https://seas.harvard.edu/person/qian-zhang) 

### Special Thanks
- All contributors who help make this project better
- [The Power and AI Initiative (PAI) at Harvard SEAS](https://pai.seas.harvard.edu/)
