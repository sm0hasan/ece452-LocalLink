"""added more attributes to user

Revision ID: a45bb1eb89bd
Revises: 692d96b0c868
Create Date: 2024-07-19 04:48:48.877921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45bb1eb89bd'
down_revision = '692d96b0c868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('events', schema=None) as batch_op:
    #     batch_op.alter_column('eventID',
    #            existing_type=sa.VARCHAR(),
    #            type_=sa.Integer(),
    #            existing_nullable=False,
    #            autoincrement=True,
    #            existing_server_default=sa.text('nextval(\'"events_eventID_seq"\'::regclass)'))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('events', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('volunteerHours', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('timeZone', sa.String(), nullable=True))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('timeZone')
        batch_op.drop_column('volunteerHours')
        batch_op.drop_column('events')

    # with op.batch_alter_table('events', schema=None) as batch_op:
    #     batch_op.alter_column('eventID',
    #            existing_type=sa.Integer(),
    #            type_=sa.VARCHAR(),
    #            existing_nullable=False,
    #            autoincrement=True,
    #            existing_server_default=sa.text('nextval(\'"events_eventID_seq"\'::regclass)'))

    # ### end Alembic commands ###
