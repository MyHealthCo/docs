from diagrams import Cluster, Diagram
from diagrams.aws.compute import Compute, Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.general import User
from diagrams.aws.network import APIGateway, ElbApplicationLoadBalancer
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python

with Diagram("High Level\nCache Test Design", show=False):
    user = User("Load Tester")
    result_data = SimpleStorageServiceS3Bucket("Result Data")

    with Cluster("Preperation"):
        fake_data = Python("Fake Data\nGenerator")
        s3 = SimpleStorageServiceS3Bucket("Fake\nPatient Data")

    with Cluster("Trial - DynamoDB"):
        dynamo_cache = Dynamodb("DynamoDB Cache")
        dynamo_gateway = APIGateway("AWS API Gateway")
        dynamo_compute = Lambda("DynamoDB Worker")

    with Cluster("Trial - Redis"):
        redis_cache = Redis("Redis Cache")
        redis_gateway = APIGateway("AWS API Gateway")
        redis_compute = Lambda("Redis Worker")

    with Cluster("Load Application"):
        locust_load_balancer = ElbApplicationLoadBalancer("Load Balancer")
        with Cluster("Swarm"):
            locust_swarm = [
                Compute("Locust.io\nLoad Tester 1"),
                Compute("Locust.io\nLoad Tester 2"),
                Compute("Locust.io\nLoad Tester n"),
            ]

    # Prep Phase
    fake_data >> s3
    s3 >> dynamo_cache
    s3 >> redis_cache

    # Load Testing
    user >> locust_load_balancer
    locust_load_balancer >> locust_swarm
    locust_swarm >> dynamo_gateway
    locust_swarm >> redis_gateway
    locust_load_balancer >> user
    user >> result_data

    # DynamoDB Application Setup
    dynamo_gateway >> dynamo_compute
    dynamo_compute >> dynamo_cache

    # Redis Application Setup
    redis_gateway >> redis_compute
    redis_compute >> redis_cache
