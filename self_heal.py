import docker
import time

client = docker.from_env()
container = client.containers.get("self-healing-web-container")

while True:
    container.reload()
    health = container.attrs["State"]["Health"]["Status"]

    print(f"Container health: {health}")

    if health == "unhealthy":
        print("Container is unhealthy. Restarting...")
        container.restart()

    time.sleep(10)
