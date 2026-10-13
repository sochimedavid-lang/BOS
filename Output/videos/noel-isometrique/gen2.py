"""Version dynamique (37 s, rythme d'origine) avec voix rapide + bruitages : build-h2/ et build-v2/."""
import json, pathlib, shutil
import gen

ICI = pathlib.Path(__file__).resolve().parent
TOTAL = 37
AUDIO = f'      <audio id="mix" src="mix.wav" data-start="0" data-duration="{TOTAL}" data-track-index="10"></audio>\n    </div>\n\n    <script>'


def build(nom, html):
    d = ICI / nom; d.mkdir(exist_ok=True)
    for f in ["package.json", "hyperframes.json"]:
        shutil.copy(ICI / f, d / f)
    (d / "meta.json").write_text(json.dumps({"id": f"noel-{nom}", "name": f"noel-{nom}"}), encoding="utf-8")
    (d / "index.html").write_text(html, encoding="utf-8")
    shutil.copy(ICI / "audio" / "mix.wav", d / "mix.wav")


if __name__ == "__main__":
    src = (ICI / "index.html").read_text(encoding="utf-8").replace('    </div>\n\n    <script>', AUDIO, 1)
    build("build-h2", src)
    build("build-v2", gen.vertical(src))
    print("OK : build-h2/ et build-v2/")
