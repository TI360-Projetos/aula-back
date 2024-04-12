from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def teste(self):
        self.client.get("/imoveis")