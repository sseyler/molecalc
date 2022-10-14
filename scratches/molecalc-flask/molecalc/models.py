import gzip
import io

import numpy as np

from .extensions import db

import sqlalchemy as sa
from sqlalchemy import (
    # Column,
    DateTime,
    Float,
    # Integer,
    LargeBinary,
    String,
    create_engine,
)

# Alias common SQLAlchemy names
Column = db.Column
Model = db.Model
Integer = db.Integer


def compress(s):
    if type(s) == str:
        s = s.encode()
    b = gzip.compress(s)
    return b


def decompress(b):
    s = gzip.decompress(b)
    return s


class CompressedString(sa.types.TypeDecorator):
    """Storage datatype for large blobs of text."""

    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        return compress(value)

    def process_result_value(self, value, dialect):
        return decompress(value)


class NumpyArray(sa.types.TypeDecorator):
    """Storage datatype for numpy arrays."""

    impl = LargeBinary

    def save_array(arr):
        s = io.StringIO()
        np.savetxt(s, arr)
        return s.getvalue()

    def load_array(txt):
        s = io.StringIO(txt)
        arr = np.loadtxt(s)
        return arr

    def process_bind_param(self, value, dialect):
        value = self.save_array(value)
        return compress(value)

    def process_result_value(self, value, dialect):
        value = decompress(value)
        value = self.load_array(value)
        return value


# def db_connect():
#     """Performs database connection using database settings from settings.py.
#       Returns sqlalchemy engine instance"""
#     connect_string = "sqlite:///database.sqlite"
#     return create_engine(connect_string)


class GamessCalculation(Model):
    __tablename__ = 'gamess-calculations'
    id = Column(Integer, primary_key=True)

    # Basic descriptors
    hashkey = Column(String, unique=True)
    created = Column(DateTime)
    name = Column(String)
    smiles = Column(String)
    sdf = Column(String)
    mol2 = Column(String)
    svg = Column(String)
    coordinates = Column(String)
    theorylvl = Column(String)

    # GAMESS Results
    enthalpy = Column(Float)
    charges = Column(String)

    islinear = Column(String)
    vibjsmol = Column(CompressedString)
    vibfreq = Column(String)
    vibintens = Column(String)
    thermo = Column(String)

    orbitals = Column(String)
    orbitalstxt = Column(CompressedString)

    soltotal = Column(Float)
    solpolar = Column(Float)
    solnonpolar = Column(Float)
    solsurface = Column(Float)
    soldipole = Column(String)
    soldipoletotal = Column(Float)

    def __repr__(self):
        fmt = '<GamessCalculation {:} {:} >'
        return fmt.format(self.smiles, self.hashkey)


class Counter(Model):
    __tablename__ = "molecules"
    smiles = Column(String, primary_key=True)
    count = Column(Integer)

    def __repr__(self):
        fmt = '<Molecule {:} {:} >'
        return fmt.format(self.smiles, self.count)


# def initialize_db(engine):
#     Base.metadata.create_all(engine)
#     return


# if __name__ == "__main__":
#     engine = db_connect()
#     initialize_db(engine)
