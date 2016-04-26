from sqlalchemy import Column, Integer, String, DateTime
from database.storage import Base

class ScanEvent(Base):
    __tablename__ = 'scanevent'
    id = Column(Integer, primary_key=True)
    barcode = Column(String(20), unique=False)
    timestamp = Column(DateTime(), unique=False)

    def __init__(self, barcode=None, timestamp=None):
        self.barcode = barcode
        self.timestamp = timestamp

    def __repr__(self):
        return '<Barcode %r>' % (self.barcode)
