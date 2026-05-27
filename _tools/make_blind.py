"""
make_blind.py — Strip author details for double-blind review
Creates: MANUSCRIPT_DRAFT_v0.1_BLIND.md + TITLE_PAGE.md
"""
import re

src = r'D:\Yoka\Workspace\Provolution-main\10_ENGLISH\MANUSCRIPT_DRAFT_v0.1.md'
blind_out = r'D:\Yoka\Workspace\Provolution-main\10_ENGLISH\MANUSCRIPT_DRAFT_v0.1_BLIND.md'
title_out = r'D:\Yoka\Workspace\Provolution-main\10_ENGLISH\TITLE_PAGE.md'

with open(src, encoding='utf-8') as f:
    content = f.read()

# Extract author block (between first --- and ## Abstract)
author_block_match = re.search(
    r'(\*\*Draft v0\.1.*?\*\*\n\n---\n\n)(.*?)(\n---\n\n## Abstract)',
    content, re.DOTALL
)

author_block = author_block_match.group(2).strip() if author_block_match else ""

# Create blind version — replace author block
blind = re.sub(
    r'(\*\*Draft v0\.1.*?\*\*\n\n---\n\n).*?(\n---\n\n## Abstract)',
    r'\1**[Author details removed for blind peer review]**\2',
    content, flags=re.DOTALL
)

# Also anonymize any self-references in body (GitHub URL, framework name is ok, author name is not)
blind = blind.replace('Yoka Tobias Dietz', '[Author]')
blind = blind.replace('yokadeeds-dev@provolution.org', '[contact removed]')
blind = blind.replace('ORCID: 0009-0006-2349-9002', '')
blind = blind.replace('Independent Researcher, Hamm (Westfalen), Germany', '[Affiliation removed]')
blind = blind.replace(
    'https://github.com/yokadeeds-dev/Provolution',
    '[Repository URL withheld for blind peer review — available upon request or post-acceptance]'
)

with open(blind_out, 'w', encoding='utf-8') as f:
    f.write(blind)
print(f'Blind manuscript: {blind_out}')

# Create title page
title_page = f"""# TITLE PAGE — Author Details

**Title:**
Probatio Systemica & Provolution: A Systematic, Quantified Framework for Climate Transformation

**Draft:** v0.1 — 2026-04-18

---

**Author:**
Yoka Tobias Dietz
ORCID: 0009-0006-2349-9002
Contact: yokadeeds-dev@provolution.org

**Affiliation:**
Independent Researcher, Hamm (Westfalen), Germany

---

**Competing Interests:** None declared.
**Funding:** Self-funded / independent research.
**Data Availability:** All data, formulas, and application templates available at https://github.com/yokadeeds-dev/Provolution (CC0 1.0).

---

**Corresponding Author:**
Yoka Tobias Dietz
yokadeeds-dev@provolution.org
"""

with open(title_out, 'w', encoding='utf-8') as f:
    f.write(title_page)
print(f'Title page: {title_out}')
