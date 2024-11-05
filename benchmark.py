import torch
import time


# pip3 install torch --index-url https://download.pytorch.org/whl/cu118

def check_gpu():
    # Check if GPU is available
    if torch.cuda.is_available():
        return True
    else:
        device = torch.device("cpu")
        return False


def benchmark(n: int):
    # Determine the device to use
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    # Create two random matrices on the GPU
    matrix_a = torch.randn(n, n, device=device)
    matrix_b = torch.randn(n, n, device=device)
    
    # benchmark matrix multiplication
    start_time = time.time()
    result = torch.matmul(matrix_a, matrix_b)
    end_time = time.time()

    return end_time - start_time
