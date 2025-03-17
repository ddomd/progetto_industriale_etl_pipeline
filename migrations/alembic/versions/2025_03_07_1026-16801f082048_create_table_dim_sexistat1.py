"""create_table_dim_sexistat1

Revision ID: 16801f082048
Revises: 116259842bd3
Create Date: 2025-03-07 10:26:40.601264

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "16801f082048"
down_revision: Union[str, None] = "116259842bd3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_sexistat1",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_sexistat1")
