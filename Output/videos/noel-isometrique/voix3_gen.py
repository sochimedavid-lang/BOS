import voix_off as vo, voix_dyn as vd, urllib.error, time, pathlib, sys
vo.STYLE = vd.STYLE
cle = vo.lire_cle(); out = pathlib.Path('voix3'); out.mkdir(exist_ok=True); S = vd.SEGMENTS
MODELE = sys.argv[1] if len(sys.argv) > 1 else "gemini-3.8-flash-tts"
jobs = [("r1", S[0][2]), ("r2", S[1][2]), ("r3", "Minuit pile… … … Décollage !"), ("r4", S[4][2]),
        ("r5", "Tokyo ! … … Paris ! … … Cotonou ! … … New York !"), ("r6", S[9][2]), ("r7", S[10][2])]
for nom, txt in jobs:
    f = out / f"{nom}.wav"
    if f.exists(): continue
    for essai in range(10):
        try:
            pcm = vo.synthese(cle, MODELE, "Sulafat", txt)
            print(nom, f"{vo.ecrire_wav(f, pcm):.2f}s", txt, flush=True); break
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if (e.code == 503 or (e.code == 429 and "PerDay" not in body)) and essai < 9:
                print(nom, e.code, "nouvelle tentative…", flush=True); time.sleep(30 if e.code == 503 else 62); continue
            print(nom, "ERREUR", e.code, body[:200].replace("\n", " ")); raise SystemExit(1)
print("FINI")
