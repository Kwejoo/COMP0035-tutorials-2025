from __future__ import annotations

from importlib import resources

from sqlmodel import Field, MetaData, SQLModel, create_engine

from activities import data

SQLModel.metadata = MetaData()


class Paralympics(SQLModel, table=True):
    __tablename__ = "Games"
    id: int | None = Field(default=None, primary_key=True)
    type: str | None
    year: int | None
    country: str | None
    host: str | None
    start: str | None
    end: str | None
    disabilities_included: str | None
    countries: int | None
    events: int | None
    sports: int | None
    participants_m: int | None
    participants_f: int | None
    participants: int | None
    highlights: str | None
    URL: str | None


class NPCCodes(SQLModel, table=True):
    __tablename__ = "NPCCodes"
    Code: str = Field(default=None, primary_key=True)
    Name: str
    Region: str | None = Field(default=None, nullable=True)
    SubRegion: str | None
    MemberType: str | None
    Notes: str | None


def create_db():
    sqlite_file_name = resources.files(data).joinpath("para-not-normalised.sqlite")
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine_u = create_engine(sqlite_url)
    SQLModel.metadata.create_all(engine_u)
    return engine_u

