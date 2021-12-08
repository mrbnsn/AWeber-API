from app import db, ma

# Widget Model
class Widget(db.Model):
    __table_args__ = (
        db.CheckConstraint('Length(name) <= 64'),
    )

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=False)
    num_parts = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name: str, num_parts: int):
        self.name = name
        self.num_parts = num_parts
        

# Widget Schema
class WidgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Widget


# Init schema
widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many=True)