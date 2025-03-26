import marimo

__generated_with = "0.11.28"
app = marimo.App()


app._unparsable_cell(
    r"""
    !pip install mplstereonet
    """,
    name="_"
)


@app.cell
def _():
    import matplotlib.pyplot as plt
    import mplstereonet
    return mplstereonet, plt


@app.cell
def _(plt):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='stereonet')

    # Measurements follow the right-hand-rule to indicate dip direction
    strike, dip = [315,320], [30,40]

    ax.plane(strike, dip, 'g-', linewidth=2)
    ax.pole(strike, dip, 'go', markersize=5)

    ax.grid()

    plt.show()
    return ax, dip, fig, strike


if __name__ == "__main__":
    app.run()
