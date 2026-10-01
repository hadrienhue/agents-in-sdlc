"""Tunnel systeme.io BioConnect × Spengler : capture -> merci -> vente.

Génère des blocs « Code HTML » autonomes (pas de DOCTYPE/html/head/body),
avec un design system commun : variables CSS, logo SVG en base64,
container queries à 700 px.
"""
import base64, os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PREV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_apercu/")
os.makedirs(PREV, exist_ok=True)

# ------------------------------------------------------------------ logo
LOGO_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 232 46">'
    '<rect x="0" y="2" width="46" height="40" rx="6" fill="#F26B1D"/>'
    '<path d="M4 23h10l4-9 5 17 4-12 3 4h12" fill="none" stroke="#fff" stroke-width="3" '
    'stroke-linejoin="round" stroke-linecap="round"/>'
    '<text x="58" y="19" fill="#F26B1D" font-family="Arial,Helvetica,sans-serif" font-size="20" '
    'font-weight="700" letter-spacing="4">BIO</text>'
    '<text x="58" y="39" fill="#F26B1D" font-family="Arial,Helvetica,sans-serif" font-size="20" '
    'font-weight="700" letter-spacing="1.5" textLength="150">CONNECT</text>'
    '<path d="M58 43h172" stroke="#F26B1D" stroke-width="1.6"/></svg>'
)
LOGO_B64 = "data:image/svg+xml;base64," + base64.b64encode(LOGO_SVG.encode()).decode()
LOGO = f'<img class="bc-logo" src="{LOGO_B64}" alt="BioConnect">'
BRAND = f'<div class="brand">{LOGO}<span class="bc-x">× <span>♥</span> Spengler</span></div>'

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>'

# ------------------------------------------------------------------ design system
DS = r"""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap');
.bcf{--or:#F26B1D;--or-d:#D9550B;--or-l:#FFA266;--red:#E8452F;--navy:#0B2341;--navy-2:#071A31;--txt:#2B3240;--mut:#5E6675;--cream:#FFF4EC;--lav:#F2EFFA;--line:#ECE6E0;
  --ok:#1E8E4E;--ok-bg:#E8F6EE;--warn:#B45A0A;--warn-bg:#FDF1E4;--bad:#C0322B;--bad-bg:#FBE8E7;--r:18px;
  --f-serif:'DM Serif Display',Georgia,serif;--f-sans:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  container-type:inline-size;container-name:bcf;width:100%;text-align:left;
  font-family:var(--f-sans);color:var(--txt);background:#fff;line-height:1.6;font-size:16px;-webkit-font-smoothing:antialiased}
.bcf *,.bcf *::before,.bcf *::after{box-sizing:border-box}
.bcf h1,.bcf h2,.bcf h3,.bcf p,.bcf ul,.bcf li{margin:0;padding:0;text-align:inherit;text-transform:none;font-style:normal;letter-spacing:normal;line-height:inherit}
.bcf p,.bcf li{font-size:inherit;color:inherit;font-family:inherit}
.bcf img{max-width:100%;display:block}
.bcf a{color:inherit}
.bcf a.btn,.bcf a.btn:hover{color:#fff;text-decoration:none}
.bcf .wrap{max-width:1100px;margin:0 auto;padding:0 24px}
.bcf .sec{padding:68px 0}
.bcf .serif{font-family:var(--f-serif);font-weight:400;color:var(--navy);letter-spacing:-.01em}
.bcf .h1{font-size:52px;line-height:1.08}
.bcf .h2{font-size:38px;line-height:1.15}
.bcf .accent{color:var(--or)}
.bcf .kicker{display:block;font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--or);margin-bottom:14px}
.bcf .center{text-align:center;max-width:720px;margin:0 auto}
.bcf .center .sub{margin-top:12px;color:var(--mut)}
.bcf .muted{color:var(--mut)}
.bcf .bg-cream{background:var(--cream)}.bcf .bg-lav{background:var(--lav)}.bcf .bg-navy{background:var(--navy);color:#C9D3E3}
.bcf .grid2{display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:center}
.bcf .grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.bcf .grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
/* bouton */
.bcf .btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--or);color:#fff;font-weight:700;font-size:16px;letter-spacing:.03em;text-transform:uppercase;padding:18px 34px;border-radius:999px;border:0;cursor:pointer;box-shadow:0 10px 24px -10px rgba(242,107,29,.7);transition:transform .15s,background .15s}
.bcf .btn:hover{background:var(--or-d);transform:translateY(-2px)}
.bcf .btn svg{width:16px;height:16px}
.bcf .btn.ghost{background:transparent;color:var(--navy)!important;border:2px solid var(--navy);box-shadow:none}
/* liste à coches */
.bcf .checks{list-style:none}
.bcf .checks li{display:flex;gap:12px;align-items:flex-start;margin-bottom:12px}
.bcf .checks li::before{content:"✓";flex:0 0 22px;height:22px;border-radius:50%;background:var(--or);color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
/* emplacement image */
.bcf .ph{position:relative;background:linear-gradient(135deg,#F4F1EE,#E9E4DF);border-radius:var(--r);overflow:hidden;display:flex;align-items:center;justify-content:center;color:#9a9188;font-size:14px;text-align:center}
.bcf .ph::before{content:attr(data-label);position:absolute;padding:16px}
.bcf .ph img{position:relative;z-index:1;width:100%;height:100%;object-fit:contain}
.bcf .ph.cover img{object-fit:cover}
/* carte */
.bcf .card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:22px}
.bcf .card h3{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:6px}
.bcf .card p{font-size:14.5px;color:var(--mut)}
/* en-tête (couverture du guide) */
.bcf .hdr{background:var(--navy);background-image:radial-gradient(circle at 92% -40%,rgba(255,255,255,.08) 0 160px,transparent 161px)}
.bcf .hdr .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:76px}
.bcf .brand{display:flex;align-items:center;gap:20px}
.bcf .bc-logo{height:38px;width:auto}
.bcf .bc-x{color:#fff;font-weight:700;font-size:17px;white-space:nowrap}
.bcf .pill{background:var(--red);color:#fff!important;font-weight:700;font-size:13px;letter-spacing:.14em;text-transform:uppercase;padding:11px 22px;border-radius:999px;white-space:nowrap;text-decoration:none}
.bcf .subhdr{background:var(--navy);border-top:1px solid rgba(255,255,255,.08);color:#C9D3E3;font-size:12px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;text-align:center;padding:9px 16px}
.bcf .subhdr span{display:inline-block;border-bottom:2px solid var(--or);padding-bottom:3px}
/* pied de page (pages intérieures du guide) */
.bcf .foot{background:var(--navy);color:#C9D3E3;padding:52px 0 26px;background-image:radial-gradient(circle at 0% 110%,rgba(232,69,47,.3) 0 170px,transparent 171px)}
.bcf .foot .row{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px}
.bcf .foot .ref{font-size:12px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#fff;margin-top:14px}
.bcf .foot .ref::after{content:"";display:block;width:56px;height:3px;background:var(--or);margin-top:8px}
.bcf .fnums{display:flex;flex-wrap:wrap;gap:18px}
.bcf .fnum{display:flex;flex-direction:column;align-items:center;gap:6px;color:#fff;font-size:12.5px;text-align:center;min-width:76px}
.bcf .fnum i{width:48px;height:48px;border-radius:50%;border:1px solid rgba(255,255,255,.3);display:flex;align-items:center;justify-content:center;font-style:normal}
.bcf .fnum i svg{width:22px;height:22px}
.bcf .fnum b{background:var(--red);color:#fff;border-radius:999px;padding:2px 12px;font-size:15px;white-space:nowrap}
.bcf .retenir{background:#fff;color:var(--navy);border-radius:16px;padding:18px 22px;margin:34px 0 26px;font-size:14px}
.bcf .retenir strong{display:block;font-size:13px;letter-spacing:.06em;margin-bottom:4px}
.bcf .fcontact{display:flex;flex-wrap:wrap;justify-content:center;gap:10px 26px;margin-bottom:20px;font-size:14px}
.bcf .fcontact a{color:#fff;text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.bcf .fcontact svg{width:18px;height:18px}
.bcf .edit{border-top:1px solid rgba(255,255,255,.18);padding-top:20px;text-align:center;font-size:13px;line-height:1.7}
.bcf .edit a{color:#C9D3E3;margin:0 8px}
.bcf .edit .legal{margin-top:10px;font-size:12px;opacity:.85}
/* ---------- container query : bloc ≤ 700 px ---------- */
@container bcf (max-width:700px){
  .wrap{padding:0 16px}
  .sec{padding:48px 0}
  .h1{font-size:34px}
  .h2{font-size:28px}
  .grid2{grid-template-columns:1fr;gap:30px}
  .grid3,.grid4{grid-template-columns:1fr}
  .btn{width:100%;padding:17px 18px;font-size:15px}
  .hdr .wrap{height:64px}
  .bc-logo{height:30px}
  .bc-x{font-size:14px}
  .brand{gap:12px}
  .pill{font-size:10.5px;padding:8px 12px;letter-spacing:.1em}
  .foot .row{flex-direction:column;align-items:flex-start}
  .fnums{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;width:100%}
  .fnum{min-width:0;font-size:11px}
  .fnum b{font-size:13px;padding:2px 8px}
  .fnum i{width:40px;height:40px}
  .foot{background-image:radial-gradient(circle at 0% 110%,rgba(232,69,47,.25) 0 110px,transparent 111px)}
}
@container bcf (max-width:420px){.pill{display:none}.hdr .wrap{justify-content:center}}
</style>"""

def header(pill, href=None):
    tag = f'<a class="pill" href="{href}">{pill}</a>' if href else f'<span class="pill">{pill}</span>'
    return f"""  <div class="hdr"><div class="wrap">
    {BRAND}
    {tag}
  </div></div>
  <div class="subhdr"><span>Santé à domicile</span></div>
"""

FOOTER = f"""  <div class="foot"><div class="wrap">
    <div class="row">
      <div>{BRAND}<div class="ref">Document de référence</div></div>
      <div class="fnums">
        <div class="fnum"><i><svg viewBox="0 0 24 24" fill="#fff"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg></i><b>15</b>SAMU</div>
        <div class="fnum"><i><svg viewBox="0 0 24 24" fill="#fff"><path d="M12 2s5 4.5 5 10a5 5 0 0 1-10 0c0-2.2 1-3.8 2-5 0 2 1 3 2 3 0-3 1-6 1-8z"/></svg></i><b>18</b>Pompiers</div>
        <div class="fnum"><i><svg viewBox="0 0 24 24" fill="#fff"><g transform="translate(12 12)"><circle r="1.3" cy="-8"/><circle r="1.3" cy="8"/><circle r="1.3" cx="-8"/><circle r="1.3" cx="8"/><circle r="1.3" cx="5.7" cy="-5.7"/><circle r="1.3" cx="-5.7" cy="-5.7"/><circle r="1.3" cx="5.7" cy="5.7"/><circle r="1.3" cx="-5.7" cy="5.7"/></g></svg></i><b>112</b>Urgences UE</div>
        <div class="fnum"><i><svg viewBox="0 0 24 24" fill="#fff"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/></svg></i><b>116 117</b>Médecin de garde</div>
      </div>
    </div>
    <div class="retenir"><strong>À RETENIR</strong>Ce guide et ce kit ne remplacent ni un avis médical ni l'intervention des professionnels de santé. Ils constituent un outil simple de prévention et d'accompagnement, destiné à vous aider à réagir plus efficacement lorsqu'une urgence survient à domicile.</div>
    <!-- A_REMPLACER : e-mail de contact et réseaux sociaux (supprimez une ligne si inutile) -->
    <div class="fcontact">
      <a href="mailto:CONTACT_EMAIL"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>CONTACT_EMAIL</a>
      <a href="LIEN_FACEBOOK" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8z"/></svg>Facebook</a>
      <a href="LIEN_INSTAGRAM" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>Instagram</a>
      <a href="LIEN_LINKEDIN" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 9h4v12H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v2c.6-1.1 2-2.3 4.2-2.3 4 0 4.8 2.6 4.8 6V21h-4v-5.5c0-1.4 0-3.2-2-3.2s-2.3 1.5-2.3 3.1V21h-4z"/></svg>LinkedIn</a>
    </div>
    <div class="edit">
      Guide édité par BioConnect × ♥ Spengler — Matériel médical de confiance<br>
      En cas d'urgence vitale ou de doute sérieux, appelez le 15 ou le 112.
      <div class="legal">© BioConnect – Solutions biomédicales · <!-- A_REMPLACER : pages légales systeme.io --><a href="LIEN_MENTIONS_LEGALES">Mentions légales</a><a href="LIEN_CONFIDENTIALITE">Politique de confidentialité</a><a href="LIEN_CGV">CGV</a></div>
    </div>
  </div></div>
"""

def note(title, lines):
    body = "\n".join("     " + l for l in lines)
    return f"""<!-- =====================================================================
     {title}
     ---------------------------------------------------------------------
{body}
     Section systeme.io en « Pleine largeur », padding 0. Le bloc Code HTML
     n'apparaît pas dans l'aperçu de l'éditeur : vérifiez sur la page publiée.
     ===================================================================== -->
"""

# ================================================================== PAGE 1 : CAPTURE
P1_CSS = r"""<style>
.bcf .cap-hero{background:linear-gradient(120deg,#fff 0%,#fff 40%,var(--cream) 100%);padding:56px 0 40px}
.bcf .cap-hero .grid2{grid-template-columns:1.1fr .9fr;gap:44px}
.bcf .tag{display:inline-block;background:var(--navy);color:#fff;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.bcf .tag span{color:var(--or-l)}
.bcf .cap-hero .h1{margin-bottom:18px}
.bcf .lead{font-size:18px;margin-bottom:24px;max-width:540px}
.bcf .cap-hero .checks li{font-weight:500;color:var(--navy)}
.bcf .visual{position:relative}
.bcf .visual .ph{aspect-ratio:4/3.4;background:linear-gradient(135deg,#fff,#F3EEE9);box-shadow:0 24px 50px -30px rgba(11,35,65,.45)}
.bcf .free{position:absolute;top:-16px;right:-6px;z-index:2;width:112px;height:112px;border-radius:50%;background:var(--or);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:18px;line-height:1.1;transform:rotate(8deg)}
.bcf .free small{font-weight:500;font-size:12px}
.bcf .formhead{background:var(--navy);text-align:center;padding:28px 20px 30px;scroll-margin-top:10px}
.bcf .formhead h2{font-family:var(--f-serif);font-weight:400;font-size:30px;color:#fff;line-height:1.2}
.bcf .formhead p{color:#C9D3E3;margin-top:6px;font-size:15px}
.bcf .formhead .down{display:block;margin:12px auto 0;width:32px;height:32px;color:var(--or-l)}
@container bcf (max-width:700px){
  .cap-hero{padding:32px 0 30px}
  .cap-hero .grid2{grid-template-columns:1fr;gap:24px}
  .visual{order:-1;max-width:300px;margin:0 auto;width:100%}
  .visual .ph{aspect-ratio:4/3}
  .free{width:88px;height:88px;font-size:14px;right:0}
  .lead{font-size:16.5px}
  .formhead h2{font-size:24px}
}
</style>"""

P1A = note("PAGE 1 – CAPTURE · BLOC A (au-dessus du formulaire systeme.io)", [
    "Ordre dans l'éditeur :  [Code HTML : BLOC A]  →  [Formulaire systeme.io]  →  [Code HTML : BLOC B]",
    "Formulaire : champs Prénom + E-mail, case de consentement, bouton",
    "« JE REÇOIS LE GUIDE » (fond #F26B1D, arrondi max), section fond #0B2341.",
    "Action après envoi : rediriger vers la PAGE 2 (merci).",
    "À PERSONNALISER : recherchez « A_REMPLACER ».",
]) + DS + P1_CSS + f"""
<div class="bcf">
{header("Guide pratique")}
  <div class="cap-hero"><div class="wrap"><div class="grid2">
    <div>
      <span class="tag">Guide PDF <span>gratuit</span></span>
      <h1 class="serif h1">Urgence à domicile : sauriez-vous <span class="accent">quoi dire au 15&nbsp;?</span></h1>
      <p class="lead">Recevez le <strong>guide des mesures médicales d'urgence</strong> : comment mesurer les signes vitaux d'un proche et transmettre des informations précises aux secours.</p>
      <ul class="checks">
        <li>Les repères normal / attention / urgence pour la saturation, la tension et la température</li>
        <li>La phrase à transmettre au médecin régulateur pour chaque mesure</li>
        <li>Le protocole d'appel aux secours en 6 étapes</li>
        <li>Les numéros d'urgence : 15, 18, 112, 116 117</li>
      </ul>
    </div>
    <div class="visual">
      <div class="free">GRATUIT<small>format PDF</small></div>
      <div class="ph" data-label="Couverture du guide">
        <!-- A_REMPLACER : URL du visuel / couverture du guide -->
        <img src="IMG_GUIDE" alt="Guide des mesures médicales d'urgence – BioConnect × Spengler" onerror="this.style.display='none'">
      </div>
    </div>
  </div></div></div>
  <div class="formhead" id="formulaire">
    <h2>Où souhaitez-vous recevoir le guide&nbsp;?</h2>
    <p>Indiquez votre prénom et votre adresse e-mail.</p>
    <svg class="down" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 4v15"/><path d="m6 13 6 6 6-6"/></svg>
  </div>
</div>
"""

P1B_CSS = r"""<style>
.bcf .rgpd{background:var(--navy);color:#C9D3E3;text-align:center;font-size:12.5px;line-height:1.55;padding:0 20px 28px}
.bcf .rgpd p{max-width:640px;margin:0 auto}
.bcf .rgpd a{color:#fff}
.bcf .rcard{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:#fff;display:flex;flex-direction:column}
.bcf .rcard .hd{padding:16px 20px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;gap:10px}
.bcf .rcard h3{font-size:17px;color:var(--navy)}
.bcf .prio{font-size:11px;font-weight:700;letter-spacing:.06em;padding:4px 10px;border-radius:999px;background:var(--bad-bg);color:var(--bad);white-space:nowrap}
.bcf .prio.p2{background:#FFF6D6;color:#8A6A00}.bcf .prio.p3{background:var(--ok-bg);color:var(--ok)}
.bcf .lv{display:flex;justify-content:space-between;align-items:center;padding:11px 20px;font-size:14px;gap:12px}
.bcf .lv b{font-family:var(--f-serif);font-weight:400;font-size:18px}
.bcf .lv.ok{background:var(--ok-bg);color:var(--ok)}.bcf .lv.wa{background:var(--warn-bg);color:var(--warn)}.bcf .lv.ba{background:var(--bad-bg);color:var(--bad)}
.bcf .lock{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:18px;text-align:center;font-size:13.5px;color:var(--mut);background:repeating-linear-gradient(45deg,#fafafa,#fafafa 8px,#f4f4f4 8px,#f4f4f4 16px)}
.bcf .lock strong{color:var(--navy)}
.bcf .blur{filter:blur(5px);user-select:none}
.bcf .say{margin:16px 20px 20px;background:var(--navy);color:#fff;border-radius:12px;padding:14px 16px;font-size:13.5px;font-style:italic;flex:1}
.bcf .say small{display:block;font-style:normal;letter-spacing:.14em;text-transform:uppercase;font-size:10px;opacity:.65;margin-bottom:6px}
.bcf .say em{color:var(--or-l);font-weight:600}
.bcf .tabs{margin-top:40px}
.bcf .steps{margin-top:36px}
.bcf .step{display:flex;gap:14px;align-items:center;padding:20px}
.bcf .step .n{font-family:var(--f-serif);font-size:28px;color:var(--or);line-height:1}
.bcf .step h3{margin:0}
.bcf .story .grid2{grid-template-columns:.75fr 1.25fr}
.bcf .story .ph{aspect-ratio:4/4.4;border-radius:6px}
.bcf .story .h2{margin-bottom:18px}
.bcf .story p{margin-bottom:14px}
.bcf .quote{border-left:4px solid var(--or);background:#fff;padding:14px 18px;border-radius:0 12px 12px 0;font-style:italic;font-weight:500;color:var(--navy)}
.bcf .sign{font-size:14px;color:var(--mut)}.bcf .sign strong{color:var(--navy)}
.bcf .final{text-align:center}
.bcf .final .sub{margin:12px 0 26px}
@container bcf (max-width:700px){.story .grid2{grid-template-columns:1fr}.story .ph{max-width:320px}}
</style>"""

STORY = """      <p>Une nuit, mon beau-père respirait très difficilement. Grâce à un oxymètre, j'ai constaté une saturation en oxygène anormalement basse et j'ai pu transmettre cette information au médecin régulateur, qui a immédiatement envoyé les pompiers avec de l'oxygène.</p>
      <p class="quote">« Je suis convaincu que cette information a contribué à lui sauver la vie. »</p>"""

FOUNDER_IMG = """<div class="ph cover" data-label="Photo du fondateur">
      <!-- A_REMPLACER : URL du portrait -->
      <img src="IMG_FONDATEUR" alt="José Rodriguez, Directeur Général de BioConnect" onerror="this.style.display='none'">
    </div>"""

P1B = note("PAGE 1 – CAPTURE · BLOC B (en dessous du formulaire systeme.io)", [
    "À PERSONNALISER : recherchez « A_REMPLACER ».",
]) + DS + P1B_CSS + f"""
<div class="bcf">
  <div class="rgpd"><p>En validant ce formulaire, vous acceptez que BioConnect utilise votre prénom et votre e-mail pour vous envoyer le guide puis des informations sur ses produits. Désinscription possible à tout moment via le lien présent dans chaque e-mail. <a href="LIEN_CONFIDENTIALITE">Politique de confidentialité</a>.</p></div>

  <div class="sec"><div class="wrap">
    <div class="center">
      <span class="kicker">Aperçu du guide</span>
      <h2 class="serif h2">Lire les chiffres <span class="accent">et savoir quoi dire</span></h2>
      <p class="sub">Pour chaque mesure : des repères et la phrase à transmettre au régulateur.</p>
    </div>
    <div class="grid3 tabs">
      <div class="rcard">
        <div class="hd"><h3>Saturation (SpO₂)</h3><span class="prio">PRIORITÉ 1</span></div>
        <div class="lv ok"><span>Normal</span><b>95 – 100 %</b></div>
        <div class="lv wa"><span>Attention</span><b>90 – 94 %</b></div>
        <div class="lv ba"><span>Urgence → 15</span><b>&lt; 90 %</b></div>
        <div class="say"><small>Ce que vous dites au régulateur</small>« L'oxymètre indique une saturation en oxygène de <em>[chiffre] %</em>. La fréquence cardiaque affichée est de <em>[chiffre] battements par minute</em>. »</div>
      </div>
      <div class="rcard">
        <div class="hd"><h3>Tension artérielle</h3><span class="prio p2">PRIORITÉ 2</span></div>
        <div class="lv ok"><span>Normal</span><b class="blur">90–140 / 60–90</b></div>
        <div class="lv wa"><span>Élevée</span><b class="blur">&gt; 140 / 90</b></div>
        <div class="lv ba"><span>Urgence → 15</span><b class="blur">&gt; 180 / 110</b></div>
        <div class="lock"><strong>Repères complets et phrase type</strong>dans le guide</div>
      </div>
      <div class="rcard">
        <div class="hd"><h3>Température</h3><span class="prio p3">PRIORITÉ 3</span></div>
        <div class="lv ok"><span>Normal</span><b class="blur">36,1 – 37,2 °C</b></div>
        <div class="lv wa"><span>Fièvre</span><b class="blur">37,5 – 39,9 °C</b></div>
        <div class="lv ba"><span>Urgence → 15</span><b class="blur">≥ 40 °C</b></div>
        <div class="lock"><strong>Repères complets et phrase type</strong>dans le guide</div>
      </div>
    </div>
  </div></div>

  <div class="sec bg-lav"><div class="wrap">
    <div class="center">
      <span class="kicker">Inclus dans le guide</span>
      <h2 class="serif h2">Les 6 étapes d'un <span class="accent">appel efficace</span></h2>
      <p class="sub">Les bonnes informations, dans le bon ordre, pour aider le régulateur à décider.</p>
    </div>
    <div class="grid3 steps">
      <div class="card step"><span class="n">01</span><h3>Votre identité</h3></div>
      <div class="card step"><span class="n">02</span><h3>L'adresse exacte</h3></div>
      <div class="card step"><span class="n">03</span><h3>Le problème</h3></div>
      <div class="card step"><span class="n">04</span><h3>Les mesures</h3></div>
      <div class="card step"><span class="n">05</span><h3>Les antécédents</h3></div>
      <div class="card step"><span class="n">06</span><h3>Ne raccrochez pas</h3></div>
    </div>
  </div></div>

  <div class="sec bg-cream story"><div class="wrap"><div class="grid2">
    {FOUNDER_IMG}
    <div>
      <span class="kicker">Pourquoi ce guide</span>
      <h2 class="serif h2">Quelques chiffres peuvent <span class="accent">faire la différence</span></h2>
{STORY}
      <p style="margin-top:14px">Ce guide vous aide à utiliser l'oxymètre, le tensiomètre et le thermomètre, et à transmettre rapidement des données précises aux secours.</p>
      <p class="sign"><strong>José Rodriguez</strong> – Directeur Général, BioConnect</p>
    </div>
  </div></div></div>

  <div class="sec final"><div class="wrap">
    <h2 class="serif h2">Préparez-vous <span class="accent">avant</span> l'urgence</h2>
    <p class="sub muted">Le guide est envoyé gratuitement par e-mail.</p>
    <a class="btn" href="#formulaire">Je reçois le guide {ARROW}</a>
  </div></div>
{FOOTER}</div>
"""

# ================================================================== PAGE 2 : MERCI
P2_CSS = r"""<style>
.bcf .ty-hero{background:linear-gradient(180deg,var(--cream),#fff);padding:60px 0 40px;text-align:center}
.bcf .ty-ok{width:76px;height:76px;border-radius:50%;background:var(--ok);color:#fff;display:flex;align-items:center;justify-content:center;margin:0 auto 22px;box-shadow:0 12px 26px -12px rgba(30,142,78,.7)}
.bcf .ty-ok svg{width:38px;height:38px}
.bcf .ty-hero .h1{margin-bottom:14px}
.bcf .ty-hero .lead{font-size:18px;color:var(--mut);max-width:600px;margin:0 auto 28px}
.bcf .ty-steps{margin-top:8px}
.bcf .ty-steps .card{text-align:center}
.bcf .ty-steps .n{width:40px;height:40px;border-radius:50%;background:var(--navy);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;margin:0 auto 12px}
.bcf .bridge .ph{aspect-ratio:1/0.85}
.bcf .bridge .h2{margin-bottom:16px}
.bcf .bridge p{margin-bottom:18px}
.bcf .mini{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 26px}
.bcf .mini li{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:14px;color:var(--navy);font-weight:600}
.bcf .mini li span{display:block;font-weight:400;color:var(--mut);font-size:12.5px}
@container bcf (max-width:700px){.ty-hero{padding:40px 0 30px}.ty-hero .lead{font-size:16.5px}.mini{grid-template-columns:1fr}}
</style>"""

P2 = note("PAGE 2 – MERCI (un seul bloc Code HTML)", [
    "Page vers laquelle redirige le formulaire de la page 1.",
    "À PERSONNALISER : LIEN_DRIVE_PDF (lien de partage Drive du guide, accès « Tous",
    "les utilisateurs disposant du lien »), LIEN_PAGE_3, IMG_KIT_COMPLET, e-mail expéditeur.",
]) + DS + P2_CSS + f"""
<div class="bcf">
{header("Guide pratique")}
  <div class="ty-hero"><div class="wrap">
    <div class="ty-ok"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></div>
    <h1 class="serif h1">Merci, votre guide <span class="accent">est en route</span></h1>
    <p class="lead">Vous allez recevoir le guide des mesures médicales d'urgence par e-mail dans quelques minutes. Vous pouvez aussi le télécharger dès maintenant.</p>
    <!-- A_REMPLACER : lien de partage Google Drive du PDF -->
    <a class="btn" href="LIEN_DRIVE_PDF" target="_blank" rel="noopener">Télécharger le guide (PDF) {ARROW}</a>
  </div></div>

  <div class="sec" style="padding-top:20px"><div class="wrap">
    <div class="grid3 ty-steps">
      <div class="card"><div class="n">1</div><h3>Ouvrez votre messagerie</h3><p>Cherchez l'e-mail envoyé par BioConnect <!-- A_REMPLACER : adresse d'expédition -->(EXPEDITEUR_EMAIL).</p></div>
      <div class="card"><div class="n">2</div><h3>Rien reçu ?</h3><p>Vérifiez les dossiers « Spam » ou « Promotions » et ajoutez l'adresse à vos contacts.</p></div>
      <div class="card"><div class="n">3</div><h3>Gardez-le accessible</h3><p>Enregistrez le PDF sur votre téléphone ou imprimez-le et rangez-le près de vos appareils de mesure.</p></div>
    </div>
  </div></div>

  <div class="sec bg-cream bridge"><div class="wrap"><div class="grid2">
    <div class="ph" data-label="Photo du kit complet">
      <!-- A_REMPLACER : URL de la photo du kit -->
      <img src="IMG_KIT_COMPLET" alt="Kit urgence domicile Spengler" onerror="this.style.display='none'">
    </div>
    <div>
      <span class="kicker">Étape suivante</span>
      <h2 class="serif h2">Le guide explique comment mesurer. <span class="accent">Le kit contient les appareils.</span></h2>
      <p>Pour appliquer le guide, il faut un oxymètre, un tensiomètre et un thermomètre fiables, réunis au même endroit. Nous avons rassemblé ces appareils Spengler dans une trousse unique.</p>
      <ul class="mini">
        <li>Tensiomètre<span>AutoTensio®</span></li>
        <li>Oxymètre de pouls<span>OxyStart®</span></li>
        <li>Thermomètre infrarouge<span>Tempo Easy</span></li>
        <li>Trousse de transport<span>Spengler</span></li>
      </ul>
      <!-- A_REMPLACER : URL de la page 3 (vente) -->
      <a class="btn" href="LIEN_PAGE_3">Découvrir le kit urgence {ARROW}</a>
    </div>
  </div></div></div>
{FOOTER}</div>
"""

# ================================================================== PAGE 3 : VENTE
P3_CSS = r"""<style>
.bcf .s-hero{background:linear-gradient(120deg,#fff 0%,#fff 45%,var(--cream) 100%);padding:60px 0 52px}
.bcf .s-hero .grid2{grid-template-columns:1.05fr 1fr;gap:40px}
.bcf .s-hero .h1{margin-bottom:20px}
.bcf .s-hero .lead{font-size:18px;max-width:520px;margin-bottom:28px}
.bcf .s-hero .ph{aspect-ratio:1/0.9}
.bcf .badge{position:absolute;top:-10px;right:0;z-index:2;width:140px;height:140px;border-radius:50%;background:#FBDCC4;display:flex;align-items:center;justify-content:center;text-align:center;font-size:14px;line-height:1.25;color:var(--navy);font-weight:600;padding:16px;transform:rotate(-6deg)}
.bcf .perks{background:var(--cream);padding:30px 0}
.bcf .perk{display:flex;gap:14px}
.bcf .perk svg{flex:0 0 38px;height:38px;color:var(--or)}
.bcf .perk h3{font-size:14px;font-weight:700;text-transform:uppercase;color:var(--navy);line-height:1.25;margin-bottom:4px}
.bcf .perk p{font-size:13px;color:var(--mut);line-height:1.45}
.bcf .story .grid2{grid-template-columns:.85fr 1.15fr}
.bcf .story .ph{aspect-ratio:4/4.3;border-radius:6px}
.bcf .story .h2{margin-bottom:20px}
.bcf .story p{margin-bottom:14px}
.bcf .quote{border-left:4px solid var(--or);background:var(--cream);padding:14px 18px;border-radius:0 12px 12px 0;font-style:italic;font-weight:500;color:var(--navy)}
.bcf .hl{color:var(--or);font-weight:600}
.bcf .sign{font-size:14px;color:var(--mut)}.bcf .sign strong{color:var(--navy)}
.bcf .kit .grid4{margin-top:40px}
.bcf .kit .card .ph{aspect-ratio:1/1;margin-bottom:16px;border-radius:12px}
.bcf .kit .card h3{display:flex;align-items:center;gap:8px;font-size:14px;text-transform:uppercase}
.bcf .model{display:inline-block;margin-top:10px;font-size:12px;font-weight:600;color:var(--or);background:var(--cream);padding:3px 10px;border-radius:999px}
.bcf .rcard{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:#fff;display:flex;flex-direction:column}
.bcf .rcard .hd{padding:16px 20px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;gap:10px}
.bcf .rcard h3{font-size:17px;color:var(--navy)}
.bcf .prio{font-size:11px;font-weight:700;letter-spacing:.06em;padding:4px 10px;border-radius:999px;background:var(--bad-bg);color:var(--bad);white-space:nowrap}
.bcf .prio.p2{background:#FFF6D6;color:#8A6A00}.bcf .prio.p3{background:var(--ok-bg);color:var(--ok)}
.bcf .lv{display:flex;justify-content:space-between;align-items:center;padding:11px 20px;font-size:14px;gap:12px}
.bcf .lv b{font-family:var(--f-serif);font-weight:400;font-size:18px;text-align:right}
.bcf .lv.ok{background:var(--ok-bg);color:var(--ok)}.bcf .lv.wa{background:var(--warn-bg);color:var(--warn)}.bcf .lv.ba{background:var(--bad-bg);color:var(--bad)}
.bcf .ref .grid3{margin-top:40px}
.bcf .note{font-size:12.5px;color:var(--mut);text-align:center;margin-top:20px}
.bcf .offer{background:var(--navy)}
.bcf .offer .h2{color:#fff}
.bcf .offer .kicker{color:var(--or-l)}
.bcf .offer .ph{aspect-ratio:1/1;background:linear-gradient(135deg,#17345C,#0F2B4F);color:#8aa0bf}
.bcf .box{background:#fff;border-radius:22px;padding:32px;margin-top:24px}
.bcf .box ul{list-style:none;margin-bottom:20px}
.bcf .box li{padding:9px 0;border-bottom:1px dashed var(--line);display:flex;justify-content:space-between;gap:12px;font-size:15px}
.bcf .box li span:last-child{color:var(--ok);font-weight:600;white-space:nowrap}
.bcf .price{display:flex;align-items:baseline;gap:14px;margin-bottom:4px}
.bcf .price .now{font-family:var(--f-serif);font-size:50px;color:var(--navy);line-height:1}
.bcf .price .old{text-decoration:line-through;color:var(--mut);font-size:20px}
.bcf .box .btn{width:100%;margin-top:18px}
.bcf .trust{display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:center;margin-top:14px;font-size:13px;color:var(--mut)}
.bcf .faq .wrap{max-width:820px}
.bcf .faq details{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:#fff}
.bcf .faq summary{cursor:pointer;list-style:none;padding:18px 22px;font-weight:600;color:var(--navy);display:flex;justify-content:space-between;gap:16px}
.bcf .faq summary::-webkit-details-marker{display:none}
.bcf .faq summary::after{content:"+";color:var(--or);font-size:22px;line-height:1;transition:transform .2s}
.bcf .faq details[open] summary::after{transform:rotate(45deg)}
.bcf .faq details p{padding:0 22px 20px;color:var(--mut)}
.bcf .faq .center{margin-bottom:34px}
.bcf .final .h2{margin-bottom:18px}
.bcf .final p{margin-bottom:26px}
.bcf .final .ph{aspect-ratio:4/3.4}
@container bcf (max-width:700px){
  .s-hero{padding:34px 0}
  .s-hero .grid2,.story .grid2{grid-template-columns:1fr}
  .s-hero .lead{font-size:16.5px}
  .badge{width:104px;height:104px;font-size:11.5px}
  .story .ph{max-width:340px}
  .perks .grid4{grid-template-columns:1fr 1fr;gap:18px}
  .kit .grid4{grid-template-columns:1fr 1fr;gap:12px}
  .kit .card{padding:14px}
  .box{padding:22px}
  .price .now{font-size:40px}
}
</style>"""

# barre mobile : HORS du conteneur .bcf (container-type casserait position:fixed)
STICKY = f"""<style>
.bcf-sticky{{display:none}}
@media (max-width:700px){{
  .bcf-sticky{{display:block;position:fixed;left:0;right:0;bottom:0;z-index:19;background:#fff;border-top:1px solid #ECE6E0;padding:10px 16px;box-shadow:0 -8px 20px -12px rgba(0,0,0,.25)}}
  .bcf-sticky a{{display:block;text-align:center;background:#F26B1D;color:#fff!important;text-decoration:none;font:700 15px/1 'Inter',Arial,sans-serif;letter-spacing:.03em;text-transform:uppercase;padding:16px;border-radius:999px}}
  .bcf .foot{{padding-bottom:96px}}
}}
</style>
<div class="bcf-sticky"><a href="#offre">Commander le kit</a></div>
"""

def kcard(img, alt, label, icon, title, text, model):
    return f"""      <div class="card">
        <div class="ph" data-label="{label}"><img src="{img}" alt="{alt}" onerror="this.style.display='none'"></div>
        <h3>{icon}{title}</h3>
        <p>{text}</p>
        <span class="model">{model}</span>
      </div>"""

ICO = lambda d: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F26B1D" stroke-width="1.8">{d}</svg>'

P3 = note("PAGE 3 – VENTE (un seul bloc Code HTML)", [
    "À PERSONNALISER : LIEN_COMMANDE (page de commande systeme.io), prix,",
    "IMG_xxx (URL des photos), e-mail et réseaux sociaux dans le pied de page.",
]) + DS + P3_CSS + f"""
<div class="bcf">
{header("Commander", "#offre")}
  <div class="s-hero"><div class="wrap"><div class="grid2">
    <div>
      <span class="kicker">Kit urgence domicile</span>
      <h1 class="serif h1">Et si une urgence survenait <span class="accent">chez vous&nbsp;?</span></h1>
      <p class="lead">Mesurez les signes vitaux essentiels et transmettez-les aux services de secours pour une prise en charge plus rapide et adaptée.</p>
      <a class="btn" href="#offre">Découvrir l'offre {ARROW}</a>
    </div>
    <div style="position:relative">
      <div class="badge">Kit complet en une seule trousse</div>
      <div class="ph" data-label="Photo du kit complet">
        <!-- A_REMPLACER : URL de la photo du kit -->
        <img src="IMG_KIT_COMPLET" alt="Kit Spengler : trousse, tensiomètre, oxymètre et thermomètre" onerror="this.style.display='none'">
      </div>
    </div>
  </div></div></div>

  <div class="perks"><div class="wrap"><div class="grid4">
    <div class="perk"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></svg><div><h3>Simple d'utilisation</h3><p>Appareils conçus pour un usage à domicile</p></div></div>
    <div class="perk"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 4 6v6c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V6l-8-3z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg><div><h3>Mesures essentielles</h3><p>Tension, saturation, pouls, température</p></div></div>
    <div class="perk"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 11 12 3l9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/></svg><div><h3>À la maison</h3><p>Et en déplacement grâce à la trousse</p></div></div>
    <div class="perk"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><path d="M15.5 14.2c3.2-.4 6 1.5 6 4.8"/></svg><div><h3>Toute la famille</h3><p>Adultes, enfants et seniors</p></div></div>
  </div></div></div>

  <div class="sec story"><div class="wrap"><div class="grid2">
    {FOUNDER_IMG}
    <div>
      <span class="kicker">Notre histoire</span>
      <h2 class="serif h2">Pourquoi avons-nous créé <span class="accent">ce kit&nbsp;?</span></h2>
{STORY}
      <p style="margin-top:14px">Cette expérience nous a montré l'intérêt d'avoir à domicile un matériel simple et fiable pour donner des informations précises aux urgentistes.</p>
      <p class="hl">C'est de là qu'est née l'idée de ce kit, en partenariat avec Spengler, marque spécialisée dans le matériel de diagnostic médical.</p>
      <p class="sign"><strong>José Rodriguez</strong> – Directeur Général, BioConnect</p>
    </div>
  </div></div></div>

  <div class="sec bg-lav kit"><div class="wrap">
    <div class="center">
      <span class="kicker">Contenu du kit</span>
      <h2 class="serif h2">Les appareils pour mesurer <span class="accent">les signes vitaux essentiels</span></h2>
    </div>
    <div class="grid4">
{kcard("IMG_TENSIOMETRE","Tensiomètre électronique Spengler","Photo tensiomètre",ICO('<path d="M20.8 8.6a5 5 0 0 0-8.8-3.2 5 5 0 0 0-8.8 3.2C3.2 14 12 20 12 20s8.8-6 8.8-11.4z"/>'),"Tension artérielle","Pression systolique, diastolique et pouls.","AutoTensio®")}
{kcard("IMG_OXYMETRE","Oxymètre de pouls Spengler","Photo oxymètre",ICO('<rect x="5" y="7" width="14" height="10" rx="4"/><path d="M9 12h6"/>'),"Saturation en oxygène","Taux d'oxygène dans le sang (SpO₂) et rythme cardiaque.","OxyStart®")}
{kcard("IMG_THERMOMETRE","Thermomètre infrarouge Spengler","Photo thermomètre",ICO('<path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z"/>'),"Température","Mesure frontale sans contact.","Tempo Easy")}
{kcard("IMG_TROUSSE","Trousse de transport Spengler","Photo trousse",ICO('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2"/>'),"Trousse","Tout le matériel rangé au même endroit.","Incluse")}
    </div>
  </div></div>

  <div class="sec ref"><div class="wrap">
    <div class="center">
      <span class="kicker">Guide inclus</span>
      <h2 class="serif h2">Des repères pour <span class="accent">interpréter chaque mesure</span></h2>
      <p class="sub">Le guide fourni avec le kit indique, pour chaque appareil, les valeurs de référence et les informations à transmettre au 15.</p>
    </div>
    <div class="grid3">
      <div class="rcard"><div class="hd"><h3>Saturation (SpO₂)</h3><span class="prio">PRIORITÉ 1</span></div>
        <div class="lv ok"><span>Normal</span><b>95 – 100 %</b></div><div class="lv wa"><span>Attention</span><b>90 – 94 %</b></div><div class="lv ba"><span>Urgence → 15</span><b>&lt; 90 %</b></div></div>
      <div class="rcard"><div class="hd"><h3>Tension artérielle</h3><span class="prio p2">PRIORITÉ 2</span></div>
        <div class="lv ok"><span>Normal</span><b>90–140 / 60–90</b></div><div class="lv wa"><span>Élevée</span><b>&gt; 140 / 90</b></div><div class="lv ba"><span>Urgence → 15</span><b>&gt; 180/110 ou &lt; 80/50</b></div></div>
      <div class="rcard"><div class="hd"><h3>Température</h3><span class="prio p3">PRIORITÉ 3</span></div>
        <div class="lv ok"><span>Normal</span><b>36,1 – 37,2 °C</b></div><div class="lv wa"><span>Fièvre</span><b>37,5 – 39,9 °C</b></div><div class="lv ba"><span>Urgence → 15</span><b>≥ 40 °C ou &lt; 35 °C</b></div></div>
    </div>
    <p class="note">Repères indicatifs issus du guide. Ils ne remplacent pas un avis médical : en cas de doute, appelez le 15.</p>
  </div></div>

  <div class="sec offer" id="offre"><div class="wrap"><div class="grid2">
    <div class="ph" data-label="Photo du kit (packshot)">
      <img src="IMG_KIT_COMPLET" alt="Kit urgence domicile BioConnect × Spengler" onerror="this.style.display='none'">
    </div>
    <div>
      <span class="kicker">Kit urgence domicile</span>
      <h2 class="serif h2">Ce que vous recevez</h2>
      <div class="box">
        <ul>
          <li><span>Tensiomètre électronique AutoTensio®</span><span>Inclus</span></li>
          <li><span>Oxymètre de pouls OxyStart®</span><span>Inclus</span></li>
          <li><span>Thermomètre infrarouge Tempo Easy</span><span>Inclus</span></li>
          <li><span>Trousse de transport Spengler</span><span>Incluse</span></li>
          <li><span>Guide des mesures médicales d'urgence (PDF)</span><span>Inclus</span></li>
        </ul>
        <!-- A_REMPLACER : prix (supprimez <span class="old"> s'il n'y a pas de prix barré) -->
        <div class="price"><span class="now">XX,XX €</span><span class="old">XX,XX €</span></div>
        <small class="muted">Prix TTC · livraison à domicile <!-- A_REMPLACER : délais / frais de port --></small>
        <!-- A_REMPLACER : URL de la page de commande systeme.io -->
        <a class="btn" href="LIEN_COMMANDE">Commander le kit {ARROW}</a>
        <div class="trust"><span>Paiement sécurisé</span><span>·</span><span>Questions : CONTACT_EMAIL</span></div>
      </div>
    </div>
  </div></div></div>

  <div class="sec faq"><div class="wrap">
    <div class="center"><span class="kicker">Vos questions</span><h2 class="serif h2">Questions fréquentes</h2></div>
    <details><summary>Faut-il des connaissances médicales pour utiliser le kit&nbsp;?</summary><p>Non. Les appareils sont conçus pour un usage à domicile, et le guide explique chaque écran et comment lire les résultats (normal / attention / urgence).</p></details>
    <details><summary>Le kit remplace-t-il un médecin ou un appel aux secours&nbsp;?</summary><p>Non. Le kit et le guide ne remplacent ni un avis médical ni l'intervention des professionnels de santé. Ils aident à transmettre des informations précises. En cas d'urgence vitale ou de doute sérieux, appelez le 15 ou le 112.</p></details>
    <details><summary>Le kit convient-il aux enfants&nbsp;?</summary><p>Il s'adresse à toute la famille. Pour la saturation chez l'enfant, le guide recommande une sonde pédiatrique adaptée à la taille des doigts.</p></details>
    <details><summary>Comment obtenir une mesure fiable&nbsp;?</summary><p>Oxymètre : doigt propre et chaud, attendre 30 secondes. Tension : personne assise au calme depuis 5 minutes, bras à hauteur du cœur, 2 mesures à 2 minutes d'intervalle. Thermomètre frontal : à 3 cm du milieu du front.</p></details>
    <details><summary>Quels sont les délais de livraison&nbsp;?</summary><p><!-- A_REMPLACER -->Indiquez ici vos délais et frais de livraison.</p></details>
    <details><summary>Comment vous contacter&nbsp;?</summary><p>Par e-mail à CONTACT_EMAIL.</p></details>
  </div></div>

  <div class="sec bg-cream final"><div class="wrap"><div class="grid2">
    <div>
      <span class="kicker">Pour les familles</span>
      <h2 class="serif h2">Être mieux préparé, <span class="accent">à la maison comme en déplacement</span></h2>
      <p>Le kit vous permet de réagir plus sereinement et de disposer des informations essentielles à transmettre aux secours.</p>
      <a class="btn" href="#offre">Commander le kit {ARROW}</a>
    </div>
    <div class="ph cover" data-label="Photo famille / mise en situation">
      <!-- A_REMPLACER : URL d'une photo de mise en situation -->
      <img src="IMG_FAMILLE" alt="Famille à la maison" onerror="this.style.display='none'">
    </div>
  </div></div></div>
{FOOTER}</div>
""" + STICKY


import re as _re
def scope_cq(html):
    """Préfixe .bcf aux sélecteurs des @container (sinon les règles de base, plus spécifiques, l'emportent)."""
    out, i = [], 0
    for m in _re.finditer(r'@container bcf \([^)]*\)\{', html):
        if m.start() < i: continue
        out.append(html[i:m.end()]); j = m.end(); depth = 1; k = j
        while depth:
            if html[k] == '{': depth += 1
            elif html[k] == '}': depth -= 1
            k += 1
        body = html[j:k-1]
        body = _re.sub(r'(^|\})\s*([^{}]+)\{', lambda mm: mm.group(1) + ','.join(
            (x.strip() if x.strip().startswith('.bcf') else '.bcf ' + x.strip()) for x in mm.group(2).split(',')) + '{', body)
        out.append(body + '}'); i = k
    out.append(html[i:]); return ''.join(out)

FILES = {
    "1-capture-bloc-A.html": P1A,
    "1-capture-bloc-B.html": P1B,
    "2-merci.html": P2,
    "3-vente.html": P3,
}
FILES = {k: scope_cq(v) for k, v in FILES.items()}
P1A, P1B, P2, P3 = (FILES[k] for k in FILES)
for name, html in FILES.items():
    assert "<!DOCTYPE" not in html and "<html" not in html and "<body" not in html and "<head" not in html
    open(OUT + name, "w", encoding="utf-8").write(html)

# ---------------------------------------------------------------- aperçus locaux
HOST = '<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><body style="margin:0;font-family:Arial;color:red"><style>h1,h2,h3{font-family:Arial;text-align:center}p{text-align:center}</style>'
MOCK = """<div style="background:#0B2341;padding:0 20px 18px"><div style="max-width:440px;margin:0 auto;display:grid;gap:10px;font-family:Arial">
<input placeholder="Prénom" style="padding:15px;border-radius:10px;border:0;font-size:16px"><input placeholder="E-mail" style="padding:15px;border-radius:10px;border:0;font-size:16px">
<label style="color:#C9D3E3;font-size:13px"><input type=checkbox> J'accepte de recevoir le guide et les e-mails de BioConnect</label>
<button style="padding:17px;border:0;border-radius:999px;background:#F26B1D;color:#fff;font-weight:700;font-size:16px">JE REÇOIS LE GUIDE</button>
<small style="color:#8fa0bb;text-align:center">[ formulaire systeme.io simulé ]</small></div></div>"""
open(PREV + "p1.html", "w", encoding="utf-8").write(HOST + P1A + MOCK + P1B)
open(PREV + "p2.html", "w", encoding="utf-8").write(HOST + P2)
open(PREV + "p3.html", "w", encoding="utf-8").write(HOST + P3)
# bloc étroit dans une page large : vérifie les container queries
open(PREV + "p3-narrow.html", "w", encoding="utf-8").write(HOST + '<div style="width:620px;margin:0 auto;border:1px dashed #999">' + P3 + "</div>")
for n, h in FILES.items():
    print(n, len(h.encode()), "octets")
