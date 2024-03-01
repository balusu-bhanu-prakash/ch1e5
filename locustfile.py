from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests (1-2 seconds)

    @task
    def test_hello_world(self):
        self.client.get("/")  # Simulates a GET request to the homepage route

if __name__ == "__main__":
    import os
    os.system(f"locust -f locustfile.py --headless --host={os.getenv('HOST')} --users {os.getenv('USERS')} --spawn-rate {os.getenv('HATCH_RATE')}")