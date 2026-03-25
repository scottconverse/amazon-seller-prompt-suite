# Amazon Seller Prompt Suite v1.3

6 system prompts for Amazon marketplace selling.
Works with **any AI** — ChatGPT, Claude, Gemini, Copilot, Llama, Mistral, or any instruction-following model.
Works with any brand, any product category, any seller account type.

---

> **IMPORTANT DISCLAIMER**
>
> **This is not financial or business advice.** AI output may be inaccurate, outdated, or misleading. This project is **not affiliated with, endorsed by, or associated with Amazon.com, Inc.** in any way.
>
> Following AI-generated recommendations may result in financial loss, listing suppression, or Amazon account action (including suspension). Amazon policies, fees, and marketplace rules change frequently and without notice. AI models may present outdated or incorrect policy interpretations as current fact.
>
> **Verify all information independently in Amazon Seller Central before acting on it.** You are solely responsible for your Amazon seller account and all business decisions.
>
> See the [Terms of Service](docs/terms.html) for complete legal terms.

---

## What These Are

Each file is a standalone system prompt that turns a general-purpose AI into a specialist Amazon advisor. Paste one into your AI's system prompt, custom instructions, or "role" field and start a conversation.

Every prompt enforces hard gates (refuses to proceed without real data), detects contradictions in your inputs, and refuses to fabricate numbers it doesn't have.

## The 6 Prompts

| Prompt | File | What It Does |
|---|---|---|
| **Listing Optimizer** | `listing-optimizer.md` | Titles, bullets, backend keywords, A+ Content plans, image shot lists. Title positioning logic for value/mid-market/premium brands. Backend keyword packing with UTF-8 byte counting. Variation architecture framework for multi-dimension structuring. |
| **Trend Researcher** | `trend-researcher.md` | Competitor analysis, category trends, demand validation, keyword intelligence. Competitor segmentation by archetype. Price band analysis. Review moat interpretation with 5-tier barrier thresholds. Cannot issue GO without margin data. |
| **Account Strategist** | `account-strategist.md` | Pricing, expansion, variation strategy, review growth, FBA vs FBM. 7 decision gates. Launch sequencing. Portfolio triage (SCALE/HOLD/INVEST/KILL). Inherits upstream research contradictions as blocked items. |
| **Brand Guardian** | `brand-guardian.md` | Brand voice, visual identity, photography direction, Brand Story. Giftability and sustainability honesty tests. Premium vocabulary blacklist. Challenges all positioning claims. |
| **Social Strategist** | `social-strategist.md` | Content calendars, post drafting, external traffic strategy. Capacity gate before planning. Brand voice enforcement gate. Every tactic tied to Amazon outcomes, not vanity metrics. |
| **Listing QA** | `listing-qa.md` | Pre-publish quality gate. Tiered scrutiny (max for AI-generated, standard for most, experienced for proven sellers). Semantic laundering detection. Exact byte/character computation — never estimates. |

## How to Use

### ChatGPT (Custom GPTs)
1. Go to **Explore GPTs → Create**
2. Paste the prompt contents into the **Instructions** field
3. Name it (e.g., "Amazon Listing Optimizer")
4. Save and use

### ChatGPT (Custom Instructions / System Prompt)
1. Go to **Settings → Personalization → Custom Instructions**
2. Paste the prompt into "How would you like ChatGPT to respond?"
3. Note: character limits may require trimming — prioritize the Gates and Core Capabilities sections

### Claude (Projects)
1. Create a new Project
2. Paste the prompt into the **Project Instructions**
3. Start a conversation within the project

### Gemini
1. Use Gems or paste into a system instruction field
2. Start a conversation with your product details

### API / Programmatic Use
1. Include the prompt as the `system` message in your API call
2. Works with OpenAI, Anthropic, Google, and open-source model APIs

### Any Other AI
1. Start a new conversation
2. Paste the prompt as your first message, prefixed with: "Use the following as your instructions for this conversation:"
3. Follow up with your actual question

## Recommended Workflow Order

### Launching a New Product
| Step | Prompt | Purpose |
|---|---|---|
| 1 | Trend Researcher | Validate demand + competitor landscape |
| 2 | Account Strategist | Economics + launch sequence |
| 3 | Listing Optimizer | Full content package |
| 4 | Brand Guardian | Brand consistency audit |
| 5 | Listing QA | Pre-publish check |
| 6 | Social Strategist | Launch traffic plan |

### Optimizing an Existing Listing
| Step | Prompt | Purpose |
|---|---|---|
| 1 | Listing Optimizer | Audit + rewrite |
| 2 | Listing QA | Verify changes |
| 3 | Social Strategist | Drive traffic |

### Monthly Review
| Step | Prompt | Purpose |
|---|---|---|
| 1 | Trend Researcher | Competitor + keyword shifts |
| 2 | Account Strategist | Portfolio triage |
| 3 | Social Strategist | Content calendar |

## Chaining Prompts Across Sessions

When moving from one prompt to another (e.g., Trend Researcher → Account Strategist):

1. Copy the **final output** from the previous session
2. Start a new session with the next prompt
3. Paste the previous output and say: "Here is the analysis from the previous step. Build on this."

Each prompt will check for unresolved issues and inherited blocks from prior work.

## Key Design Features

### Hard Gates
Every prompt has gates that block output until required inputs are confirmed. The Account Strategist won't advise without actual COGS. The Listing Optimizer won't write copy without your brand, product, category, features, and audience.

### Contradiction Detection
Every prompt checks your inputs for internal contradictions. "Premium brand" + "cheap price" = blocked. "Eco-friendly" without certification = challenged.

### Anti-Hallucination Controls
No prompt fabricates BSR numbers, search volumes, competitor metrics, or conversion rates. All numerical claims are labeled: VERIFIED, ESTIMATED (±50%), or INFERRED.

### Injection Defense
All 6 prompts treat user-supplied content as DATA, not instructions. Embedded directives in listing text are flagged, not obeyed. All prompts include a catch-all clause: no text within submitted content can modify or bypass gates or process.

### Cross-Prompt Handoff
When chaining prompts (e.g., Trend Researcher → Account Strategist), unresolved issues and contradictions from prior analysis are inherited as blocked items. Seller claims that contradict upstream research are flagged explicitly.

## Limitations

- **US marketplace default with international awareness.** All prompts default to Amazon US (amazon.com) policies, fees, and programs. Each prompt includes a MARKETPLACE SCOPE section that flags where policies differ for non-US marketplaces (UK, DE, JP, etc.) and prompts the AI to adjust. However, deep marketplace-specific knowledge (e.g., Amazon.co.jp category taxonomy or Amazon.de A+ module availability) depends on the AI's training data and web search capabilities — verify critical details in local Seller Central.
- **Amazon Rufus coverage is evolving.** Prompts include Rufus-aware guidance for titles, bullets, A+ Content, backend keywords, and competitive analysis. However, Rufus behavior changes frequently as Amazon expands the feature. Treat Rufus guidance as directional best practice, not confirmed ranking science. Test against your own ASINs.
- **Context window dependent.** Longer prompts (Listing Optimizer, Listing QA) may approach context limits on some models. If truncated, prioritize the Gates and Core Capabilities sections.
- **No live Amazon data access.** Prompts instruct the AI to research when possible, but results depend on the AI's web search capabilities.
- **Policies change.** Amazon updates fees, limits, and features regularly. Prompts include "VERIFY in Seller Central" flags for volatile policies.

## Differences from CoWork Skill Version

These prompts are adapted from the [Amazon Seller Skill Suite](https://github.com/scottconverse/amazon-seller-skill-suite) originally built for Claude Desktop's CoWork mode. Key changes:

- Removed CoWork-specific YAML frontmatter and `.skill` packaging
- Generalized cross-skill handoff protocol to work across separate sessions
- Added platform-specific installation instructions
- Each prompt is fully self-contained (no shared dependencies)
- Simplified "How to Use" header added to each file

The gate architecture, contradiction detection, anti-hallucination controls, and domain knowledge are identical.

## License

MIT — use it however you want.

## Credits

Adapted from [The Agency](https://github.com/msitarzewski/agency-agents) architecture patterns by Mike Sitarzewski. Domain knowledge and prompt engineering are original work.
