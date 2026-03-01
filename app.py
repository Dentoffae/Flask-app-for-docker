"""Простое приложение для тестирования контейнера в Docker."""
import platform
import sys
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Главная страница."""
    return jsonify({
        "message": "Docker test app is running",
        "status": "ok",
    })


@app.route("/info")
def info():
    """Информация о среде выполнения."""
    return jsonify({
        "python_version": sys.version,
        "platform": platform.platform(),
        "container": "Docker",
    })


@app.route("/multiply/<int:a>/<int:b>")
def multiply(a: int, b: int):
    """Умножение двух чисел."""
    return jsonify({
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": a * b,
    }), 200


@app.route("/divide/<a>/<b>")
def divide(a: str, b: str):
    """Деление двух чисел."""
    try:
        a_num = float(a)
        b_num = float(b)
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400
    if b_num == 0:
        return jsonify({"error": "Division by zero"}), 400
    return jsonify({
        "operation": "divide",
        "a": a_num,
        "b": b_num,
        "result": a_num / b_num,
    })
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
