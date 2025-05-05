# PowerMCP ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

PowerMCP is an open-source collection of MCP servers for power system software like PowerWorld and OpenDSS. These tools enable LLMs to directly interact with power system applications, facilitating intelligent coordination, simulation, and control in the energy domain.

## 🌟 What is MCP?

The <a href="https://modelcontextprotocol.io/introduction" target="_blank">Model Context Protocol</a> (MCP) is a revolutionary standard that enables AI applications to seamlessly connect with various external tools. Think of MCP as a universal adapter for AI applications, similar to what USB-C is for physical devices. It provides:

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

- <a href="https://www.youtube.com/watch?v=MbF-SlBI4Ws" target="_blank">**Contingency Evaluation Demo**</a>: An LLM automatically operates power system software, such as PowerWorld and pandapower, to perform contingency analysis and generate professional reports.

- <a href="https://www.youtube.com/watch?v=euFUvhhV5dM" target="_blank">**Loadgrowth Evaluation Demo**</a>: An LLM automatically operates power system software, such as PowerWorld, to evaluate different load growth scenarios and generate professional reports with recommendations.

### Useful MCP Tutorials

MCP follows a client-server architecture where:

* **Hosts** are LLM applications (like Claude Desktop or IDEs) that initiate connections
* **Clients** maintain 1:1 connections with servers, inside the host application
* **Servers** provide context, tools, and prompts to clients

Check out these helpful tutorials to get started with MCP:

- <a href="https://modelcontextprotocol.io/introduction" target="_blank">**Getting Started with MCP**</a>: Official introduction to the Model Context Protocol fundamentals.
- <a href="https://modelcontextprotocol.io/docs/concepts/architecture" target="_blank">**Core Architecture**</a>: Detailed explanation of MCP's client-server architecture.
- <a href="https://modelcontextprotocol.io/build/server" target="_blank">**Building Your First MCP Server**</a>: Step-by-step guide to creating a basic MCP server.
- <a href="https://github.com/modelcontextprotocol/python-sdk/tree/main/examples" target="_blank">**MCP Python SDK Examples**</a>: Collection of sample implementations using the Python SDK.
- <a href="https://docs.anthropic.com/claude/docs/model-context-protocol" target="_blank">**Anthropic MCP Tutorial**</a>: Learn how to use MCP with Claude models.

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

3. Configure your LLM application (e.g., <a href="https://claude.ai/download" target="_blank">Claude Desktop</a>, <a href="https://www.cursor.com/" target="_blank">Cursor</a>) to use the MCP server:
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
- <a href="https://modelcontextprotocol.io/introduction" target="_blank">Model Context Protocol documentation</a>
- <a href="https://github.com/modelcontextprotocol/python-sdk" target="_blank">MCP Python SDK</a>
- <a href="https://smithery.ai/" target="_blank">Other General MCP Servers</a>

## 🤝 Contributing

We welcome contributions! Please see our <a href="https://power-agent.github.io/" target="_blank">Contributing Guidelines</a> for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The open-source community for their continuous support
- All contributors who help make this project better
- <a href="https://pai.seas.harvard.edu/" target="_blank">The Power and AI Initiative (PAI) at Harvard SEAS</a>
