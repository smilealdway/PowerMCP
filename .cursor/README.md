# MCP Server Configuration

## Important Configuration Notes

Before using the MCP servers, you need to replace the Python executable path and MCP server file paths in `mcp.json` with your local paths.

### Path Configuration
- The example paths in `mcp.json` are for Windows systems
- For macOS/Linux systems, use appropriate paths and commands
- Python path example: `/path/to/your/python`
- MCP server file path example: `/path/to/your/mcp/server.py`

### MCP Servers Have Been Tested
- Egret
- OpenDSS
- pandapower
- PowerWorld
- PyPSA

### MCP Servers Under Development
- ANDES
- PSSE
- ...

Each server requires its own Python environment and configuration file path to be specified in `mcp.json`. 