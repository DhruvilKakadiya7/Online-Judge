import subprocess
from .config import *

def run_cpp_code(input_file , output_file , error_file , source_code) :
    
    compile_command = f'g++ -o "{source_code[:-4]}" "{source_code}"'
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if compile_process.returncode == 0:
        run_command = f'{source_code[:-4]}.exe'
        
        with open(input_file , "r") as _in , open(output_file , "w") as _out:
            run_process = subprocess.run(run_command, shell=True, stdin=_in, stdout=_out, stderr=subprocess.PIPE, text=True)
        
        with open(error_file, 'w') as errorfile:
            errorfile.write(run_process.stderr)
        
        if run_process.returncode == 0 :
            return ACCEPTED
        else:
            return RUNTIME_ERROR
    else:
        with open(error_file, 'w') as errorfile:
            errorfile.write(compile_process.stderr)
            
        return COMPILATION_ERROR
