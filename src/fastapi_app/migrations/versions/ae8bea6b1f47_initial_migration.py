"""Initial migration

Revision ID: ae8bea6b1f47
Revises:
Create Date: 2024-08-20 05:51:08.549906

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ae8bea6b1f47"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("email", sa.String(length=120), unique=True, nullable=False),
        sa.Column("hashed_password", sa.String(length=250), nullable=True),
        sa.Column("is_active", sa.Boolean(), default=True),
    )

    # Create items table
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("title", sa.String(length=120), index=True, nullable=False),
        sa.Column("description", sa.String(length=250)),
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("items")
    op.drop_table("users")
