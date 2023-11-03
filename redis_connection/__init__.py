import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 30001)

redis_pool = redis.ConnectionPool(
    host=redis_host,
    port=redis_port,
    db=0,
)
