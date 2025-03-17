"""create_table_dim_tipo_alloggio

Revision ID: 116259842bd3
Revises: 75c41cef2592
Create Date: 2025-03-07 10:26:28.892304

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "116259842bd3"
down_revision: Union[str, None] = "75c41cef2592"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_tipo_alloggio",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_alloggio")
