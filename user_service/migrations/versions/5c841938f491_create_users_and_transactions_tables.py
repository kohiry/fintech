"""create users and transactions tables

Revision ID: 5c841938f491
Revises: 
Create Date: 2024-08-30 06:24:19.378928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c841938f491'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        amount FLOAT NOT NULL
    );

    CREATE TYPE transaction_status AS ENUM ('SEND', 'FAILED', 'SUCCESS');

    CREATE TABLE transactions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        cost FLOAT NOT NULL,
        status transaction_status NOT NULL
    );
    """)


def downgrade():
    op.execute("""
    DROP TABLE transactions;
    DROP TYPE transaction_status;
    DROP TABLE users;
    """)
