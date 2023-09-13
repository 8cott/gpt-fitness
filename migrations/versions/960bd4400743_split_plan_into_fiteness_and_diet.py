"""Split plan into fiteness and diet

Revision ID: 960bd4400743
Revises: 619e40c38e74
Create Date: 2023-09-13 11:27:14.089237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960bd4400743'
down_revision = '619e40c38e74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_plans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fitness_plan', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('diet_plan', sa.Text(), nullable=True))
        batch_op.drop_column('plan')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_plans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plan', sa.TEXT(), autoincrement=False, nullable=False))
        batch_op.drop_column('diet_plan')
        batch_op.drop_column('fitness_plan')

    # ### end Alembic commands ###
