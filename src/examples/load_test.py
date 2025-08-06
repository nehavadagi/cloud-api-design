from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_note(self):
        self.client.get("/notes/1")

    @task(3)
    def create_note(self):
        self.client.post("/notes/", json={
            "title": "Load Test",
            "content": "Simulating 1000 concurrent users"
        })