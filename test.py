from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def teste(self):
        self.client.get("https://cb20-2804-431-c7df-643e-25ca-2f3d-89f5-c691.ngrok-free.app/imoveis")