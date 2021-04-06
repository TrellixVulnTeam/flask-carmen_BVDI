"""change Category

Revision ID: 1828f83e49f7
Revises: 21a10dc65fe9
Create Date: 2021-04-06 19:08:14.543902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1828f83e49f7'
down_revision = '21a10dc65fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
