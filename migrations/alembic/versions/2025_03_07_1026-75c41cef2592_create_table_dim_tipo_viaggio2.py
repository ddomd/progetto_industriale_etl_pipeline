"""create_table_dim_tipo_viaggio2

Revision ID: 75c41cef2592
Revises: 9d62bf53e66c
Create Date: 2025-03-07 10:26:19.182911

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "75c41cef2592"
down_revision: Union[str, None] = "9d62bf53e66c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_tipo_viaggio2",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_viaggio2")
