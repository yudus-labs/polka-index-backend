from pathlib import Path
import polka_index_backend as pib

cfg_path = Path(__file__).parent.joinpath('.cfg', 'config.yml')

app = pib.create_app(cfg_path)


if __name__ == '__main__':
    app.run()
