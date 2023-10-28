COMPILATION_ERROR = 1
RUNTIME_ERROR = 2
WRONG_ANSWER = 3
TIME_LIMIT_EXCEEDED = 4
MEMORY_LIMIT_EXCEEDED = 5
ACCEPTED = 6

def getMessage(id) :
    decode = {
        1 : "Compilation Error",
        2 : "Runtime Error",
        3 : "Wrong Answer",
        4 : "Time Limit Exceeded",
        5 : "Memory Limit Exceeded",
        6 : "Accepted"
    }
    return decode[id]

BASE_DIR = "G:\\SEM-7\\ADF\\FINAL PROJECT\\AlgoBooth\\media\\"

