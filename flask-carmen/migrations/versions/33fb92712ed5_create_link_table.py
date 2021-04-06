"""create Link Table

Revision ID: 33fb92712ed5
Revises: a96c4798273c
Create Date: 2021-04-06 11:13:56.640777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33fb92712ed5'
down_revision = 'a96c4798273c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('link_id', sa.Integer(), nullable=False),
    sa.Column('link_name', sa.String(length=30), nullable=True),
    sa.Column('link_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('link_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    # ### end Alembic commands ###