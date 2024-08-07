import docker
import uuid
from models.user import User

docker_client = docker.from_env()


def create_user():
    userid = str(uuid.uuid4())
    user = User(userId=userid)
    return user


# --out influxdb=http://192.168.1.100:8086/k6 bunu alttaki container çalıştırma fonksiyonuna ekleyeceğiz


def run_docker_container(user_id: str, virtual_users: int, duration: str):
    container = docker_client.containers.run(
        "k6",
        detach=True,
        environment={
            "USER_ID": user_id,
            "VUS": virtual_users,
            "DURATION": duration,
        },

    )
    return container.id
