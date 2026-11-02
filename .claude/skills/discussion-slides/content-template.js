// Content for one discussion deck. Copy to Vorl_N/slides/content.js and fill in.
// Every slide header is a plain section name. No invented titles, taglines or subheadlines;
// anything explanatory goes into the bullets, the table foot, or the speaker notes.
module.exports = [
  { type: "title", title: "Lecture N: Paper Discussion", sub: "<Authors (Venue Year)> · <Authors (Venue Year)>", sub2: "Seminar: Reproducibility of Scientific Results in Software Engineering Research · <date>" },
  { type: "index", items: ["Paper 1: <Author> et al. <year> · summary", "Paper 1 · discussion", "Paper 2: <Author> et al. <year> · summary", "Paper 2 · discussion", "Cross comparison: similarities and differences", "Discussion: what do you agree with?", "Criticism of the papers"] },

  { type: "section", title: "Paper 1", sub: "<Authors (Year)>: <Full title> · <Venue, pages>" },
  { type: "content", header: "General Summary", bullets: ["<3–5 short points>"], notes: "" },
  { type: "table", header: "Terminology / Definitions", rows: [["Setting", "Paper's term", "Our lecture (2020)"], ["...", "...", "..."]], foot: "<definitions with page numbers>" },
  { type: "content", header: "Research Questions", bullets: ["RQ1: ..."] },
  { type: "content", header: "Methodology", stats: [["<n>", "<label>"], ["<n>", "<label>"], ["<n>", "<label>"]], bullets: ["..."] },
  { type: "content", header: "Results", bullets: ["... (p. x)"] },
  { type: "content", header: "Validity / Discussion", bullets: ["..."] },
  { type: "question", header: "Paper 1 · Discussion", question: "<open question>", hook: "<quote or number with page>", a: ["<position A>", "<argument>"], b: ["<position B>", "<argument>"], notes: "<follow-up if it stalls>" },

  { type: "section", title: "Paper 2", sub: "<Authors (Year)>: <Full title> · <Venue>" },
  // ... same six summary slides and 2–3 discussion questions as Paper 1 ...

  { type: "section", title: "Cross Comparison" },
  { type: "table", header: "Cross Comparison: Differences", rows: [["", "Paper 1", "Paper 2"], ["Asked", "...", "..."]] },
  { type: "content", header: "Cross Comparison: Similarities", bullets: ["..."] },
  { type: "question", header: "Discussion: What Do You Agree With?", question: "...", hook: "...", a: ["...", "..."], b: ["...", "..."] },

  { type: "section", title: "Criticism" },
  { type: "content", header: "Criticism · Paper 1", bullets: ["..."], notes: "Counterpoint: ..." },
  { type: "content", header: "Criticism · Paper 2", bullets: ["..."] },

  { type: "content", header: "Open Floor", bullets: ["Any further discussion points you wanted to bring up?", "Criticisms of either paper we have not covered", "Further interesting ideas or approaches you want to talk about", "Anything from your own notes and preparation"] },
  { type: "closing", title: "Thank you for your attention" },
];
