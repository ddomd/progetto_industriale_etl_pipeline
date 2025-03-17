"""create_table_facts_turismo

Revision ID: 637662d46e57
Revises: 31dc1ed54a67
Create Date: 2025-03-06 15:29:01.810971

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "637662d46e57"
down_revision: Union[str, None] = "31dc1ed54a67"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "facts_turismo",
        sa.Column(
            "FREQ",
            sa.String(50),
            sa.ForeignKey("dim_cl_freq.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "REF_AREA",
            sa.String(50),
            sa.ForeignKey("dim_cl_itter107.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "DATA_TYPE",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_dato7.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "TYPE_ACCOMMODATION",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_alloggio2.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "ECON_ACTIVITY_NACE_2007",
            sa.String(50),
            sa.ForeignKey("dim_cl_ateco_2007.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "COUNTRY_RES_GUESTS",
            sa.String(50),
            sa.ForeignKey("dim_cl_iso.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "LOCALITY_TYPE",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipoitter1.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "URBANIZ_DEGREE",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipoitter1.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "COASTAL_AREA",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipoitter1.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "SIZE_BY_NUMBER_ROOMS",
            sa.String(50),
            sa.ForeignKey("dim_cl_numerosita.id", ondelete="CASCADE"),
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
    op.drop_table("facts_turismo")
