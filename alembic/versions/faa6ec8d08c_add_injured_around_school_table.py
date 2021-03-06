"""Add injured_around_school table

Revision ID: faa6ec8d08c
Revises: 57106d545c3f
Create Date: 2019-08-16 00:11:13.826663

"""

# revision identifiers, used by Alembic.
revision = 'faa6ec8d08c'
down_revision = '57106d545c3f'
branch_labels = None
depends_on = None

import sqlalchemy as sa

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('injured_around_school',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('school_id', sa.Integer(), nullable=True),
                    sa.Column('school_name', sa.Text(), nullable=True),
                    sa.Column('school_type', sa.Text(), nullable=True),
                    sa.Column('school_longitude', sa.Float(), nullable=True),
                    sa.Column('school_latitude', sa.Float(), nullable=True),
                    sa.Column('school_yishuv_name', sa.Text(), nullable=True),
                    sa.Column('school_anyway_link', sa.Text(), nullable=True),
                    sa.Column('involved_injury_severity', sa.Integer(), nullable=True),
                    sa.Column('involved_injury_severity_hebrew', sa.Text(), nullable=True),
                    sa.Column('accident_year', sa.Integer(), nullable=True),
                    sa.Column('distance_in_km', sa.Float(), nullable=True),
                    sa.Column('injured_count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_injured_around_school_id'), 'injured_around_school', ['id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_injured_around_school_id'), table_name='injured_around_school')
    op.drop_table('injured_around_school')
    ### end Alembic commands ###
