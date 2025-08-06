"""
DESIGN PROOF ONLY - CMP9785M Assessment
Theoretical load test scenario. Not executed.
"""
from locust import HttpUser, task

class DesignTestUser(HttpUser):
    @task
    def test_note_retrieval(self):
        self.client.get("/notes/1")  # Mocked endpoint