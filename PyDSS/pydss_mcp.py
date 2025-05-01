from mcp.server.fastmcp import FastMCP
import py_dss_interface
from typing import List, Dict, Union, Optional

# Create global DSS instance
dss = py_dss_interface.DSS()

# Create an MCP server
mcp = FastMCP("PyDSS-MCP")

@mcp.tool()
def compile_and_solve(dss_file: str) -> Dict[str, bool]:
    """
    Compile an OpenDSS file and solve the circuit
    
    Args:
        dss_file: Path to the OpenDSS file (.dss)
    
    Returns:
        Dict indicating success status
    """
    try:
        dss.text(f"compile [{dss_file}]")
        dss.text("solve")
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

@mcp.tool()
def get_total_power() -> Dict[str, Union[List[float], str]]:
    """
    Get the total power from the current circuit
    
    Returns:
        Dict containing total power values [P, Q] in kW and kVAr
    """
    try:
        total_power = dss.circuit.total_power
        return {
            "success": True,
            "power": total_power,
            "units": "kW, kVAr"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    mcp.run(transport="stdio") 