from mcp.server.fastmcp import FastMCP
from pypsa import Network
import numpy as np
from typing import Dict, List, Optional, Union
import json

# Create an MCP server
mcp = FastMCP("PyPSA-MCP")


@mcp.tool()
def get_network_info(network_name: str) -> str:
    """Get basic information about the network"""
    network = Network(network_name)
    info = {
        "buses": len(network.buses),
        "generators": len(network.generators),
        "loads": len(network.loads),
        "lines": len(network.lines),
        "components": list(network.all_components)
    }
    return json.dumps(info, indent=2)

@mcp.tool()
def optimize_network(
    network_name: str,
    solver_name: str = "gurobi",
    formulation: str = "kirchhoff"
) -> str:
    """Run a linear optimal power flow (LOPF) on the network"""
    
    network = Network(network_name)
    try:
        # Use the correct LOPF method for the current PyPSA version
        network.optimize(
            solver_name=solver_name,
            formulation=formulation
        )
        
        # Get optimization results
        results = {
            "objective": network.objective,
            "generators": {
                gen: {
                    "p": float(network.generators_t.p[gen].iloc[0]),
                    "status": float(network.generators_t.status[gen].iloc[0])
                }
                for gen in network.generators.index
            },
            "loads": {
                load: float(network.loads_t.p[load].iloc[0])
                for load in network.loads.index
            }
        }
        return json.dumps(results, indent=2)
    except Exception as e:
        return f"Optimization failed: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio") 