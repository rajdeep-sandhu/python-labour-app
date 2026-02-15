import marimo

__generated_with = "0.19.11"
app = marimo.App(width="full", app_title="Qquey Console")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # SQL Query Console
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
