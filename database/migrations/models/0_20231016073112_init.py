from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "dummymodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL
);
COMMENT ON TABLE "dummymodel" IS 'Model for demo purpose.';
CREATE TABLE IF NOT EXISTS "Person" (
    "person_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "Person" IS 'Tortoise-based log model.';
CREATE TABLE IF NOT EXISTS "Face" (
    "face_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "person_id" INT NOT NULL REFERENCES "Person" ("person_id") ON DELETE CASCADE
);
COMMENT ON TABLE "Face" IS 'Tortoise-based log model.';
CREATE TABLE IF NOT EXISTS "user" (
    "user_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(200) NOT NULL,
    "username" VARCHAR(200) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL,
    "manager" BOOL NOT NULL DEFAULT FALSE
);
COMMENT ON TABLE "user" IS 'Data model for user.';
CREATE TABLE IF NOT EXISTS "Zone" (
    "zone_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "Zone" IS 'Tortoise-based zone model.';
CREATE TABLE IF NOT EXISTS "AttendanceTracking" (
    "tracking_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "camera_id" INT NOT NULL REFERENCES "Zone" ("zone_id") ON DELETE CASCADE,
    "face_id" INT NOT NULL REFERENCES "Face" ("face_id") ON DELETE CASCADE
);
COMMENT ON TABLE "AttendanceTracking" IS 'Tortoise-based log model.';
CREATE TABLE IF NOT EXISTS "Camera" (
    "camera_id" SERIAL NOT NULL PRIMARY KEY,
    "camera_name" VARCHAR(256) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "zone_id" INT NOT NULL REFERENCES "Zone" ("zone_id") ON DELETE CASCADE
);
COMMENT ON TABLE "Camera" IS 'Tortoise-based camera model.';
CREATE TABLE IF NOT EXISTS "Log" (
    "log_id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "camera_id" INT NOT NULL REFERENCES "Zone" ("zone_id") ON DELETE CASCADE,
    "face_id" INT NOT NULL REFERENCES "Face" ("face_id") ON DELETE CASCADE
);
COMMENT ON TABLE "Log" IS 'Tortoise-based log model.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
