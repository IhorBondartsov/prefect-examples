from prefect import task, Flow
from prefect.storage import GitHub

@task
def print_data(data):
    print(data)
    print(data)

with Flow(name="example") as flow:
    print_data("asd")
    print_data("asd")


flow.storage = GitHub(
    repo="IhorBondartsov/prefect-examples",   # name of repo
    path="flows/flow.py",                    # location of flow file in repo
    access_token_secret="GIT_TOKEN"   # name of personal access token secret
)