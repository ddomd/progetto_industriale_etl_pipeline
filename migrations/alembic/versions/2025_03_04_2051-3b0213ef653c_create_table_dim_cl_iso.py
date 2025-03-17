"""create table dim_CL_ISO

Revision ID: 3b0213ef653c
Revises: 
Create Date: 2025-03-04 20:51:38.178678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b0213ef653c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("dim_cl_iso", sa.Column("id", sa.String(50), primary_key=True), sa.Column("nome", sa.Text()))


def downgrade() -> None:
    op.drop_table("dim_cl_iso")
