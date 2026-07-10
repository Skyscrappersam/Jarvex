import threading


class StreamWorker(threading.Thread):

    def __init__(
        self,
        target,
        callback=None,
        *args,
        **kwargs
    ):

        super().__init__(daemon=True)

        self.target = target
        self.callback = callback

        self.args = args
        self.kwargs = kwargs

    def run(self):

        try:

            result = self.target(
                *self.args,
                **self.kwargs
            )

            if self.callback:
                self.callback(result)

        except Exception as e:

            if self.callback:
                self.callback(
                    f"❌ {e}"
                )