# gpu-benchmark-image

### The Purpose of this image is to perform a matrix multiplication to benchark the GPU performance of the host machine

Uses an nvidia base image and Pytorch to perform the benchmark computation. Uses Flask as the api backend.

### APIs

`/check_gpu` : Returns `True` or `False` to indicate of the container has access to a host GPU.

`/run_benchmark/<n>` : Runs the benchmark matrix multiplication of 2 n x n matrices. 

`/result` : Returns the time it took to perform the computation

### Running the Container
To run the container use this docker command
```bash
docker run --name gpu-check --gpus all -p 5000:5000 gpu-check
```
