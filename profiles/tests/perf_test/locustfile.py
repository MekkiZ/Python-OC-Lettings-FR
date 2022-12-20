from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task(6)
    def home(self):
        self.client.get("")

    @task(2)
    def index_lettings(self):
        self.client.get('profiles/')

    @task
    def lettings(self):
        self.client.get('profiles/HeadlinesGazer/')
