const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/cd6396ce-1997-4801-afef-adc87686af94_17e2dedf-0a8d-4d30-ba14-2e9b4f50d3f5/pptx/scripts/apply_theme.js");
const OUT = process.argv[2];
const THEME = { name: "Artifact Review", headFontFace: "Cambria", bodyFontFace: "Calibri",
  colors: { dk1: "1B2A30", lt1: "FFFFFF", dk2: "0F4C5C", lt2: "EEF3F4", accent1: "0F4C5C", accent2: "D98E04",
    accent3: "5E8C61", accent4: "B5523B", accent5: "6B7F86", accent6: "9FC1C9", hlink: "0F4C5C", folHlink: "6B7F86" } };
const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE"; pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Artifact Evaluation – Lecture 2 Discussion";
const C = pres.SchemeColor;
const W = 13.333;
pres.defineSlideMaster({ title: "TITLE", background: { color: THEME.colors.dk2 }, objects: [
  { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.2, w: 11.7, h: 1.6, fontSize: 44, bold: true, color: C.background1, valign: "bottom", align: "left" }, text: "" } },
  { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.0, w: 11.7, h: 1.6, fontSize: 20, color: THEME.colors.accent6 ? C.accent6 : C.background1, valign: "top" }, text: "" } } ] });
pres.defineSlideMaster({ title: "SECTION", background: { color: THEME.colors.dk2 }, objects: [
  { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.6, w: 11.7, h: 1.3, fontSize: 40, bold: true, color: C.background1, align: "left" }, text: "" } },
  { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.9, w: 11.7, h: 1.0, fontSize: 20, color: C.accent6 }, text: "" } } ] });
pres.defineSlideMaster({ title: "CONTENT", background: { color: "FFFFFF" }, slideNumber: { x: 12.4, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: "6B7F86" }, objects: [
  { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 12.1, h: 0.9, fontSize: 32, bold: true, color: C.text2 }, text: "" } },
  { text: { text: "Seminar: Reproducibility in SE Research · Lecture 2", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: "6B7F86" } } } ] });

let n = 0;
function card(s, x, y, w, h, fill) { s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill || "EEF3F4" }, line: { color: fill || "EEF3F4" }, objectName: "card" + (n++) }); }
function txt(s, t, o) { s.addText(t, Object.assign({ isTextBox: true, fontSize: 16, color: C.text1, valign: "top", margin: 0.1 }, o)); }
function bullets(items, size) { return items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1, paraSpaceAfter: 6, fontSize: size || 16 } })); }
function stat(s, x, y, w, big, label, col) { txt(s, big, { x, y, w, h: 0.9, fontSize: 40, bold: true, color: col || C.accent1, fontFace: "Cambria" }); txt(s, label, { x, y: y + 0.85, w, h: 0.7, fontSize: 13, color: C.accent5 }); }
function pill(s, x, y, w, t, col) { s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h: 0.42, rectRadius: 0.2, fill: { color: col }, line: { color: col }, objectName: "pill" + (n++) }); txt(s, t, { x, y, w, h: 0.42, fontSize: 13, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0 }); }
function sec(t) { pres.addSection({ title: t }); return t; }

// 1 Title
let S = sec("Opening");
let s = pres.addSlide({ masterName: "TITLE", sectionTitle: S });
s.addText("Who decides what a good artifact is?", { placeholder: "title" });
s.addText("Artifact evaluation from both sides: Hermann, Winter & Siegmund (FSE 2020) and Timperley, Herckis, Le Goues & Hilton (EMSE 2021)\nLecture 2 discussion · 27 October", { placeholder: "body" });
s.addNotes("Welcome. Today: two papers that look at artifact evaluation from opposite sides, the reviewers (Hermann et al.) and the authors (Timperley et al.). Note: Stefan Winter, our lecturer, is a co-author of the Hermann paper.");

// 2 Agenda
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Plan for the next 90 minutes", { placeholder: "title" });
const ag = [["0–5", "Welcome and goals"], ["5–10", "Terminology check"], ["10–25", "Paper summaries"], ["25–30", "Two sides of one problem"], ["30–37", "Warm-up question"], ["37–60", "Core questions, whole group"], ["60–62", "Short break"], ["62–77", "Group work and report back"], ["77–85", "Outside-the-box questions"], ["85–90", "Wrap-up and takeaways"]];
ag.forEach((a, i) => { const col = i % 2, row = Math.floor(i / 2); const x = 0.6 + col * 6.15, y = 1.55 + row * 1.02;
  card(s, x, y, 5.95, 0.85, [4, 5, 7, 8].includes(i) ? "FBEFD5" : "EEF3F4");
  txt(s, a[0] + " min", { x: x + 0.2, y: y + 0.17, w: 1.6, h: 0.5, fontSize: 16, bold: true, color: C.accent1, valign: "middle", margin: 0 });
  txt(s, a[1], { x: x + 1.9, y: y + 0.17, w: 3.9, h: 0.5, fontSize: 17, valign: "middle", margin: 0 }); });
s.addNotes("About 25 minutes of input, about 60 minutes of discussion. Amber blocks are discussion. Keep the summaries to 7 minutes each.");

// 3 Goals
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("What we want to leave with", { placeholder: "title" });
[["Understand", "What artifact evaluation is meant to check, and why nobody agrees"], ["Weigh", "Standards or incentives: which problem should be fixed first?"], ["Propose", "One concrete change to artifact evaluation, and who has to make it"]].forEach((g, i) => {
  const x = 0.6 + i * 4.1; card(s, x, 1.7, 3.9, 3.6); pill(s, x + 0.3, 2.0, 1.8, g[0], [THEME.colors.accent1, THEME.colors.accent2, THEME.colors.accent3][i]);
  txt(s, g[1], { x: x + 0.3, y: 2.7, w: 3.3, h: 2.4, fontSize: 20 }); });
txt(s, "Ground rule: argue from the papers or your own experience; disagreeing is the point.", { x: 0.6, y: 5.7, w: 12, h: 0.6, fontSize: 16, italic: true, color: C.accent5 });

// 4 Terminology
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Terminology check: which terms do the papers use?", { placeholder: "title" });
const rows = [["", "Who runs it", "Which artifacts", "2020 term (our lecture)", "Hermann et al. (old ACM)"],
  ["Same team, same setup", "Authors", "Original", "Repeatability", "Repeatability"],
  ["Other team, same setup", "Others", "Authors' artifacts", "Reproducibility", "Replicability"],
  ["Other team, own setup", "Others", "Independent", "Replicability", "Reproducibility"]];
s.addTable(rows.map((r, i) => r.map((c, j) => ({ text: c, options: { bold: i === 0 || j === 0, color: i === 0 ? "FFFFFF" : "1B2A30", fill: { color: i === 0 ? "0F4C5C" : (j === 3 ? "FBEFD5" : "EEF3F4") }, fontSize: 15 } }))),
  { x: 0.6, y: 1.6, w: 12.1, colW: [2.9, 1.7, 2.2, 2.6, 2.7], rowH: 0.6, border: { type: "solid", pt: 1, color: "FFFFFF" }, margin: 0.08 });
card(s, 0.6, 4.4, 12.1, 1.6, "FBEFD5");
txt(s, [{ text: "Question to the room: ", options: { bold: true } }, { text: "Which of the three does an artifact evaluation committee actually test?" }], { x: 0.9, y: 4.6, w: 11.5, h: 0.6, fontSize: 20 });
txt(s, "ACM swapped the two terms in 2020, after Hermann et al. was accepted (footnote 5, p. 471). Timperley et al. mostly say \"replication\".", { x: 0.9, y: 5.25, w: 11.5, h: 0.6, fontSize: 14, color: C.accent5 });
s.addNotes("Answer: 2020 reproducibility at best: another team runs the authors' artifact. Hermann's 'replicability' = our 'reproducibility'. Keep this to one minute.");

// 5 Section summaries
S = sec("Paper summaries");
s = pres.addSlide({ masterName: "SECTION", sectionTitle: S });
s.addText("Two papers, two sides", { placeholder: "title" }); s.addText("The reviewers' view, then the authors' view · 15 minutes", { placeholder: "body" });

// 6 Hermann overview
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Hermann et al. 2020: asking the reviewers", { placeholder: "title" });
txt(s, [{ text: "Question: ", options: { bold: true } }, { text: "What do AEC members think artifact evaluation is for, and what makes a good artifact?" }], { x: 0.6, y: 1.45, w: 12.1, h: 0.7, fontSize: 18 });
stat(s, 0.6, 2.3, 2.9, "79", "calls for artifacts analysed, 2011–2019");
stat(s, 3.6, 2.3, 2.9, "1034", "AEC members invited");
stat(s, 6.6, 2.3, 2.9, "257", "responses (~25 %), mostly programming languages");
stat(s, 9.6, 2.3, 3.1, "< 30 min", "the only real threshold any call sets: setup and a basic test");
card(s, 0.6, 4.3, 12.1, 2.3);
txt(s, bullets(["Method: document analysis of the calls, then a survey with open questions, analysed by card sorting", "No artifact was opened; badges were not checked against artifact quality", "ESEC/FSE 2020 · printed pp. 469–480 · co-author Stefan Winter is our lecturer"], 16), { x: 0.9, y: 4.5, w: 11.5, h: 2.0 });
s.addNotes("Pre-study: 79 calls for artifacts from SE and PL conferences. Survey: 1034 AEC members invited, 257 responded, 124 completed. Counts are given as total (PL/SE).");

// 7 Hermann findings
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Hermann et al.: no agreed threshold", { placeholder: "title" });
[["Purpose drifts", "From \"check the claims\" to reproducibility and reuse. Reviewers stress reproducing results, users stress reuse (p. 479)."],
 ["No thresholds", "Calls list criteria (documentation 46, consistency 45, completeness 39) but almost never say how good is good enough (pp. 471–472)."],
 ["Mixed value", "20 users see a difference between evaluated and unevaluated artifacts, 34 do not (p. 477)."],
 ["One-time reviewers", "Most serve on an AEC only once; a third have never submitted an artifact themselves (pp. 473, 478)."]].forEach((f, i) => {
  const x = 0.6 + (i % 2) * 6.15, y = 1.55 + Math.floor(i / 2) * 2.55; card(s, x, y, 5.95, 2.35);
  txt(s, f[0], { x: x + 0.25, y: y + 0.2, w: 5.4, h: 0.55, fontSize: 20, bold: true, color: C.accent1 });
  txt(s, f[1], { x: x + 0.25, y: y + 0.8, w: 5.4, h: 1.45, fontSize: 18 }); });
s.addNotes("Also: 13 respondents asked, unprompted, for artifact evaluation to be coupled to paper acceptance. ICSE/FSE dropped the Functional badge to raise the bar (p. 476).");

// 8 Timperley overview
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Timperley et al. 2021: asking the authors", { placeholder: "title" });
txt(s, [{ text: "Question: ", options: { bold: true } }, { text: "Does the SE community value artifacts, and what makes creating, using and reviewing them hard?" }], { x: 0.6, y: 1.45, w: 12.1, h: 0.7, fontSize: 18 });
stat(s, 0.6, 2.3, 2.9, "62.7 %", "of 1434 papers (ICSE, FSE, ASE, EMSE 2014–18) link an artifact");
stat(s, 3.6, 2.3, 2.9, "153", "authors surveyed (22 % response)");
stat(s, 6.6, 2.3, 2.9, "~14 %", "of artifact links dead in 2019 (26 % for 2014 papers)", C.accent4);
stat(s, 9.6, 2.3, 3.1, "74 of 196", "FSE artifact papers submitted to AE; 64 accepted", C.accent2);
card(s, 0.6, 4.3, 12.1, 2.3);
txt(s, bullets(["\"Artifact\" = any link to external material; \"available\" = the link still works", "Thematic analysis shows the range of challenges, not how common each is (p. 9)", "Secondary analysis with Diffusion of Innovations, then 8 recommendations (R1–R8)"], 16), { x: 0.9, y: 4.5, w: 11.5, h: 2.0 });
s.addNotes("Watch the Fig. 4 maths: the paper reports 26.33 %, which is 74 of all 281 papers. Of the 196 papers with artifacts it is about 38 %.");

// 9 Timperley challenges
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Timperley et al.: twelve challenges, one root", { placeholder: "title" });
const ch = ["C1 Not worth it", "C2 Portability", "C3 Maintenance", "C4 Tacit knowledge", "C5 Doesn't fit purpose", "C6 No standards", "C7 Hosting", "C8 Double-blind review", "C9 External constraints", "C10 No reviewer incentives", "C11 Technical obstacles", "C12 Limited communication"];
ch.forEach((c, i) => { const x = 0.6 + (i % 4) * 3.05, y = 1.55 + Math.floor(i / 4) * 0.85; const hot = [0, 5, 9].includes(i);
  card(s, x, y, 2.9, 0.7, hot ? "FBEFD5" : "EEF3F4"); txt(s, c, { x: x + 0.15, y, w: 2.65, h: 0.7, fontSize: 15, bold: hot, valign: "middle" }); });
card(s, 0.6, 4.3, 5.95, 2.3); card(s, 6.75, 4.3, 5.95, 2.3);
txt(s, [{ text: "Users' top problems (n = 130)", options: { bold: true, breakLine: true, color: C.accent1 } }, ...bullets(["No usage instructions: 103", "Artifact no longer accessible: 81", "Had to re-implement: 28"], 15)], { x: 0.85, y: 4.45, w: 5.5, h: 2.1, fontSize: 17 });
txt(s, [{ text: "Recommendations R1–R8", options: { bold: true, breakLine: true, color: C.accent1 } }, ...bullets(["Creators: describe, self-contain, plan from day one", "Reviewers and organisers: rubrics, clear goals, cheaper reviewing", "Community: count artifacts in hiring, promotion and grants"], 15)], { x: 7.0, y: 4.45, w: 5.5, h: 2.1, fontSize: 17 });
s.addNotes("Highlighted: the incentive and standards challenges, which the discussion focuses on. Table 4, pp. 14–15; Table 5, p. 19; Table 6, pp. 29–30.");

// 10 Comparison
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Same problem, seen from two sides", { placeholder: "title" });
const cmp = [["", "Hermann et al.", "Timperley et al."], ["Who is asked", "Reviewers (AEC members)", "Authors (creators, users, few reviewers)"], ["Field", "SE and programming languages", "Software engineering only"],
  ["Diagnosis", "Unclear purpose and standards", "Misaligned incentives, poor communication"], ["Proposal", "Clear purpose and criteria per community; experienced reviewers", "R1–R8 for creators, reviewers, organisers, community leaders"], ["Both agree", "Artifacts should count towards paper acceptance", "Artifacts should count towards paper acceptance"]];
s.addTable(cmp.map((r, i) => r.map((c, j) => ({ text: c, options: { bold: i === 0 || j === 0, color: i === 0 ? "FFFFFF" : "1B2A30", fill: { color: i === 0 ? "0F4C5C" : (i === 5 ? "FBEFD5" : "EEF3F4") }, fontSize: 15 } }))),
  { x: 0.6, y: 1.6, w: 12.1, colW: [2.3, 4.9, 4.9], rowH: 0.7, border: { type: "solid", pt: 1, color: "FFFFFF" }, margin: 0.1 });
txt(s, "They cite each other: Timperley et al. build three recommendations on Hermann et al.", { x: 0.6, y: 6.1, w: 12.1, h: 0.5, fontSize: 14, italic: true, color: C.accent5 });
s.addNotes("Bridge into the discussion: both papers see the same missing standard, and each partly blames the other side's missing guidance.");

// Discussion
S = sec("Discussion");
s = pres.addSlide({ masterName: "SECTION", sectionTitle: S });
s.addText("Discussion", { placeholder: "title" }); s.addText("Warm-up, three whole-group questions, group work, outside-the-box", { placeholder: "body" });

function qslide(title, q, hook, a, b, notes) {
  const sl = pres.addSlide({ masterName: "CONTENT", sectionTitle: S }); sl.addText(title, { placeholder: "title" });
  txt(sl, q, { x: 0.6, y: 1.45, w: 12.1, h: 1.1, fontSize: 24, bold: true, color: C.text1, fontFace: "Cambria" });
  card(sl, 0.6, 2.75, 12.1, 1.35); txt(sl, [{ text: "From the papers  ", options: { bold: true, color: C.accent1 } }, { text: hook }], { x: 0.85, y: 2.85, w: 11.6, h: 1.15, fontSize: 16 });
  card(sl, 0.6, 4.35, 5.95, 2.3, "E7F0E8"); card(sl, 6.75, 4.35, 5.95, 2.3, "FBEFD5");
  txt(sl, [{ text: a[0], options: { bold: true, breakLine: true, color: C.accent3 } }, { text: a[1] }], { x: 0.85, y: 4.5, w: 5.5, h: 2.05, fontSize: 20 });
  txt(sl, [{ text: b[0], options: { bold: true, breakLine: true, color: C.accent2 } }, { text: b[1] }], { x: 7.0, y: 4.5, w: 5.5, h: 2.05, fontSize: 20 });
  sl.addNotes(notes); return sl; }

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Warm-up · 7 min", { placeholder: "title" });
txt(s, "Would you sign up for an artifact evaluation committee next year?\nWhy or why not?", { x: 0.6, y: 1.8, w: 12.1, h: 1.8, fontSize: 32, bold: true, fontFace: "Cambria", color: C.text2 });
card(s, 0.6, 4.1, 12.1, 1.6);
txt(s, "Most AEC members serve only once (Hermann et al., Fig. 2, p. 473). \"We usually just make students do AEC\" (Timperley et al., participant 64, p. 23).", { x: 0.85, y: 4.3, w: 11.6, h: 1.3, fontSize: 17 });
s.addNotes("Quick round, everyone answers in one sentence. Leads straight into incentives: learning opportunity vs. unpaid, low-status work.");

qslide("Q1 · Low bar or high bar?", "Should artifact badges be easy to get (more sharing) or hard to get (badges that mean something)?",
  "\"Enforcing quality criteria only means that some authors will not publish their code\" (Hermann p. 475). ICSE and FSE dropped the Functional badge to raise the bar (p. 476). At FSE, 86 % of submitted artifacts were accepted (Timperley Fig. 4, p. 21).",
  ["Low bar", "Availability is the bottleneck. Any code beats no code."], ["High bar", "If 86 % pass, a badge signals little to users."],
  "If it stalls: Hermann found 34 users saw no difference between evaluated and unevaluated artifacts and 20 did (p. 477). Does that support the low bar or the high bar? About 7 min.");
qslide("Q2 · Should the artifact decide the paper?", "Should a failed artifact evaluation be able to get a paper rejected?",
  "Both papers lean yes (Hermann pp. 478–479, 13 unprompted respondents; Timperley p. 28). CAV and TACAS already require artifacts for tool papers. \"The evaluations do not determine if the paper is accepted, so I didn't pay much attention\" (Hermann, id 79, p. 478).",
  ["Yes, couple them", "Otherwise artifact evaluation is optional decoration, and reviewers know it."], ["No, keep separate", "Puts one-time junior reviewers in charge of careers, clashes with double-blind review (C8), penalises industry papers (C9)."],
  "If it stalls: what about Hermann's 'conditional acceptance' (id 214, p. 478)? About 8 min.");
qslide("Q3 · Run the scripts or try to break them?", "Should artifact reviewers just run the authors' scripts, or probe whether the results hold up?",
  "\"AECs, by asking for replicable scripts, are likely to replicate the same mistake\" (Timperley participant 25, p. 22). Some Hermann reviewers modify experiments, and 24 calls encourage it (p. 475). One reviewer found hard-coded outputs only by reading the code (p. 477).",
  ["Run the scripts", "Cheap, scalable, clear pass or fail: exactly what 2020 reproducibility means."], ["Probe", "Otherwise a badge just certifies that a bug is repeatable."],
  "If it stalls: how long would it take to find hard-coded outputs, and who pays for that time? About 8 min.");

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Short break · 2 min", { placeholder: "title" });
txt(s, "Next: two groups, two questions, 10 minutes, then report back", { x: 0.6, y: 2.8, w: 12.1, h: 1.0, fontSize: 28, fontFace: "Cambria", color: C.text2, align: "center" });

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Group work · 10 min, then 5 min report back", { placeholder: "title" });
[["Group A · Standards or incentives?", "If you could change one thing, would it be clear standards (Hermann's diagnosis) or rewards for artifact work (Timperley's diagnosis)?", "Timperley participant 31 stopped submitting to AE because of \"wildly different reviewer expectations\" (p. 26). Standards problem or incentive problem?"],
 ["Group B · Who keeps an artifact alive?", "After the PhD student graduates, who is responsible for a research tool?", "26 % of 2014 links dead by 2019 (Timperley Fig. 3, p. 20). R3 asks for transition plans and a Zenodo snapshot (p. 32). Is a frozen snapshot enough?"]].forEach((g, i) => {
  const x = 0.6 + i * 6.15; card(s, x, 1.55, 5.95, 5.1, i ? "FBEFD5" : "E7F0E8");
  txt(s, g[0], { x: x + 0.25, y: 1.7, w: 5.45, h: 0.6, fontSize: 20, bold: true, color: i ? C.accent2 : C.accent3 });
  txt(s, g[1], { x: x + 0.25, y: 2.4, w: 5.45, h: 1.6, fontSize: 20, bold: true });
  txt(s, g[2], { x: x + 0.25, y: 4.0, w: 5.45, h: 1.8, fontSize: 17 });
  txt(s, "Bring back: one position and its best argument", { x: x + 0.25, y: 5.9, w: 5.45, h: 0.5, fontSize: 14, italic: true, color: C.accent5 }); });
s.addNotes("Split the room in two. Each group appoints a speaker who reports one position and its strongest argument in about 2 minutes. Then let the other group respond.");

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Outside the box · 8 min", { placeholder: "title" });
[["What if artifacts counted exactly like papers for your PhD and for hiring?", "What would go wrong? How would people game it?"],
 ["Imagine an AI agent builds and runs every artifact automatically", "What would it catch, and what would it miss? What are human reviewers for?"],
 ["Spare: review artifacts before the paper, like a registered report?", "Would that change what gets built?"]].forEach((q, i) => {
  const y = 1.55 + i * 1.7; card(s, 0.6, y, 12.1, 1.5);
  txt(s, q[0], { x: 0.85, y: y + 0.15, w: 11.6, h: 0.6, fontSize: 20, bold: true, color: i === 2 ? C.accent5 : C.text1 });
  txt(s, q[1], { x: 0.85, y: y + 0.8, w: 11.6, h: 0.55, fontSize: 16, color: C.accent5 }); });
s.addNotes("Expected for Q1: salami-sliced artifacts, gamed GitHub stars, badges as metrics (Goodhart's law). Q2 connects to the 30-minute setup rule (Hermann p. 472), CI checks (Timperley R2, p. 31) and 'replicating the same mistake'.");

// Wrap-up
S = sec("Wrap-up");
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Wrap-up · one change each", { placeholder: "title" });
txt(s, "Name one change to artifact evaluation you would make, and who has to make it.", { x: 0.6, y: 1.5, w: 12.1, h: 0.9, fontSize: 24, bold: true, fontFace: "Cambria" });
["Author", "Advisor", "AEC chair", "Steering committee", "Funder"].forEach((r, i) => { const x = 0.6 + i * 2.45; card(s, x, 2.7, 2.3, 2.6); pill(s, x + 0.2, 2.9, 1.9, r, [THEME.colors.accent1, THEME.colors.accent3, THEME.colors.accent2, THEME.colors.accent4, THEME.colors.accent5][i]); });
txt(s, "Then: which of our ideas did neither paper propose?", { x: 0.6, y: 5.6, w: 12.1, h: 0.6, fontSize: 18, italic: true, color: C.accent5 });
s.addNotes("Collect answers in the boxes (on the board or by editing this slide live). Optional question for the lecturer: what has changed in artifact evaluation since 2020?");

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("Background, if questions come up", { placeholder: "title" });
txt(s, bullets(["ACM badges v1.1 (2020) swapped \"reproduced\" and \"replicated\", matching our lecture's definitions", "Artifact evaluation started at ESEC/FSE 2011; ICSE from 2019 (Timperley p. 4)", "Zenodo gives DOIs and snapshots and can archive GitHub releases; Software Heritage archives public source code", "Containers share the host kernel; VMs emulate a whole machine and distort performance. Neither freezes what a build downloads", "Funders: NSF requires a two-page data management plan (Timperley p. 34)"], 18), { x: 0.6, y: 1.5, w: 12.1, h: 4.6 });
txt(s, "From memory where no page is given: check before stating as fact.", { x: 0.6, y: 6.2, w: 12.1, h: 0.4, fontSize: 12, italic: true, color: C.accent5 });

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S });
s.addText("References", { placeholder: "title" });
txt(s, bullets(["Hermann, B., Winter, S., Siegmund, J. (2020). Community Expectations for Research Artifacts and Evaluation Processes. ESEC/FSE 2020, pp. 469–480. doi:10.1145/3368089.3409767", "Timperley, C. S., Herckis, L., Le Goues, C., Hilton, M. (2021). Understanding and improving artifact sharing in software engineering research. Empirical Software Engineering 26:67. doi:10.1007/s10664-021-09973-5", "Week 1 context: Collberg & Proebsting (2016), CACM 59(3); Heumüller et al. (2020), EMSE"], 17), { x: 0.6, y: 1.5, w: 12.1, h: 4.5 });

(async () => { await pres.writeFile({ fileName: OUT }); await applyTheme(OUT, THEME); console.log("ok"); })();
