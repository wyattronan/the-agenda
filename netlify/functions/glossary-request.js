// The Agenda — "Request a definition" endpoint for the Glossary tab.
// Files each request as a GitHub issue labeled "glossary-request" in wyattronan/the-agenda.
// The daily Claude update reads those issues, drafts the definition, and opens a pull request for review.
//
// Setup (once): in Netlify, Site configuration → Environment variables, add GITHUB_TOKEN:
// a fine-grained GitHub token with access to wyattronan/the-agenda only and "Issues: Read and write".

const REPO = process.env.GLOSSARY_REPO || "wyattronan/the-agenda";
const LABEL = "glossary-request";
const clean = (s, max) => String(s || "").replace(/[\u0000-\u001f\u007f]/g, " ").replace(/\s+/g, " ").trim().slice(0, max);

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") return { statusCode: 405, body: "Method not allowed" };
  let data;
  try { data = JSON.parse(event.body || "{}"); } catch { return { statusCode: 400, body: "Bad request" }; }

  // Honeypot: real visitors never fill this hidden field.
  if (data.website) return { statusCode: 200, body: JSON.stringify({ ok: true }) };

  const term = clean(data.term, 120);
  const note = clean(data.note, 600);
  const query = clean(data.query, 200);
  if (term.length < 2) return { statusCode: 400, body: "Missing term" };

  const token = process.env.GITHUB_TOKEN;
  if (!token) return { statusCode: 500, body: "Not configured" };
  const gh = (path, opts = {}) => fetch(`https://api.github.com/repos/${REPO}${path}`, {
    ...opts,
    headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json", "User-Agent": "the-agenda-glossary", ...(opts.headers || {}) },
  });

  const title = `Glossary request: ${term}`;
  const when = new Date().toISOString();

  // If the same term is already requested and open, add a +1 comment instead of a duplicate issue.
  const open = await gh(`/issues?state=open&labels=${LABEL}&per_page=100`);
  if (open.ok) {
    const dupe = (await open.json()).find((i) => i.title.toLowerCase() === title.toLowerCase());
    if (dupe) {
      await gh(`/issues/${dupe.number}/comments`, { method: "POST", body: JSON.stringify({ body: `Requested again ${when}.${note ? `\n\n> ${note}` : ""}` }) });
      return { statusCode: 200, body: JSON.stringify({ ok: true, duplicate: true }) };
    }
  }

  const body = [
    `**Term or question:** ${term}`,
    note ? `**What the visitor was trying to understand:** ${note}` : null,
    query && query !== term ? `**What they searched for:** ${query}` : null,
    `**Submitted:** ${when} from the Glossary tab`,
    "",
    "_For the daily update: draft a glossary entry in the existing format (term, part of speech, forms, plain-language definition, In practice using the term in context, Can it change? with the votes needed, any If/Then links), source every fact, and open a pull request for review. Don't publish directly to main._",
  ].filter((l) => l !== null).join("\n\n");

  const res = await gh(`/issues`, { method: "POST", body: JSON.stringify({ title, body, labels: [LABEL] }) });
  if (!res.ok) return { statusCode: 502, body: "Could not file request" };
  return { statusCode: 200, body: JSON.stringify({ ok: true }) };
};
