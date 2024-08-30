"""add row hashed_password for user

Revision ID: b5cfa005b553
Revises: 5c841938f491
Create Date: 2024-08-30 07:30:42.953409

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5cfa005b553'
down_revision: Union[str, None] = '5c841938f491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('ALTER TABLE "users" ADD COLUMN "hashed_password" VARCHAR(255) NOT NULL DEFAULT \'\';')


def downgrade() -> None:
    op.execute('ALTER TABLE "users" DROP COLUMN "hashed_password";')

