/* motion-kit.js : briques d'animation déterministes pour HyperFrames + GSAP.
   Règle d'or : les états de départ se posent avec gsap.set au montage, les animations avec tl.to à un instant donné.
   Pas de fromTo (piège immediateRender), pas de Math.random, pas de timer. Tout est fonction du temps.
   Usage : const tl = gsap.timeline({ paused: true }); … MK.done(tl, DUREE); */
(function () {
  const MK = {};
  const $ = (s) => (typeof s === "string" ? document.querySelector(s) : s);
  const $$ = (s) => (typeof s === "string" ? [...document.querySelectorAll(s)] : Array.isArray(s) ? s.flatMap((x) => $$(x)) : [s]);
  MK.$ = $; MK.$$ = $$;

  /* ---------- ressorts et hasard déterministe ---------- */
  MK.spring = (z, w) => { const wd = w * Math.sqrt(1 - z * z); return (t) => (t >= 1 ? 1 : 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + ((z * w) / wd) * Math.sin(wd * t))); };
  MK.ease = { ui: MK.spring(0.42, 20), card: MK.spring(0.55, 14), type: MK.spring(0.8, 12) }; // nerveux, moyen, lourd
  MK.rng = (seed = 7) => () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

  /* ---------- montage ---------- */
  MK.el = (tag, cls, parent, html = "", style = {}) => { const e = document.createElement(tag); if (cls) e.className = cls; e.innerHTML = html; Object.assign(e.style, style); if (parent) $(parent).appendChild(e); return e; };
  // personnage-bulle en verre : (x, y) = centre de la tête, s = échelle
  MK.person = (parent, x, y, s = 1, { eyes = true } = {}) => MK.el("div", "per", parent, `<div class="bo"></div><div class="hd">${eyes ? '<i class="l"></i><i class="r"></i>' : ""}</div>`, { left: x + "px", top: y + "px", transform: `scale(${s})` });
  // découpe un texte en lettres .ch (garde les espaces)
  MK.split = (sel) => { const e = $(sel); const t = e.textContent; e.innerHTML = t.split("").map((c) => `<span class="ch">${c === " " ? "&nbsp;" : c}</span>`).join(""); return [...e.querySelectorAll(".ch")]; };
  // fond « fluide » : taches floues qui dérivent (couleurs = liste CSS)
  MK.fluid = (parent, colors, seed = 3) => { const r = MK.rng(seed); const box = MK.el("div", "fluid", parent); return colors.map((c, i) => MK.el("b", "", box, "", { left: r() * 90 + "%", top: r() * 90 + "%", width: 500 + r() * 600 + "px", height: 500 + r() * 600 + "px", background: c, marginLeft: "-300px", marginTop: "-300px" })); };

  /* ---------- scènes et sous-titres ---------- */
  // scenes : [[sélecteur, début, fin], …] → visibilité nette (opacity 0/1)
  MK.scenes = (tl, list, total) => { list.forEach(([s]) => gsap.set(s, { opacity: 0 })); list.forEach(([s, a, b]) => { tl.set(s, { opacity: 1 }, a); if (b < total) tl.set(s, { opacity: 0 }, b); }); };
  // chunks : [[t, "texte", couleur?], …] ; un texte vide efface
  MK.captions = (tl, sel, chunks) => { gsap.set(sel, { opacity: 0 }); chunks.forEach(([t, txt, col]) => { tl.set(sel, { textContent: txt, ...(col ? { color: col } : {}) }, t); if (txt) { tl.set(sel, { y: 14, opacity: 0 }, t); tl.to(sel, { y: 0, opacity: 1, duration: 0.25, ease: "power2.out" }, t); } else tl.set(sel, { opacity: 0 }, t); }); };

  /* ---------- entrées et sorties ---------- */
  // le masque .m prend la taille de police de son texte pour que sa marge (en em) laisse passer les accents des capitales
  MK.fitMask = (sel) => $$(sel).forEach((e) => { const m = e.parentElement; if (m && m.classList.contains("m") && !m.style.fontSize) m.style.fontSize = getComputedStyle(e).fontSize; });
  MK.rise = (tl, sel, t, { dur = 0.75, stagger = 0, ease = MK.ease.type, from = 115 } = {}) => { MK.fitMask(sel); gsap.set(sel, { yPercent: from }); tl.to(sel, { yPercent: 0, duration: dur, ease, stagger }, t); };
  MK.exitUp = (tl, sel, t, { dur = 0.35, stagger = 0.04 } = {}) => tl.to(sel, { yPercent: -120, opacity: 0, duration: dur, ease: "power3.in", stagger }, t);
  MK.pop = (tl, sel, t, { dur = 0.6, stagger = 0, from = 0 } = {}) => { gsap.set(sel, { scale: from, opacity: 0 }); tl.to(sel, { scale: 1, opacity: 1, duration: dur, ease: MK.ease.ui, stagger }, t); };
  MK.slide = (tl, sel, t, { x = 0, y = 0, dur = 0.8, ease = MK.ease.card, stagger = 0 } = {}) => { gsap.set(sel, { x, y }); tl.to(sel, { x: 0, y: 0, duration: dur, ease, stagger }, t); };
  MK.fadeIn = (tl, sel, t, dur = 0.3) => { gsap.set(sel, { opacity: 0 }); tl.to(sel, { opacity: 1, duration: dur }, t); };
  MK.stamp = (tl, sel, t) => { gsap.set(sel, { scale: 2.2, rotation: -10, opacity: 0 }); tl.to(sel, { scale: 1, rotation: 0, opacity: 1, duration: 0.6, ease: MK.ease.ui }, t); };
  MK.shake = (tl, sel, t, amp = 12) => tl.to(sel, { keyframes: [{ x: -amp, y: amp * 0.6 }, { x: amp * 0.8, y: -amp * 0.7 }, { x: -amp * 0.4, y: amp * 0.4 }, { x: 0, y: 0 }], duration: 0.28, ease: "none" }, t);
  MK.pulse = (tl, sel, times, k = 1.06) => times.forEach((t) => { tl.to(sel, { scale: k, duration: 0.08, ease: "power2.out" }, t); tl.to(sel, { scale: 1, duration: 0.4, ease: MK.ease.ui }, t + 0.08); });

  /* ---------- texte vivant ---------- */
  // frappe au clavier : écrit `text` lettre par lettre dans sel, curseur clignotant optionnel (.caret)
  MK.type = (tl, sel, text, t, { cps = 16 } = {}) => { const e = $(sel); e.textContent = ""; const o = { n: 0 }; tl.to(o, { n: text.length, duration: text.length / cps, ease: "none", onUpdate: () => { e.textContent = text.slice(0, Math.round(o.n)); } }, t); };
  // compteur : de `from` à `to`, format(v) → texte
  MK.count = (tl, sel, from, to, t, dur, fmt = (v) => Math.round(v).toLocaleString("fr-FR")) => { const e = $(sel); const o = { v: from }; e.textContent = fmt(from); tl.to(o, { v: to, duration: dur, ease: "power2.out", onUpdate: () => { e.textContent = fmt(o.v); } }, t); };
  // défilement horizontal continu (marquee)
  MK.marquee = (tl, sel, t, dur, dx) => tl.to(sel, { x: dx, duration: dur, ease: "none" }, t);

  /* ---------- tracés ---------- */
  // (opacity 0 avant le départ : sinon un bout arrondi laisse un point visible)
  MK.draw = (tl, path, t, dur = 1, ease = "power2.inOut") => { const p = $(path), L = p.getTotalLength(); gsap.set(p, { strokeDasharray: L, strokeDashoffset: L, opacity: 0 }); tl.set(p, { opacity: 1 }, t); tl.to(p, { strokeDashoffset: 0, duration: dur, ease }, t); };
  // fait suivre un tracé SVG à un élément (dx, dy = position du SVG dans son parent)
  MK.follow = (tl, sel, path, t, dur = 1, { dx = 0, dy = 0, ease = "power2.inOut" } = {}) => { const p = $(path), o = { k: 0 }; tl.to(o, { k: 1, duration: dur, ease, onUpdate: () => { const q = p.getPointAtLength(p.getTotalLength() * o.k); gsap.set(sel, { x: dx + q.x, y: dy + q.y }); } }, t); };

  /* ---------- transitions ---------- */
  // coupe diagonale : panel (.diag) + bord lumineux optionnel (.edge)
  MK.diagonal = (tl, panel, edge, t, { to = "polygon(0% 82%, 100% 50%, 100% 100%, 0% 100%)", dur = 0.5 } = {}) => { tl.to(panel, { clipPath: to, duration: dur, ease: "power3.out" }, t); if (edge) { gsap.set(edge, { opacity: 0, y: 500 }); tl.set(edge, { opacity: 1 }, t); tl.to(edge, { y: 0, duration: dur, ease: "power3.out" }, t); } };
  // révélation circulaire depuis (x, y) en px
  MK.circleIn = (tl, sel, t, { x = 540, y = 960, dur = 0.55 } = {}) => { gsap.set(sel, { clipPath: `circle(0px at ${x}px ${y}px)` }); tl.to(sel, { clipPath: `circle(2300px at ${x}px ${y}px)`, duration: dur, ease: "expo.in" }, t); };
  MK.circleOut = (tl, sel, t, { x = 540, y = 960, dur = 0.5 } = {}) => { tl.set(sel, { clipPath: `circle(2300px at ${x}px ${y}px)` }, t); tl.to(sel, { clipPath: `circle(0px at ${x}px ${y}px)`, duration: dur, ease: "expo.in" }, t); };
  // volet plein écran qui monte (origine en bas)
  MK.wipeUp = (tl, sel, t, dur = 0.35) => { gsap.set(sel, { scaleY: 0, transformOrigin: "50% 100%" }); tl.to(sel, { scaleY: 1, duration: dur, ease: "expo.in" }, t); };
  // anneau de verre qui traverse la caméra
  MK.lens = (tl, sel, tIn, tOut) => { gsap.set(sel, { scale: 0.15, opacity: 0 }); tl.to(sel, { scale: 1, opacity: 1, duration: 0.6, ease: MK.ease.card }, tIn); tl.to(sel, { scale: 4, opacity: 0, duration: 0.55, ease: "power3.in" }, tOut); };
  // dérive lente des taches d'un fond fluide
  MK.drift = (tl, blobs, total, seed = 5) => { const r = MK.rng(seed); blobs.forEach((b) => tl.to(b, { x: (r() - 0.5) * 500, y: (r() - 0.5) * 500, scale: 0.8 + r() * 0.6, duration: total / 2, ease: "sine.inOut", yoyo: true, repeat: 1 }, 0)); };

  /* ---------- fin ---------- */
  // fixe la durée totale ; l'enregistrement window.__timelines reste écrit dans la page (le contrôle HyperFrames le cherche là)
  MK.done = (tl, total) => { tl.set({}, {}, total); };

  window.MK = MK;
})();
