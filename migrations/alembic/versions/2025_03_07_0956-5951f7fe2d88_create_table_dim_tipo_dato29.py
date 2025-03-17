"""create_table_dim_tipo_dato29

Revision ID: 5951f7fe2d88
Revises: 637662d46e57
Create Date: 2025-03-07 09:56:29.245664

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5951f7fe2d88"
down_revision: Union[str, None] = "637662d46e57"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_tipo_dato29",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_dato29")
