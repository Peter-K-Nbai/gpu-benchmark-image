from flask import Flask, jsonify
import benchmark
app = Flask(__name__)

latest_result = None


# check if there is gpu
@app.route('/check_gpu', methods=['GET'])
def check_gpu():
    has_gpu = benchmark.check_gpu()
    if has_gpu:
        return jsonify({"message": "CP has a GPU"})
    else:
        return jsonify({"message": "No GPU found"})


# run the benchmark
@app.route('/run_benchmark/<int:value>', methods=['POST'])
def run(value):
    global latest_result
    latest_result = benchmark.benchmark(n=value)  # Use the passed value
    return jsonify({"message": "Started Benchmark", "value": value})


# get the result
@app.route('/result', methods=['GET'])
def get_result():
    if latest_result is not None:
        return jsonify({"result": latest_result})
    else:
        return jsonify({"error": "No result available"}), 404

if __name__ == '__main__':
    app.run(debug=False)
