from dataclasses import dataclass
from typing import Optional, Dict, Any
from mcp.server.fastmcp import FastMCP
import subprocess
import json
import os
from pathlib import Path

# Create an MCP server for PSSE
mcp = FastMCP("PSSE-MCP")

# Configuration
@dataclass
class PSSEConfig:
    python27_path: str = r"C:\Python27\python.exe"
    psse_version: int = 33
    max_buses: int = 2000
    psse_path: str = rf'C:\Program Files (x86)\PTI\PSSE{psse_version}'
    
    @property
    def bin_path(self) -> str:
        return os.path.join(self.psse_path, 'PSSBIN')
    
    @property
    def psse_script(self) -> str:
        return str(Path(__file__).parent / 'psse_operations.py')

config = PSSEConfig()

def run_psse_command(args: list) -> Dict[str, Any]:
    """Run PSSE command through Python 2.7"""
    try:
        # Ensure the operations script exists
        if not os.path.exists(config.psse_script):
            return {
                "status": -1,
                "message": f"PSSE operations script not found at: {config.psse_script}",
                "success": False
            }
            
        cmd = [config.python27_path, config.psse_script] + args
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            env={
                "PATH": f"{config.bin_path};{os.environ.get('PATH', '')}",
                "PYTHONPATH": config.bin_path
            }
        )
        
        if result.returncode != 0:
            return {
                "status": -1,
                "message": f"Command failed: {result.stderr}",
                "success": False
            }
        
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "status": -1,
                "message": f"Failed to parse PSSE output: {result.stdout}",
                "success": False
            }
            
    except Exception as e:
        return {
            "status": -1,
            "message": f"Error running command: {str(e)}",
            "success": False
        }

@mcp.tool()
def load_and_solve_case(case_path: str) -> Dict[str, Any]:
    """
    Load and solve a power flow case
    
    Args:
        case_path: Path to the .sav case file
    
    Returns:
        Dictionary containing solution status and messages
    """
    # Convert to absolute path if relative
    case_path = str(Path(case_path).resolve())
    args = ["solve", "--sav-case", case_path]
    return run_psse_command(args)

@mcp.tool()
def run_dynamic_simulation(
    sav_case: str,
    dyr_case: str,
    fault_bus: int,
    fault_duration_cycles: float = 3.0,
    total_simulation_time: float = 10.0,
    output_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Run a dynamic simulation with a bus fault
    
    Args:
        sav_case: Path to .sav case file
        dyr_case: Path to .dyr dynamics file
        fault_bus: Bus number for fault application
        fault_duration_cycles: Fault duration in cycles (default 3.0)
        total_simulation_time: Total simulation time in seconds (default 10.0)
        output_file: Optional path for output file
    
    Returns:
        Dictionary containing simulation status and results
    """
    # Convert to absolute paths if relative
    sav_case = str(Path(sav_case).resolve())
    dyr_case = str(Path(dyr_case).resolve())
    if output_file:
        output_file = str(Path(output_file).resolve())
    
    args = [
        "simulate",
        "--sav-case", sav_case,
        "--dyr-case", dyr_case,
        "--fault-bus", str(fault_bus),
        "--fault-duration", str(fault_duration_cycles),
        "--simulation-time", str(total_simulation_time)
    ]
    
    if output_file:
        args.extend(["--output-file", output_file])
    
    return run_psse_command(args)

@mcp.tool()
def export_results_to_excel(
    channel_file: str,
    excel_file: str = "out.xls",
    sheet_name: str = ""
) -> Dict[str, Any]:
    """
    Export channel results to Excel
    
    Args:
        channel_file: Path to the channel output file
        excel_file: Path for the Excel output file
        sheet_name: Name of the sheet in Excel
    
    Returns:
        Dictionary containing export status
    """
    # Convert to absolute paths if relative
    channel_file = str(Path(channel_file).resolve())
    excel_file = str(Path(excel_file).resolve())
    
    args = [
        "export",
        "--output-file", channel_file,
        "--excel-file", excel_file,
        "--sheet-name", sheet_name
    ]
    
    return run_psse_command(args)

if __name__ == "__main__":
    # The server can be started using:
    # mcp install PSSE/psse_mcp.py
    # or
    # mcp dev PSSE/psse_mcp.py
    mcp.run(transport="stdio") 