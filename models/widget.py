'''Widget Model and Schema'''

from app import db, ma


class Widget(db.Model):
    '''The Widget model'''
    __table_args__ = (
        db.CheckConstraint('Length(name) <= 64'),
    )

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=False)
    num_parts = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        server_default=db.func.now())
    updated = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, name: str, num_parts: int):
        self.name = name
        self.num_parts = num_parts


class WidgetSchema(ma.SQLAlchemyAutoSchema):
    '''Widget Schema definition'''
    class Meta:
        '''Assign Widget class to Meta model'''
        model = Widget


# Init schema
widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many=True)
