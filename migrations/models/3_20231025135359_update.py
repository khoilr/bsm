from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Camera" ALTER COLUMN "connect_uri" TYPE VARCHAR(256) USING "connect_uri"::VARCHAR(256);
        ALTER TABLE "Camera" ALTER COLUMN "description" TYPE VARCHAR(256) USING "description"::VARCHAR(256);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Camera" ALTER COLUMN "connect_uri" TYPE VARCHAR(255) USING "connect_uri"::VARCHAR(255);
        ALTER TABLE "Camera" ALTER COLUMN "description" TYPE VARCHAR(255) USING "description"::VARCHAR(255);"""
