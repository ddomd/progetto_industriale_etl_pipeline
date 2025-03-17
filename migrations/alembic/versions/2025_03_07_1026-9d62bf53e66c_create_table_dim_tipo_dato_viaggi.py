"""create_table_dim_tipo_dato_viaggi

Revision ID: 9d62bf53e66c
Revises: c0884ea66fd8
Create Date: 2025-03-07 10:26:11.374070

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9d62bf53e66c"
down_revision: Union[str, None] = "c0884ea66fd8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_tipo_dato_viaggi",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_dato_viaggi")
