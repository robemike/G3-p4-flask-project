"""initial migration

Revision ID: 1a8b113de798
Revises: 
Create Date: 2024-07-15 06:57:19.334135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a8b113de798'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('my_shelf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    op.drop_table('my_shelf')
    op.drop_table('book')
    # ### end Alembic commands ###
