import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mcp.server.fastmcp import FastMCP
from common.utils import PowerError, power_mcp_tool
from typing import Dict, List, Optional, Tuple, Any, Union

# Initialize MCP server
mcp = FastMCP("PSLF Positive Sequence Load Flow Program")

from PSLF_PYTHON import *
init_pslf(silent=True)

@power_mcp_tool(mcp)
def open_case(case: str) -> Dict[str, Any]:
    """
    Open a PSLF case file.
    
    Args:
        case: Filename with .sav extension.
    
    Returns:
        Dict with status and case information
    """
    try:
        
        iret = Pslf.load_case(os.getcwd() + "\\" + case)
        cp = CaseParameters()
        
        # Get basic case information
        bus_data = cp.Nbus
        branch_data = cp.Nbrsec
        gen_data = cp.Ngen
        
        return {
            'status': 'success',
            'case_info': {
                'path': os.getcwd() + "\\" + case,
                'num_buses': bus_data if bus_data is not None else 0,
                'num_branches': branch_data if branch_data is not None else 0,
                'num_generators': gen_data if gen_data is not None else 0
            }
        }
    except Exception as e:
        return PowerError(
            status='error',
            message=str(e)
        )

@power_mcp_tool(mcp)
def solve_case() -> Dict[str, Any]:
    """
    Solves a powerflow case using PSLF.
    
    Returns:
        Dict with status and case information
    """
    try:
        
        result = Pslf.solve_case()
        
        return {
            'status': 'success',
            'case_info': {
                'result_code': result
            }
        }
    except Exception as e:
        return PowerError(
            status='error',
            message=str(e)
        )



if __name__ == "__main__":
    mcp.run(transport="stdio")