"""empty message

Revision ID: 1a458f9d2902
Revises: 2c635c20ae8e
Create Date: 2023-04-16 14:34:18.063141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a458f9d2902'
down_revision = '2c635c20ae8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_photo', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Posts', schema=None) as batch_op:
        batch_op.drop_column('profile_photo')

    # ### end Alembic commands ###