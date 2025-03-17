"""create table dim_CL_ITTER_107

Revision ID: 047c6bef0d80
Revises: 3b0213ef653c
Create Date: 2025-03-04 21:29:08.298032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '047c6bef0d80'
down_revision: Union[str, None] = '3b0213ef653c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("dim_cl_itter107", sa.Column("id", sa.String(50), primary_key=True), sa.Column("nome", sa.Text()))


def downgrade() -> None:
    op.drop_table("dim_cl_itter107")
