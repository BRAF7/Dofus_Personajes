import requests
import threading
from concurrent.futures import Future


def generate_request(url) -> Future:
    future :  Future = Future()

    thread = threading.Thread(
        target=(
        lambda: future.set_result(requests.get(url))
        )
    )
    thread.start()

    return future