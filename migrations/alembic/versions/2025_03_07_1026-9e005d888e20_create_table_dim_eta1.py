"""create_table_dim_eta1

Revision ID: 9e005d888e20
Revises: 16801f082048
Create Date: 2025-03-07 10:26:45.627420

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e005d888e20"
down_revision: Union[str, None] = "16801f082048"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_eta1",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_eta1")
