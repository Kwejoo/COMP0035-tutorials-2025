from importlib import resources

from sqlmodel import Field, MetaData, Relationship, SQLModel, create_engine

from activities import data

metadata = MetaData()
SQLModel.metadata = metadata


class GamesHost(SQLModel, table=True):
    __tablename__ = "GamesHost"
    id: int | None = Field(default=None, primary_key=True)
    games_id: int = Field(default=None, foreign_key="Games.id")
    host_id: int = Field(default=None, foreign_key="Host.id")


class GamesDisability(SQLModel, table=True):
    __tablename__ = "GamesDisability"
    id: int | None = Field(default=None, primary_key=True)
    games_id: int = Field(default=None, foreign_key="Games.id")
    disability_id: int = Field(default=None, foreign_key="Disability.id")


class GamesTeam(SQLModel, table=True):
    __tablename__ = "GamesTeam"
    id: int | None = Field(default=None, primary_key=True)
    games_id: int = Field(default=None, foreign_key="Games.id")
    team_id: str = Field(default=None, foreign_key="Team.code")


class Games(SQLModel, table=True):
    __tablename__ = "Games"
    id: int | None = Field(default=None, primary_key=True)
    type: str | None
    year: int | None
    start: str | None
    end: str | None
    countries: int | None
    events: int | None
    sports: int | None
    participants_m: int | None
    participants_f: int | None
    participants: int | None
    highlights: str | None
    URL: str | None

    hosts: list["Host"] = Relationship(back_populates="games", link_model=GamesHost)
    disabilities: list["Disability"] = Relationship(back_populates="games", link_model=GamesDisability)
    teams: list["Team"] = Relationship(back_populates="games", link_model=GamesTeam)


class Team(SQLModel, table=True):
    __tablename__ = "Team"
    code: str | None = Field(default=None, primary_key=True)
    name: str
    region: str | None
    sub_region: str | None
    member_type: str | None
    notes: str | None
    country_id: str | None = Field(default=None, foreign_key="Country.id")

    games: list["Games"] = Relationship(back_populates="teams", link_model=GamesTeam)


class Disability(SQLModel, table=True):
    __tablename__ = "Disability"
    id: int | None = Field(default=None, primary_key=True)
    description: str

    games: list["Games"] = Relationship(back_populates="disabilities", link_model=GamesDisability)


class Host(SQLModel, table=True):
    __tablename__ = "Host"
    id: int | None = Field(default=None, primary_key=True)
    place_name: str
    country_id: int | None = Field(default=None, foreign_key="Country.id")

    games: list["Games"] = Relationship(back_populates="hosts", link_model=GamesHost)


class Country(SQLModel, table=True):
    __tablename__ = "Country"
    id: int | None = Field(default=None, primary_key=True)
    country: str


def create_norm_db():
    sqlite_file_name = resources.files(data).joinpath("para-normalised.db")
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine_n = create_engine(sqlite_url)
    metadata.create_all(engine_n)
    return engine_n
