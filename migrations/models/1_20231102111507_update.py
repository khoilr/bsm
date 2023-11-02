from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "AttendanceTracking" ALTER COLUMN "camera_id" DROP NOT NULL;
        ALTER TABLE "AttendanceTracking" ALTER COLUMN "face_id" DROP NOT NULL;
        ALTER TABLE "Camera" ALTER COLUMN "zone_id" DROP NOT NULL;
        ALTER TABLE "Face" ALTER COLUMN "person_id" DROP NOT NULL;
        ALTER TABLE "EventLog" ALTER COLUMN "event_id" DROP NOT NULL;
        ALTER TABLE "EventLog" ALTER COLUMN "face_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Face" ALTER COLUMN "person_id" SET NOT NULL;
        ALTER TABLE "Camera" ALTER COLUMN "zone_id" SET NOT NULL;
        ALTER TABLE "EventLog" ALTER COLUMN "event_id" SET NOT NULL;
        ALTER TABLE "EventLog" ALTER COLUMN "face_id" SET NOT NULL;
        ALTER TABLE "AttendanceTracking" ALTER COLUMN "camera_id" SET NOT NULL;
        ALTER TABLE "AttendanceTracking" ALTER COLUMN "face_id" SET NOT NULL;"""
