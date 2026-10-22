const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/cd6396ce-1997-4801-afef-adc87686af94_17e2dedf-0a8d-4d30-ba14-2e9b4f50d3f5/pptx/scripts/apply_theme.js");
const SLIDES = require("./content.js");
const STYLES = {
  A: { name: "Clean Academic", font: "Calibri", bg: "FFFFFF", fg: "1F2933", accent: "1F6F8B", accent2: "C2410C", muted: "5B6670", panel: "F1F4F6", panelA: "E6F0F3", panelB: "FBEDE6", dark: "FFFFFF", darkFg: "1F2933", minimal: false },
  B: { name: "LMU Green", font: "Arial", bg: "FFFFFF", fg: "1A1A1A", accent: "00883A", accent2: "1A1A1A", muted: "5F6368", panel: "F1F3F2", panelA: "E3F1E8", panelB: "ECECEC", dark: "00883A", darkFg: "FFFFFF", minimal: false },
  C: { name: "Minimal Discussion", font: "Calibri", bg: "1E2227", fg: "F3F4F6", accent: "F2B544", accent2: "7DD3C0", muted: "A3AAB4", panel: "2A2F36", panelA: "2A2F36", panelB: "2A2F36", dark: "1E2227", darkFg: "F3F4F6", minimal: true },
};
const key = process.argv[2], out = process.argv[3], T = STYLES[key];
const THEME = { name: T.name, headFontFace: T.font, bodyFontFace: T.font, colors: { dk1: T.minimal ? T.bg : T.fg, lt1: T.minimal ? T.fg : "FFFFFF", dk2: T.accent, lt2: T.panel, accent1: T.accent, accent2: T.accent2, accent3: T.muted, accent4: T.panelA, accent5: T.panelB, accent6: T.panel, hlink: T.accent, folHlink: T.muted } };
const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE"; pres.theme = { headFontFace: T.font, bodyFontFace: T.font };
pres.title = "Artifact Evaluation – Lecture 2 Discussion (" + T.name + ")";
const M = 0.7, W = 13.333 - 2 * M; let n = 0;
pres.defineSlideMaster({ title: "BASE", background: { color: T.bg }, slideNumber: { x: 12.3, y: 6.95, w: 0.6, h: 0.35, fontSize: 11, color: T.muted, fontFace: T.font },
  objects: [{ text: { text: "Lecture 2 · Artifact evaluation", options: { x: M, y: 6.95, w: 6, h: 0.35, fontSize: 11, color: T.muted, fontFace: T.font } } }] });
pres.defineSlideMaster({ title: "DARK", background: { color: T.dark } });
const t = (s, x, o) => s.addText(x, Object.assign({ isTextBox: true, fontFace: T.font, color: T.fg, valign: "top", margin: 0 }, o));
const box = (s, x, y, w, h, c) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.06, fill: { color: c }, line: { color: c }, objectName: "panel" + (n++) });
const label = (s, l) => t(s, l, { x: M, y: 0.4, w: W, h: 0.9, fontSize: 40, bold: true, color: T.accent, valign: "middle" });
const head = (s, h, size) => t(s, h, { x: M, y: 0.9, w: W, h: 1.3, fontSize: size || 28, bold: true, valign: "top" });
let section = null;
for (const d of SLIDES) {
  if (d.type === "section" || d.type === "title") { section = d.type === "title" ? "Opening" : d.title; pres.addSection({ title: section }); }
  if (d.type === "closing") { section = "Close"; pres.addSection({ title: section }); }
  const dark = ["title", "section", "closing"].includes(d.type);
  const s = pres.addSlide({ masterName: dark ? "DARK" : "BASE", sectionTitle: section });
  const fgD = dark ? T.darkFg : T.fg;
  let notes = d.notes || "";
  if (d.type === "title" || d.type === "closing") { if (d.type === "closing") { t(s, d.title, { x: M, y: 2.8, w: W, h: 1.5, fontSize: 48, bold: true, color: fgD, valign: "middle" }); if (notes) s.addNotes(notes); continue; }
    t(s, d.title, { x: M, y: 2.2, w: W, h: 1.6, fontSize: T.minimal ? 54 : 44, bold: true, color: fgD, valign: "bottom" });
    t(s, d.sub, { x: M, y: 4.0, w: W, h: 1.0, fontSize: 22, color: dark && key === "B" ? "FFFFFF" : (T.minimal ? T.accent : T.accent) });
    if (d.sub2) t(s, d.sub2, { x: M, y: 5.2, w: W, h: 0.5, fontSize: 16, color: key === "B" ? "E3F1E8" : T.muted });
  } else if (d.type === "section") {
    t(s, d.title, { x: M, y: 2.4, w: W, h: 1.2, fontSize: 48, bold: true, color: fgD, valign: "bottom" });
    t(s, d.sub, { x: M, y: 3.8, w: W * 0.85, h: 1.2, fontSize: 20, color: key === "B" ? "E3F1E8" : T.muted });
  } else if (d.type === "index") {
    label(s, d.title);
    d.items.forEach((it, i) => { const y = 1.7 + i * 0.7; t(s, String(i + 1).padStart(2, "0"), { x: M, y, w: 0.8, h: 0.55, fontSize: 22, bold: true, color: T.accent, valign: "middle" });
      t(s, it, { x: M + 0.9, y, w: W - 0.9, h: 0.55, fontSize: 22, valign: "middle" }); });
  } else if (d.type === "content") {
    label(s, d.label);
    if (T.minimal) {
      head(s, d.head, 40);
      const show = d.label === "Research questions" ? d.bullets : [d.bullets[0]];
      t(s, show.map((b, i) => ({ text: b, options: { breakLine: i < show.length - 1, paraSpaceAfter: 8 } })), { x: M, y: 3.4, w: W * 0.9, h: 3.2, fontSize: 24, color: T.muted });
      notes = d.bullets.join("\n") + (notes ? "\n\n" + notes : "");
    } else {
      let y = 1.6;
      if (d.stats) { d.stats.forEach((st, i) => { const w = (W - 0.6) / 3, x = M + i * (w + 0.3); box(s, x, y, w, 1.15, T.panel);
          t(s, st[0], { x: x + 0.25, y: y + 0.12, w: 1.8, h: 0.9, fontSize: 36, bold: true, color: T.accent, valign: "middle" });
          t(s, st[1], { x: x + 2.0, y: y + 0.12, w: w - 2.2, h: 0.9, fontSize: 18, color: T.muted, valign: "middle" }); }); y += 1.45; }
      t(s, d.bullets.map((b, i) => ({ text: b, options: { bullet: { indent: 22 }, breakLine: i < d.bullets.length - 1, paraSpaceAfter: 10 } })), { x: M, y, w: W, h: 6.8 - y, fontSize: d.stats ? 20 : 22 });
    }
  } else if (d.type === "table") {
    label(s, d.label);
    const hdr = T.minimal ? T.panel : (key === "B" ? T.accent : T.accent);
    s.addTable(d.rows.map((r, i) => r.map((c, j) => ({ text: c, options: { bold: i === 0 || j === 0, color: i === 0 ? (T.minimal ? T.accent : "FFFFFF") : T.fg, fill: { color: i === 0 ? hdr : (T.minimal ? T.bg : (i % 2 ? T.panel : "FFFFFF")) }, fontSize: 20, fontFace: T.font } }))),
      { x: M, y: 1.7, w: W, rowH: 0.7, border: { type: "solid", pt: 1, color: T.minimal ? T.panel : "FFFFFF" }, margin: 0.1 });
    if (d.foot) t(s, d.foot, { x: M, y: 1.7 + d.rows.length * 0.7 + 0.35, w: W, h: 1.0, fontSize: 18, color: T.muted });
  } else if (d.type === "question") {
    label(s, d.label);
    if (T.minimal) {
      head(s, d.head, 40);
      t(s, [{ text: d.a[0] + "  ", options: { bold: true, color: T.accent2 } }, { text: d.a[1], options: { breakLine: true } }, { text: d.b[0] + "  ", options: { bold: true, color: T.accent } }, { text: d.b[1] }], { x: M, y: 3.9, w: W, h: 1.6, fontSize: 22, color: T.muted, paraSpaceAfter: 8 });
      notes = "From the papers: " + d.hook + (notes ? "\n\n" + notes : "");
    } else {
      t(s, d.head, { x: M, y: 1.45, w: W, h: 0.9, fontSize: 26, bold: true });
      box(s, M, 2.45, W, 1.3, T.panel); t(s, d.hook, { x: M + 0.3, y: 2.58, w: W - 0.6, h: 1.1, fontSize: 18, color: T.fg });
      const w = (W - 0.3) / 2;
      [[d.a, T.panelA, T.accent], [d.b, T.panelB, T.accent2]].forEach((p, i) => { const x = M + i * (w + 0.3); box(s, x, 3.95, w, 2.65, p[1]);
        t(s, p[0][0], { x: x + 0.3, y: 4.1, w: w - 0.6, h: 0.5, fontSize: 22, bold: true, color: p[2] });
        t(s, p[0][1], { x: x + 0.3, y: 4.7, w: w - 0.6, h: 1.7, fontSize: 20 }); });
    }
  }
  if (notes) s.addNotes(notes);
}
(async () => { await pres.writeFile({ fileName: out }); await applyTheme(out, THEME); console.log("ok " + key); })();
