import subprocess
from .config import *
import multiprocessing
import time

def run(input_file , output_file , error_file , source_code , result_queue) :
    result = ""
    
    compile_command = f'g++ -o "{source_code[:-4]}" "{source_code}"'
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if compile_process.returncode == 0:
        run_command = f'{source_code[:-4]}.exe'
        
        with open(input_file , "r") as _in , open(output_file , "w") as _out:
            run_process = subprocess.run(run_command, shell=True, stdin=_in, stdout=_out, stderr=subprocess.PIPE, text=True)
        
        with open(error_file, 'w') as errorfile:
            errorfile.write(run_process.stderr)
        
        if run_process.returncode == 0 :
            result = ACCEPTED
        else:
            with open(error_file, 'w') as errorfile:
                errorfile.write(compile_process.stderr)
            result = RUNTIME_ERROR
    else:
        with open(error_file, 'w') as errorfile:
            errorfile.write(compile_process.stderr)
            
        result = COMPILATION_ERROR
    
    result_queue.put(result)

def run_cpp_code(input_file , output_file , error_file , source_code) :
    
    print("run cpp code")
    result_queue = multiprocessing.Queue()
    
    process = multiprocessing.Process(target = run , args = (input_file , output_file , error_file , source_code , result_queue))
    
    
    process.start()
    
    process.join(timeout = 3)
    
    if process.is_alive() :
        process.terminate()
        process.join()
        
        return TIME_LIMIT_EXCEEDED
    
    else :
        return result_queue.get()
    
    
