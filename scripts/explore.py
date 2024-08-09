import marimo

__generated_with = "0.7.19"
app = marimo.App()


@app.cell
def __():
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import requests as req
    from rich import print as rp
    return np, os, pd, plt, req, rp


@app.cell
def __(os, req, rp):
    post_id = "CoGzQVFLqDB"
    url = f"https://www.instagram.com/p/{post_id}/media/?size=l"
    path_download = "../data/images/"

    response = req.get(url)
    if response.status_code == 200:
        # Download image
        try:
            # Create folder if not exist
            if not os.path.exists(path_download):
                os.makedirs(path_download)
            # Skip if file exist
            path_file = f"{path_download}{post_id}.jpg"
            if not os.path.exists(path_file):
                with open(path_file, "wb") as file:
                    file.write(response.content)
                rp(f"[green bold]Downloaded: {post_id}.[/green bold]")
            else:
                rp(f"[yellow bold]Skipped: {post_id}.[/yellow bold]")
        except Exception as e:
            rp(f"[red bold]Failed due to an error: {post_id}, {e}.[/red bold]")
    else:
        rp(f"[red bold]Failed: {post_id}.[/red bold]")
    return file, path_download, path_file, post_id, response, url


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
