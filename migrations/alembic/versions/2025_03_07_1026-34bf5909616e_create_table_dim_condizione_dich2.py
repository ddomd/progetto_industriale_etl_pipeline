"""create_table_dim_condizione_dich2

Revision ID: 34bf5909616e
Revises: 9e005d888e20
Create Date: 2025-03-07 10:26:58.372235

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "34bf5909616e"
down_revision: Union[str, None] = "9e005d888e20"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_condizione_dich2",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_condizione_dich2")
