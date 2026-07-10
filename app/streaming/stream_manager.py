from app.streaming.stream_worker import StreamWorker


class StreamManager:

    def __init__(self):

        self.current_worker = None

    # ==========================
    # Start Stream
    # ==========================

    def start_stream(
        self,
        target,
        callback=None,
        *args,
        **kwargs
    ):

        if self.is_streaming():
            return False

        self.current_worker = StreamWorker(
            target=target,
            callback=callback,
            *args,
            **kwargs
        )

        self.current_worker.start()

        return True

    # ==========================
    # Status
    # ==========================

    def is_streaming(self):

        return (
            self.current_worker is not None
            and self.current_worker.is_alive()
        )

    # ==========================
    # Wait
    # ==========================

    def wait(self):

        if self.current_worker:
            self.current_worker.join()

    # ==========================
    # Clear
    # ==========================

    def clear(self):

        self.current_worker = None