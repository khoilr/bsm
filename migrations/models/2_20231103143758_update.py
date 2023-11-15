from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "Event";
        DROP TABLE IF EXISTS "EventLog";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ;"""
