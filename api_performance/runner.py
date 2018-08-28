from locust import HttpLocust, TaskSet, task

class Disney_API(TaskSet):

    @task(1)
    def version(self):
        self.client.get("/version")


class runner(HttpLocust):
    task_set = Disney_API
    min_wait = 5000
    max_wait = 9000
