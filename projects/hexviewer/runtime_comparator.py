import subprocess
import time
from typing import List, Tuple

def run_and_time(executable_path: str, args: List[str]) -> Tuple[float, bool]:
    """
    Runs an executable with given arguments and measures the execution time.

    Args:
        executable_path: The path to the executable file.
        args: A list of string arguments to pass to the executable.

    Returns:
        A tuple containing (execution_time, success_status).
    """
    print(f"--- Running {executable_path} with args: {' '.join(args)} ---")
    start_time = time.perf_counter()
    try:
        # Use subprocess.run for simplicity and capturing output/errors
        result = subprocess.run(
            [executable_path] + args,
            capture_output=True,
            text=True,
            check=False  # Do not raise exception on non-zero exit code
        )
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"--- Execution finished in {elapsed_time:.4f} seconds ---")
        # print("STDOUT:")
        # print(result.stdout)
        if result.stderr:
            print("STDERR (Potential Errors):")
            print(result.stderr)

        return elapsed_time, True

    except FileNotFoundError:
        print(f"Error: Executable not found at {executable_path}")
        return 0.0, False
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")
        return 0.0, False

def compare_runtimes(exec_paths: List[str], args: List[str]):
    """
    Compares the runtimes of two executables.

    Args:
        exec_paths: List of paths to executables.
        args: Arguments to pass for all executables.
    """
    print("\n=========================================")
    print("Starting Runtime Comparison")
    print("=========================================\n")

    # Run and time Executable 1
    for exe in exec_paths:
        runtime, success = run_and_time(exe, args) 
        print(exe, runtime, success)


if __name__ == "__main__":
    # --- USAGE EXAMPLE ---
    # NOTE: Replace these paths and arguments with your actual executable paths and inputs.
    
    # Example 1: Comparing two executables that take no arguments (e.g., main.exe)
    # If you want to compare the current project's compiled executables, use their full path.
    
    # Assuming 'main.exe' is in the same directory as this script for testing purposes.
    # EXECUTABLE_PATH = "./main.exe" 
    
    # Example: Comparing two versions or implementations of a tool
    # If you have two executables, e.g., "old_tool.exe" and "new_tool.exe"
    
    # For demonstration, we'll assume the user wants to compare 'main.exe' with itself 
    # but perhaps with different arguments or compiled differently (which requires manual setup).
    
    print("=========================================")
    print("Please update the paths and arguments in the __main__ block.")
    print("=========================================\n")

    # Example usage: Comparing main.exe run with no arguments vs. running with a specific argument '50'
    compare_runtimes(
        exec_paths=['D:\\programming\\proj\\hexviewer\\main.exe',  # tcc
                    'D:\\programming\\proj\\hexviewer\\release\\main.exe',  # clang with O3
                    'D:\\programming\\proj\\hexviewer\\build\\main.exe'],  # clang with O2 and debug
        args=["D:\\programming\\proj\\hexviewer\\build\\main.pdb", '50'],
    )