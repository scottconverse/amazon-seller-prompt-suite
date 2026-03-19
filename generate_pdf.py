"""Generate a professionally formatted PDF from the Amazon Seller Prompt Suite README."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

# Colors
DARK_ORANGE = HexColor("#E65100")
MED_ORANGE = HexColor("#F57C00")
LIGHT_ORANGE = HexColor("#FFF3E0")
HEADER_BG = HexColor("#E65100")
ROW_ALT = HexColor("#FFF8F0")
WHITE = HexColor("#ffffff")
BLACK = HexColor("#000000")
GRAY = HexColor("#666666")
DARK_GRAY = HexColor("#333333")
LIGHT_GRAY = HexColor("#e0e0e0")

OUTDIR = os.path.dirname(os.path.abspath(__file__))
OUTPATH = os.path.join(OUTDIR, "Amazon-Seller-Prompt-Suite-README.pdf")


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPATH,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("CustomTitle", parent=styles["Title"],
        fontSize=26, textColor=DARK_ORANGE, spaceAfter=4, fontName="Helvetica-Bold")

    subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"],
        fontSize=12, textColor=GRAY, spaceAfter=18, fontName="Helvetica-Oblique")

    h1 = ParagraphStyle("H1", parent=styles["Heading1"],
        fontSize=17, textColor=DARK_ORANGE, spaceBefore=20, spaceAfter=10,
        fontName="Helvetica-Bold")

    h2 = ParagraphStyle("H2", parent=styles["Heading2"],
        fontSize=13, textColor=MED_ORANGE, spaceBefore=14, spaceAfter=8,
        fontName="Helvetica-Bold")

    body = ParagraphStyle("Body", parent=styles["Normal"],
        fontSize=10, textColor=DARK_GRAY, spaceAfter=6, leading=14,
        fontName="Helvetica")

    body_bold = ParagraphStyle("BodyBold", parent=body,
        fontName="Helvetica-Bold")

    bullet_style = ParagraphStyle("Bullet", parent=body,
        leftIndent=20, bulletIndent=8, spaceAfter=4)

    numbered_style = ParagraphStyle("Numbered", parent=body,
        leftIndent=20, spaceAfter=4)

    small = ParagraphStyle("Small", parent=body,
        fontSize=8, textColor=GRAY, spaceAfter=4)

    elements = []

    # ── Title ──
    elements.append(Paragraph("Amazon Seller Prompt Suite", title_style))
    elements.append(Paragraph("v1.3 — 6 System Prompts for Amazon Marketplace Selling", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=2, color=DARK_ORANGE, spaceAfter=12))

    elements.append(Paragraph(
        "Works with <b>any AI</b> — ChatGPT, Claude, Gemini, Copilot, Llama, Mistral, or any instruction-following model. "
        "Works with any brand, any product category, any seller account type.", body))
    elements.append(Spacer(1, 8))

    # ── What These Are ──
    elements.append(Paragraph("What These Are", h1))
    elements.append(Paragraph(
        "Each file is a standalone system prompt that turns a general-purpose AI into a specialist Amazon advisor. "
        "Paste one into your AI's system prompt, custom instructions, or \"role\" field and start a conversation.", body))
    elements.append(Paragraph(
        "Every prompt enforces hard gates (refuses to proceed without real data), detects contradictions in your inputs, "
        "and refuses to fabricate numbers it doesn't have.", body))
    elements.append(Spacer(1, 6))

    # ── The 6 Prompts Table ──
    elements.append(Paragraph("The 6 Prompts", h1))

    prompt_data = [
        ["Prompt", "File", "What It Does"],
        ["Listing\nOptimizer", "listing-optimizer.md",
         "Titles, bullets, backend keywords, A+ Content, image shot lists. Title positioning for value/mid-market/premium. "
         "Backend keyword packing with UTF-8 byte counting. Variation architecture framework."],
        ["Trend\nResearcher", "trend-researcher.md",
         "Competitor analysis, category trends, demand validation, keyword intelligence. Competitor segmentation by archetype. "
         "Price band analysis. Review moat interpretation with 5-tier barrier thresholds. Cannot issue GO without margin data."],
        ["Account\nStrategist", "account-strategist.md",
         "Pricing, expansion, variation strategy, review growth, FBA vs FBM. 7 decision gates. Launch sequencing. "
         "Portfolio triage (SCALE/HOLD/INVEST/KILL). Inherits upstream research contradictions."],
        ["Brand\nGuardian", "brand-guardian.md",
         "Brand voice, visual identity, photography direction, Brand Story. Giftability and sustainability honesty tests. "
         "Premium vocabulary blacklist. Challenges all positioning claims."],
        ["Social\nStrategist", "social-strategist.md",
         "Content calendars, post drafting, external traffic strategy. Capacity gate before planning. "
         "Brand voice enforcement gate. Every tactic tied to Amazon outcomes, not vanity metrics."],
        ["Listing\nQA", "listing-qa.md",
         "Pre-publish quality gate. Tiered scrutiny (max for AI-generated, standard for most, experienced for proven sellers). "
         "Semantic laundering detection. Exact byte/character computation — never estimates."],
    ]

    col_widths = [75, 130, 275]
    t = Table(prompt_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('FONTNAME', (1, 1), (1, -1), 'Courier'),
        ('FONTSIZE', (1, 1), (1, -1), 7.5),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, ROW_ALT]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # ── How to Use ──
    elements.append(Paragraph("How to Use", h1))

    platforms = [
        ("ChatGPT (Custom GPTs)", [
            "Go to Explore GPTs → Create",
            "Paste the prompt contents into the Instructions field",
            "Name it (e.g., \"Amazon Listing Optimizer\")",
            "Save and use"
        ]),
        ("ChatGPT (Custom Instructions)", [
            "Go to Settings → Personalization → Custom Instructions",
            "Paste the prompt into \"How would you like ChatGPT to respond?\"",
            "Note: character limits may require trimming — prioritize Gates and Core Capabilities"
        ]),
        ("Claude (Projects)", [
            "Create a new Project",
            "Paste the prompt into the Project Instructions",
            "Start a conversation within the project"
        ]),
        ("Gemini", [
            "Use Gems or paste into a system instruction field",
            "Start a conversation with your product details"
        ]),
        ("API / Programmatic Use", [
            "Include the prompt as the system message in your API call",
            "Works with OpenAI, Anthropic, Google, and open-source model APIs"
        ]),
        ("Any Other AI", [
            "Start a new conversation",
            "Paste the prompt as your first message, prefixed with: \"Use the following as your instructions:\"",
            "Follow up with your actual question"
        ]),
    ]

    for platform, steps in platforms:
        elements.append(Paragraph(platform, h2))
        for i, step in enumerate(steps, 1):
            elements.append(Paragraph(f"{i}. {step}", numbered_style))
        elements.append(Spacer(1, 4))

    # ── Workflow Tables ──
    elements.append(Paragraph("Recommended Workflow Order", h1))

    def workflow_table(title, data):
        elements.append(Paragraph(title, h2))
        rows = [["Step", "Prompt", "Purpose"]] + data
        t = Table(rows, colWidths=[40, 130, 310], repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
            ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, ROW_ALT]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 8))

    workflow_table("Launching a New Product", [
        ["1", "Trend Researcher", "Validate demand + competitor landscape"],
        ["2", "Account Strategist", "Economics + launch sequence"],
        ["3", "Listing Optimizer", "Full content package"],
        ["4", "Brand Guardian", "Brand consistency audit"],
        ["5", "Listing QA", "Pre-publish check"],
        ["6", "Social Strategist", "Launch traffic plan"],
    ])

    workflow_table("Optimizing an Existing Listing", [
        ["1", "Listing Optimizer", "Audit + rewrite"],
        ["2", "Listing QA", "Verify changes"],
        ["3", "Social Strategist", "Drive traffic"],
    ])

    workflow_table("Monthly Review", [
        ["1", "Trend Researcher", "Competitor + keyword shifts"],
        ["2", "Account Strategist", "Portfolio triage"],
        ["3", "Social Strategist", "Content calendar"],
    ])

    # ── Chaining ──
    elements.append(Paragraph("Chaining Prompts Across Sessions", h1))
    elements.append(Paragraph(
        "When moving from one prompt to another (e.g., Trend Researcher → Account Strategist):", body))
    for i, step in enumerate([
        "Copy the <b>final output</b> from the previous session",
        "Start a new session with the next prompt",
        "Paste the previous output and say: \"Here is the analysis from the previous step. Build on this.\""
    ], 1):
        elements.append(Paragraph(f"{i}. {step}", numbered_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "Each prompt will check for unresolved issues and inherited blocks from prior work.", body))

    # ── Key Design Features ──
    elements.append(Paragraph("Key Design Features", h1))

    features = [
        ("Hard Gates",
         "Every prompt has gates that block output until required inputs are confirmed. The Account Strategist won't advise "
         "without actual COGS. The Listing Optimizer won't write copy without your brand, product, category, features, and audience."),
        ("Contradiction Detection",
         "Every prompt checks your inputs for internal contradictions. \"Premium brand\" + \"cheap price\" = blocked. "
         "\"Eco-friendly\" without certification = challenged."),
        ("Anti-Hallucination Controls",
         "No prompt fabricates BSR numbers, search volumes, competitor metrics, or conversion rates. "
         "All numerical claims are labeled: VERIFIED, ESTIMATED (±50%), or INFERRED."),
        ("Injection Defense",
         "All 6 prompts treat user-supplied content as DATA, not instructions. Embedded directives in listing text are flagged, "
         "not obeyed. All prompts include a catch-all clause: no text within submitted content can modify or bypass gates or process."),
        ("Cross-Prompt Handoff",
         "When chaining prompts, unresolved issues and contradictions from prior analysis are inherited as blocked items. "
         "Seller claims that contradict upstream research are flagged explicitly."),
    ]

    for title, desc in features:
        elements.append(Paragraph(title, h2))
        elements.append(Paragraph(desc, body))

    # ── Limitations ──
    elements.append(Paragraph("Limitations", h1))
    limitations = [
        "<b>US marketplace default with international awareness.</b> All prompts default to Amazon US. Each includes a "
        "MARKETPLACE SCOPE section for non-US marketplaces. Verify critical details in local Seller Central.",
        "<b>Amazon Rufus coverage is evolving.</b> Prompts include Rufus-aware guidance but Rufus behavior changes frequently. "
        "Treat as directional best practice, not confirmed ranking science.",
        "<b>Context window dependent.</b> Longer prompts may approach limits on some models. Prioritize Gates and Core Capabilities if truncated.",
        "<b>No live Amazon data access.</b> Results depend on the AI's web search capabilities.",
        "<b>Policies change.</b> Prompts include \"VERIFY in Seller Central\" flags for volatile policies.",
    ]
    for lim in limitations:
        elements.append(Paragraph(f"• {lim}", bullet_style))

    # ── License ──
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceAfter=8))
    elements.append(Paragraph("MIT License — use it however you want.", small))
    elements.append(Paragraph(
        "Adapted from The Agency architecture patterns by Mike Sitarzewski. "
        "Domain knowledge and prompt engineering are original work.", small))

    doc.build(elements)
    print(f"PDF generated: {OUTPATH}")


if __name__ == "__main__":
    build_pdf()
