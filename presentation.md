# ACMX AI Assistant — Presentation Slides
**Hackathon 2026 · 5-minute presentation · 9 slides**

---

## Global Design

- **Background:** Near-black (`#0d1117`)
- **Card surfaces:** Dark grey (`#161b22`) with subtle borders
- **Accent (blue):** `#2ea7e0` — used for labels, highlights, arrows
- **Accent (green):** `#56d364` — used for success states and "thank you"
- **Warning (orange):** `#f0883e` — used to highlight pain/problems
- **Purple:** `#a371f7` — used only on roadmap slide
- **Body text:** Near-white. Muted/secondary text: grey
- **Font:** System sans-serif (Inter or similar)
- A thin gradient progress bar (blue → green) runs across the top
- Slide number shown bottom-right in faint grey

---

## Slide 1 — Title

**Label (blue, uppercase):** `Hackathon 2026 · Team ACMX`

**Headline:**
> # ACMX **AI Assistant**
> ("AI Assistant" in blue)

**Subtitle (grey):**
> A RAG-powered chatbot that turns ACMX from an expert-driven system into a self-serve, scalable platform — delivered in Slack.

**Pill badges (5 tags in a row):**
- `RAG · Retrieval-Augmented Generation`
- `Claude Sonnet 4 · Autodesk AIS`
- `Chroma · Cross-Encoder Rerank`
- `Slack Bot · Socket Mode`
- `AWS Lambda · S3`

**Speaker script:**
> Hi everyone. Today we're presenting ACMX AI Assistant — our hackathon project. In short: we built a RAG-powered chatbot that helps engineers understand and use ACMX without needing to schedule a call with the core team. I'll walk you through the problem, what we built, how it works, and where we see it going.

---

## Slide 2 — The Problem

**Label (blue, uppercase):** `The Problem`

**Headline:**
> ## Flexibility creates **complexity**
> ("complexity" in orange)

**2-column card grid:**

| Card 1 | Card 2 |
|--------|--------|
| 🧠 **Understanding — "What does ACMX do?"** | ⚙️ **Application — "How do I use it?"** |
| Policies, roles, permissions, data points. Abstract concepts unfamiliar to most teams. Hard to build a mental model without guidance. | Even after reading the docs, engineers can't translate product requirements into correct policies, specs, or integrations. |

**Quote block (blue left border, italic):**
> *"I read the docs. I still don't know where to start."*

**Speaker script:**
> ACMX is powerful and flexible — but flexibility comes with a trade-off: complexity. Engineers need to learn not just the API, but also how to write policies, define activities, and map everything to their real product. That's two separate challenges: understanding what ACMX is conceptually, and then actually applying it. Most engineers hit a wall at both.

---

## Slide 3 — The Gap

**Label (blue, uppercase):** `The Gap`

**Headline:**
> ## Read the docs. **Still stuck.**
> ("Still stuck." in orange)

**3-column stat boxes:**

| Box 1 | Box 2 | Box 3 |
|-------|-------|-------|
| 📄 | 📅 | 🐌 |
| **Read documentation** | **Schedule a meeting** | **Manual onboarding** |
| Still unsure how to start | With ACMX engineers to get unblocked | Doesn't scale as adoption grows |

**Body text below:**
> Every adopting team repeats this cycle. As ACMX grows, **this bottleneck grows with it.** (last phrase in orange)

**Speaker script:**
> This creates a repeating cycle for every new team. They hear about ACMX, they get interested, they read the documentation — and they get stuck. The current solution is to reach out to the ACMX team directly. That works for one or two teams, but it doesn't scale across the organization. Every new adopter needs a meeting, and adoption becomes bottlenecked by the team's availability.

---

## Slide 4 — Our Solution

**Label (blue, uppercase):** `Our Solution`

**Headline:**
> ## ACMX **AI Assistant**
> ("AI Assistant" in blue)

**2-column layout:**

**Left column — 2 stacked cards:**

- 🔍 **RAG Pipeline**
  Confluence wiki + Git repos indexed into a Chroma vector store. Retrieve 30 candidates → cross-encoder rerank → top 6 → Claude Sonnet 4.

- 🪵 **AWS Lambda + S3**
  Lambda reads log data from S3 buckets and feeds it into the same agent pipeline — so answers can draw on both documentation and operational context.

**Right column — single tall card:**

Label: `THREE ACCESS MODES`

- ▸ **CLI** — interactive terminal Q&A
- ▸ **REST API** — `POST /ask`
- ▸ **Slack Bot** — @mention in any channel *(third bullet in green)*

**Speaker script:**
> So we asked: how do we remove the ACMX team from the critical path of every new integration? Our answer is an AI assistant grounded in real ACMX documentation. Not a generic chatbot — a RAG system that retrieves from actual wiki pages and Git repositories, reranks the evidence, and gives engineers precise, source-cited answers. And we deliver it in Slack, which is where engineers already work.

---

## Slide 5 — Architecture

**Label (blue, uppercase):** `Architecture`

**Headline:**
> ## Six-layer **RAG stack**
> ("RAG stack" in blue)

**Table (full width, 2 columns):**

| Layer | Role |
|---|---|
| Embeddings + Chroma | Chunk, embed, and store docs; cosine similarity search over semantic content. |
| Retriever | Vector similarity search — fetch top 30 candidate chunks per query. |
| Cross-Encoder | Rerank candidates; keep top 6 passage-level matches for context. |
| LLM — Claude Sonnet 4 | Compose a grounded answer from retrieved chunks via Autodesk AIS. |
| AWS Lambda + S3 | Pull logs from S3 buckets and feed processed content into the agent alongside wiki sources. |
| Slack Bot | User-facing entry point; @mentions trigger the full RAG flow in-thread. |

Header row has blue-tinted background. First column is bold white text.

**Speaker script:**
> Here's the architecture. Each layer has a specific responsibility. Embeddings and Chroma store the chunks. The retriever does a vector similarity search. The cross-encoder reranks candidates so the most relevant paragraph-level evidence rises to the top. Claude Sonnet 4 then composes an answer using that evidence — not from memory alone. AWS Lambda brings in S3 log data alongside the wiki content. And the Slack bot is the user-facing entry point.

---

## Slide 6 — How It Works

**Label (blue, uppercase):** `How It Works`

**Headline:**
> ## Question to **answer** in seconds
> ("answer" in blue)

**Horizontal 5-step flow diagram with blue arrows between each box:**

```
[ 💬 @Mention ] → [ 🗄️ Retrieve ] → [ ⚖️ Rerank ] → [ 🤖 Generate ] → [ ✅ Reply ]
User asks in      Top 30 chunks     Cross-Encoder    Claude Sonnet 4   In-thread with
Slack channel     via Chroma        keeps top 6      via Autodesk AIS  source citations
                  vector search
```

Last box (Reply) has a green border instead of the default grey.

**2-column card row below the flow:**

| Card 1 | Card 2 |
|--------|--------|
| 🧵 **Per-thread history** | 📎 **Source citations** |
| Each Slack thread gets its own conversation context — follow-up questions work without re-explaining. | Every answer ends with the Confluence page titles and URLs it drew from — grounded, auditable, trustworthy. |

**Speaker script:**
> At question time, here's the end-to-end flow. A user @mentions the bot in Slack. The question is embedded and matched against the vector store — top 30 candidates come back. A cross-encoder scores each query-chunk pair and we keep the top 6. Those 6 chunks plus the question go to Claude, which returns a grounded, source-cited answer. The bot edits the Thinking placeholder with the final reply — in the same thread. Each thread keeps its own conversation history, so follow-ups work naturally.

---

## Slide 7 — Business Value

**Label (blue, uppercase):** `Business Value`

**Headline:**
> ## Why this **matters**
> ("matters" in green)

**2-column grid of 6 items** (each item: emoji icon on left, bold title + short description):

| | |
|---|---|
| ⚡ **Time to answer** — No more hunting across Confluence for every repeat question. | 🎯 **Quality & trust** — RAG grounds answers in source chunks — more correct than raw LLM chat. |
| 📈 **Scale of support** — Serves all teams simultaneously. No calendar dependency. | 🚀 **Onboarding** — New engineers get consistent, doc-aligned answers on day one. |
| 🪵 **Ops & incidents** — S3 log chunks via Lambda support "what happened when…" questions post-launch. | 🔭 **Strategic fit** — Assistive, auditable (cite sources), and automatable as ACMX matures. |

**Speaker script:**
> The business value is concrete. Engineers stop hunting across Confluence pages for the same repeat questions. Answers are grounded in source chunks, which reduces hallucination versus a raw LLM chat. New engineers and partners get consistent explanations aligned with published ACMX material — no more onboarding meetings required. And the same stack scales to more channels and teams as documentation grows.

---

## Slide 8 — Future Roadmap

**Label (blue, uppercase):** `Future Roadmap`

**Headline:**
> ## Building a **data flywheel**
> ("data flywheel" in purple)

**3 stacked horizontal cards** (large icon on left, title + description on right):

- 💬 **Slack help-channel history** *(planned)*
  Index real engineer replies so the assistant reflects how we actually explain fixes — not only static wiki text. Waiting for launch + Q&A volume.

- 🔄 **Auto wiki indexing** *(planned)*
  New page under the ACMX namespace → automatically fetched, chunked, and re-indexed into Chroma. No manual rebuilds.

- 🪵 **S3 log → vector DB automation** *(post-launch)*
  Full loop: ACMX service logs land in S3 → automatically ingested into the vector DB → retrieval stays current with live production behavior.

**Speaker script:**
> Looking ahead, we have three planned improvements. First — enrich the corpus with Slack help-channel history so the assistant reflects how we actually explain things, not only static wiki text. We're waiting for ACMX to launch and generate real Q&A volume first. Second — wiki automation: when a new page is created under the ACMX namespace, it should be automatically re-indexed into Chroma so the vector store stays fresh. Third — fully automate the S3 log pipeline so operational logs land in the vector DB continuously, making retrieval always current with production reality.

---

## Slide 9 — Thank You

**Centered layout. Subtle green radial glow in background.**

**Label (blue, uppercase, centered):** `Summary`

**Headline (centered):**
> ## Thank **you**
> ("you" in green)

**Subtitle (grey, centered):**
> We built an ACMX RAG pipeline — Chroma + Cross-Encoder + Claude Sonnet 4 — delivered in Slack.
> AWS Lambda brings S3 logs into the same pipeline.
> A clear roadmap to a self-updating, org-scale knowledge base.

**3-column stat boxes (centered, max ~760px wide):**

| Box 1 | Box 2 | Box 3 |
|-------|-------|-------|
| 🔍 | 💬 | 🚀 |
| **RAG Pipeline** | **Slack Bot** | **Self-serve** |
| Chroma · Rerank · Claude | In-thread · Per-thread history | No meeting required |

**Speaker script:**
> That's our project. We built an ACMX RAG pipeline — Chroma, cross-encoder reranking, Claude Sonnet 4 — exposed through Slack so real questions get grounded, fast answers. AWS Lambda brings S3 log data into the same pipeline. We have a clear roadmap: help-channel content, automatic wiki indexing, and fully automated S3 log ingestion after launch. Thank you — we're happy to do a live demo or take questions.
