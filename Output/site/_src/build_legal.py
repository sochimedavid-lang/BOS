# Génère les pages légales du site Vibe Motion à partir des infos ci-dessous.
# Remplir INFO puis relancer : python3 _src/build_legal.py
import html, os
INFO = {
  "editeur": "Vibe Motion",        # nom complet ou nom de l'entreprise
  "statut": "",         # ex. « entrepreneur individuel », « SARL »
  "ifu_rccm": "",       # numéro IFU et/ou RCCM (facultatif si pas encore immatriculé)
  "adresse": "Cotonou",        # ville + quartier ou adresse
  "email": "risenofm@gmail.com",          # e-mail de contact
  "whatsapp": "",       # numéro WhatsApp au format international, ex. 22990000000
}
MAJ = "13 octobre 2026"
def v(k, label):
    return html.escape(INFO[k]) if INFO[k] else f'<mark>[à compléter : {label}]</mark>'
wa = (f'<a href="https://wa.me/{INFO["whatsapp"]}">WhatsApp +{INFO["whatsapp"]}</a>' if INFO["whatsapp"] else v("whatsapp","numéro WhatsApp"))
mail = (f'<a href="mailto:{INFO["email"]}">{html.escape(INFO["email"])}</a>' if INFO["email"] else v("email","e-mail de contact"))
CONTACT = f'{wa} ou {mail}' if INFO["whatsapp"] else mail

PAGES = {
"mentions-legales": ("Mentions légales", f"""
<h2>Éditeur du site</h2>
<p>Le site vibemotionafrica.com et la formation Vibe Motion sont édités par {v("editeur","nom ou raison sociale")}{(", " + html.escape(INFO["statut"])) if INFO["statut"] else ""}, {v("adresse","adresse")}, Bénin.</p>
{('<p>Identifiant fiscal / registre : ' + html.escape(INFO["ifu_rccm"]) + '.</p>') if INFO["ifu_rccm"] else ""}
<p>Contact : {CONTACT}.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis (vercel.com). Le nom de domaine est enregistré auprès de Hostinger.</p>
<h2>Paiement</h2>
<p>Les paiements sont traités par la plateforme Chariow et ses partenaires de paiement (Mobile Money, carte bancaire). Vibe Motion n'a jamais accès à tes données bancaires.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, vidéos, modèles, instructions et supports de la formation sont la propriété de l'éditeur. Ils sont réservés à l'usage personnel de l'acheteur : leur revente, partage ou diffusion, même partiels, sont interdits sans accord écrit.</p>
<p>Les vidéos présentées en exemple ont été créées par Vibe Motion. Les marques citées (Claude, Anthropic, Meta, TikTok, Google, YouTube…) appartiennent à leurs propriétaires respectifs. Vibe Motion est une formation indépendante, non affiliée à ces entreprises.</p>
<h2>Résultats</h2>
<p>Les exemples de prix et toute référence à des revenus illustrent des situations possibles et ne constituent pas une promesse de résultat. Tes résultats dépendent de ton implication, de ton temps et de ton marché.</p>
"""),
"conditions-de-vente": ("Conditions générales de vente", f"""
<h2>1. Objet</h2>
<p>Les présentes conditions encadrent la vente de la formation en ligne Vibe Motion, éditée par {v("editeur","nom ou raison sociale")} (ci-après « Vibe Motion »), à toute personne qui l'achète sur vibemotionafrica.com (ci-après « l'élève »). Tout achat vaut acceptation de ces conditions.</p>
<h2>2. Contenu de la formation</h2>
<p>La formation comprend les modules vidéo et écrits décrits sur la page de vente, les instructions et modèles fournis, et l'accès à la communauté WhatsApp privée. Elle se suit depuis un téléphone ou un ordinateur, avec une connexion internet.</p>
<p>Certains outils utilisés pendant la formation sont des services tiers (par exemple Claude). Leur éventuel abonnement est payé directement par l'élève à ces services et n'est pas inclus dans le prix de la formation.</p>
<h2>3. Prix et paiement</h2>
<p>Le prix est celui affiché sur la page au moment de l'achat, en francs CFA, toutes taxes comprises le cas échéant. Le prix de lancement est réservé aux 50 premiers élèves ; il peut ensuite évoluer sans effet sur les achats déjà réalisés. Le paiement est unique et se fait via Chariow (Mobile Money ou carte).</p>
<h2>4. Accès</h2>
<p>L'accès est envoyé juste après la confirmation du paiement. Il est personnel, non cessible, et valable à vie tant que la formation est proposée. En cas de souci d'accès, contacte-nous : {CONTACT}.</p>
<h2>5. Garantie 7 jours</h2>
<p>La formation est couverte par la garantie « ta première vidéo en 7 jours ou remboursé », décrite sur la page <a href="/remboursement">Remboursement</a>.</p>
<h2>6. Utilisation</h2>
<p>Le contenu est réservé à l'usage personnel de l'élève. Tout partage d'accès, revente ou diffusion entraîne la fermeture de l'accès sans remboursement. Les vidéos que l'élève crée pour lui-même ou pour ses clients lui appartiennent.</p>
<h2>7. Responsabilité</h2>
<p>Vibe Motion transmet une méthode et des outils. L'élève reste seul responsable de leur mise en œuvre, des contenus qu'il crée et de ses relations avec ses clients. Aucun revenu n'est garanti.</p>
<h2>8. Litiges</h2>
<p>En cas de difficulté, écris-nous d'abord : nous cherchons toujours une solution à l'amiable. À défaut, le droit béninois s'applique et les tribunaux de Cotonou sont compétents.</p>
"""),
"remboursement": ("Politique de remboursement", f"""
<h2>La garantie</h2>
<p><b>Ta première vidéo motion en 7 jours, ou remboursé.</b> Si tu suis les modules 0 à 2 et fais les exercices, et qu'au bout de 7 jours après ton achat tu n'as pas réussi à exporter ta première vidéo motion, on te rembourse intégralement.</p>
<h2>Comment demander un remboursement</h2>
<ol>
<li>Écris-nous dans les 7 jours qui suivent ton achat : {CONTACT}.</li>
<li>Indique le nom ou le numéro utilisé pour payer, et la date d'achat.</li>
<li>Montre-nous rapidement où tu en es (captures de tes exercices des modules 0 à 2) : on essaie d'abord de te débloquer. Si ça ne suffit pas, on te rembourse.</li>
</ol>
<h2>Délai et mode de remboursement</h2>
<p>Le remboursement est fait sur le moyen de paiement utilisé (Mobile Money ou carte), sous 7 jours ouvrés après l'accord. L'accès à la formation et à la communauté est alors fermé.</p>
<h2>Cas non couverts</h2>
<ul>
<li>Demande faite plus de 7 jours après l'achat.</li>
<li>Formation partagée, revendue ou diffusée.</li>
<li>Demande portant sur les revenus obtenus : la garantie porte sur ta première vidéo, pas sur un résultat financier.</li>
</ul>
"""),
"confidentialite": ("Politique de confidentialité", f"""
<h2>Qui est responsable de tes données</h2>
<p>{v("editeur","nom ou raison sociale")}, {v("adresse","adresse")}, Bénin. Contact : {CONTACT}.</p>
<h2>Les données collectées</h2>
<ul>
<li><b>Lors de l'achat :</b> nom, numéro de téléphone, e-mail et informations de paiement, collectés par Chariow et ses partenaires de paiement. Nous recevons ton nom, ton contact et la confirmation du paiement, jamais tes données bancaires.</li>
<li><b>Dans la communauté WhatsApp :</b> ton nom et ton numéro, visibles des autres membres du groupe.</li>
<li><b>Sur le site :</b> des données de navigation (pages vues, appareil) via des outils de mesure et, le cas échéant, le pixel Meta, pour mesurer l'efficacité de nos publicités.</li>
</ul>
<h2>Pourquoi</h2>
<p>Pour te donner accès à la formation, t'accompagner, traiter une éventuelle demande de remboursement, et améliorer nos publicités. Nous ne vendons jamais tes données.</p>
<h2>Combien de temps</h2>
<p>Tant que tu as accès à la formation, puis au maximum 3 ans après ton dernier contact, sauf obligation légale de conservation plus longue (comptabilité).</p>
<h2>Tes droits</h2>
<p>Conformément au Code du numérique du Bénin (loi n° 2017-20), tu peux demander l'accès, la correction ou la suppression de tes données, et t'opposer à leur utilisation publicitaire : écris-nous à {CONTACT}. Tu peux aussi saisir l'Autorité de protection des données à caractère personnel (APDP).</p>
<h2>Cookies et pixel</h2>
<p>Le site peut utiliser des cookies de mesure et le pixel Meta. Tu peux les bloquer dans les réglages de ton navigateur ; le site continue de fonctionner.</p>
"""),
}

TPL = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Vibe Motion</title>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2092809134709164');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2092809134709164&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#100E0C;--s1:#1A1714;--line:rgba(255,236,214,.09);--text:#F6F1EA;--mut:#A39A8F;--acc:#F4511E}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:Inter,system-ui,sans-serif;line-height:1.7;font-size:15.5px}}
.w{{max-width:720px;margin:0 auto;padding:28px 20px 80px}}
.back{{display:inline-block;color:var(--mut);text-decoration:none;font-size:14px;margin-bottom:28px}}
.back:hover{{color:var(--text)}}
h1{{font-family:"Bricolage Grotesque",sans-serif;font-size:clamp(28px,6vw,40px);line-height:1.15;margin-bottom:6px}}
.maj{{color:var(--mut);font-size:13px;margin-bottom:28px}}
h2{{font-family:"Bricolage Grotesque",sans-serif;font-size:19px;margin:30px 0 8px}}
p,li{{color:#D9D1C6}} p+p{{margin-top:10px}}
ul,ol{{padding-left:22px;display:grid;gap:8px}}
a{{color:var(--acc)}} b{{color:var(--text)}}
mark{{background:#FFE36E;color:#111;padding:0 4px;border-radius:4px;font-weight:600}}
footer{{border-top:1px solid var(--line);margin-top:48px;padding-top:20px;font-size:13px;color:var(--mut);display:flex;flex-wrap:wrap;gap:8px 18px}}
footer a{{color:var(--mut)}}
</style></head><body><div class="w">
<a class="back" href="/">← Retour à Vibe Motion</a>
<h1>{title}</h1><p class="maj">Dernière mise à jour : {maj}</p>
{body}
<footer><a href="/mentions-legales">Mentions légales</a><a href="/conditions-de-vente">Conditions de vente</a><a href="/remboursement">Remboursement</a><a href="/confidentialite">Confidentialité</a><span>© 2026 Vibe Motion</span></footer>
</div></body></html>
"""
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
missing = [k for k,x in INFO.items() if not x and k not in ("statut","ifu_rccm","whatsapp")]
for slug,(title,body) in PAGES.items():
    open(os.path.join(root, slug + ".html"), "w").write(TPL.format(title=title, maj=MAJ, body=body.strip()))
print("pages générées ; infos manquantes :", ", ".join(missing) or "aucune")
