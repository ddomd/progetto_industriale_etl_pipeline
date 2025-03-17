"""create_table_facts_pernottamenti

Revision ID: fb6cdc1f0fba
Revises: 34bf5909616e
Create Date: 2025-03-07 10:30:32.632609

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fb6cdc1f0fba"
down_revision: Union[str, None] = "34bf5909616e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "facts_pernottamenti",
        sa.Column(
            "FREQ",
            sa.String(50),
            sa.ForeignKey("dim_cl_freq.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "RESIDENCE_TERR",
            sa.String(50),
            sa.ForeignKey("dim_cl_itter107.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "DATA_TYPE",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_dato_viaggi.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "MAIN_DESTINATION",
            sa.String(50),
            sa.ForeignKey("dim_cl_iso.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "TYPE_TRIP",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_viaggio2.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "MAIN_TYPE_ACCOMMODATION",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_alloggio.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "SEX",
            sa.String(50),
            sa.ForeignKey("dim_cl_sexistat1.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "AGE",
            sa.String(50),
            sa.ForeignKey("dim_cl_eta1.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "LABPROF_STATUS_C",
            sa.String(50),
            sa.ForeignKey("dim_cl_condizione_dich2.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "TIME_PERIOD",
            sa.String(10),
        ),
        sa.Column(
            "OBS_VALUE",
            sa.FLOAT(),
        ),
    )


def downgrade() -> None:
    op.drop_table("facts_pernottamenti")
