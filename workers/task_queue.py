import queue
import threading


class TaskQueue:

    def __init__(self, max_workers: int = 4):

        self.tasks = queue.Queue()
        self.max_workers = max_workers
        self.workers = []
        self.running = False

    def add_task(self, fn, *args, **kwargs):
        """
        Push a task into the queue.
        """
        self.tasks.put((fn, args, kwargs))

    def worker_loop(self):

        while self.running:

            try:
                fn, args, kwargs = self.tasks.get(timeout=1)
                fn(*args, **kwargs)
                self.tasks.task_done()

            except queue.Empty:
                continue

    def start(self):

        self.running = True

        for _ in range(self.max_workers):

            t = threading.Thread(target=self.worker_loop, daemon=True)
            t.start()
            self.workers.append(t)

    def stop(self):

        self.running = False

        for t in self.workers:
            t.join(timeout=1)

    def wait(self):
        self.tasks.join()
