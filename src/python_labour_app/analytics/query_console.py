import marimo

__generated_with = "0.19.11"
app = marimo.App(width="full", app_title="Query Console")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # SQL Query Console
    """)
    return


@app.cell
def _():
    import marimo as mo
    import os
    import sqlalchemy

    return mo, os, sqlalchemy


@app.cell
def _(os, sqlalchemy):
    # Vonnect to postgres
    _password = os.environ.get("POSTGRES_PASSWORD")
    _username = os.environ.get("POSTGRES_USER")
    _database = os.environ.get("POSTGRES_DB")
    # postgresql to use psycopg2, posgresql+psycopg to use psycopg3

    DATABASE_URL = f"postgresql+psycopg://{_username}:{_password}@db:5432/{_database}"
    engine = sqlalchemy.create_engine(DATABASE_URL)
    return (engine,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * from information_schema.tables;
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
