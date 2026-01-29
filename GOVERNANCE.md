# CATERYA Governance Framework

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

---

## Founding Principles

CATERYA is governed by the following immutable principles:

1. **Open by Default**: All code, metrics, datasets, and decisions are public unless privacy/security requires otherwise
2. **Community-Driven**: No single entity, corporation, or individual can unilaterally control the project
3. **Scientific Rigor**: Decisions are grounded in evidence, reproducible experiments, and peer review
4. **Anti-Capture**: Active resistance to domination by commercial or political interests
5. **Inclusive Participation**: Expertise valued over credentials, contributions over affiliations

These principles exist to prevent scenarios where ethical AI evaluation becomes a tool of centralized power.

---

## Governance Structure

### Phase 1: Founding (2025)

**Current Status**: Benevolent Dictatorship with Path to Democracy

**Leadership**: Ary HH (Founder & Lead Maintainer)

**Decision Authority**: 
- Architecture and core metrics design
- Accepting/rejecting major contributions
- Setting strategic direction (with community input)

**Accountability**:
- All decisions documented in GitHub Discussions
- Monthly transparency reports on project status
- Open roadmap with community voting

**Rationale**: Early-stage projects need coherent vision. Founder maintains veto power to prevent mission drift while building community capacity for shared governance.

---

### Phase 2: Community Stewardship (2026-2027)

**Trigger**: When project reaches 1,000+ GitHub stars, 100+ contributors, or 50+ production deployments (whichever first)

**Transition Plan**:

1. **Formation of Steering Committee**
   - 5-7 members elected by contributor community
   - Includes: Founder (permanent seat), 2 technical leads, 2 ethics/domain experts, 1-2 community representatives
   - Terms: 2 years, staggered (half elected each year)
   - Elections: Annual, via GitHub Discussions + ranked-choice voting

2. **Decision-Making Process**:
   - **Minor Changes** (bug fixes, documentation): Any maintainer can merge
   - **Major Changes** (new metrics, API changes): Requires 2 Steering Committee approvals
   - **Strategic Decisions** (licensing, partnerships, funding): Requires Steering Committee majority + community comment period (2 weeks)

3. **Conflict Resolution**:
   - Steering Committee votes (simple majority)
   - Founder retains tie-breaking vote until Phase 3
   - Appeals to community via RFC (Request for Comments) process

---

### Phase 3: Foundation Model (2027+)

**Trigger**: When annual budget exceeds $500K, or project achieves regulatory/institutional adoption

**Structure**: Non-profit foundation (501(c)(3) in US, or equivalent)

**Board Composition**:
- 9-11 members
- 1/3 elected by technical contributors
- 1/3 elected by organizational adopters (universities, NGOs, companies)
- 1/3 appointed for domain expertise (ethics, law, physics, AI safety)

**Powers**:
- Manage finances and fundraising
- Set high-level strategy
- Hire/manage staff (if any)
- Protect intellectual property and trademarks

**Constraints**:
- Cannot change core open-source license
- Cannot sell exclusive rights or create closed-source forks
- Must maintain public transparency (annual reports, audited finances)

**Advisory Councils**:
- **Technical Council**: Architecture, implementation, metrics validation
- **Ethics Council**: Value alignment, cultural sensitivity, impact assessment
- **Industry Council**: Adoption, integration, standards harmonization

---

## Decision-Making Processes

### 1. Request for Comments (RFC)

For significant changes requiring community input.

**Process**:
1. Create GitHub Discussion with `[RFC]` tag
2. Structured template: Problem, Proposal, Alternatives, Impact, Timeline
3. Open comment period (minimum 2 weeks)
4. Steering Committee reviews feedback, makes decision
5. Decision documented with rationale

**Examples of RFC-worthy topics**:
- Adding/removing core metrics
- Changing evaluation methodology
- Major API redesigns
- Partnerships with external organizations
- Funding/revenue models

---

### 2. Consensus-Based Development

For technical contributions (code, metrics, documentation).

**Process**:
1. Contributor opens Pull Request (PR)
2. Automated tests + code review (2 maintainers)
3. Community feedback period (3-7 days for major PRs)
4. Merge if: Tests pass + 2 approvals + no blocking objections

**Blocking Objections**:
- Must include technical/ethical rationale (not mere preference)
- Can be overridden by Steering Committee if deemed obstructive
- Rare: Culture of constructive criticism, not gatekeeping

---

### 3. Contributor Ladder

Transparent path from user to maintainer.

**Roles**:

| Role | Requirements | Permissions |
|------|--------------|-------------|
| **User** | Anyone using CATERYA | Read access, file issues, comment |
| **Contributor** | 1+ merged PR | Credit in AUTHORS, voting in community polls |
| **Reviewer** | 5+ quality PRs + nominated | Review PRs, influence decisions |
| **Maintainer** | 20+ PRs + Steering Committee approval | Merge PRs, triage issues, release management |
| **Steering Committee** | Election or appointment | Strategic decisions, represent project externally |

**Demotion/Removal**:
- Inactivity (6+ months) → Emeritus status (honorific, no permissions)
- Code of Conduct violations → Suspension or ban (Steering Committee decision)
- Bad-faith contributions → Warning, then removal

---

## Financial Governance

### Revenue Sources (Future)

1. **Open-Core SaaS** (see VISION.md): Premium services, always with open-source fallback
2. **Grants**: Research institutions, foundations (e.g., NSF, EU Horizon, Mozilla)
3. **Donations**: GitHub Sponsors, OpenCollective
4. **Partnerships**: Joint development with aligned organizations

### Spending Principles

1. **Core Development** (50%+): Maintainers, infrastructure, security audits
2. **Community Growth** (20-30%): Events, workshops, documentation
3. **Research** (10-20%): Academic collaborations, dataset creation
4. **Operations** (5-10%): Legal, accounting, administration

### Transparency Requirements

- Quarterly financial reports (public)
- Annual audited statements (once budget >$100K)
- All expenditures >$10K pre-announced to community
- No individual compensation exceeding nonprofit market rates

---

## Anti-Capture Safeguards

### 1. Licensing Immutability

**Rule**: Core framework must remain Apache 2.0 (or more permissive). Cannot be relicensed to proprietary.

**Enforcement**: Requires unanimous Steering Committee + 2/3 contributor supermajority.

**Rationale**: Prevents acquirer-buys-project-then-closes-it scenario.

---

### 2. Trademark Protection

**Rule**: "CATERYA" trademark held by foundation/community, not individuals or corporations.

**Allowed Uses**:
- Open-source forks (with attribution)
- Educational and research purposes
- Nonprofit deployments

**Prohibited Uses**:
- Proprietary derivatives claiming CATERYA brand
- Misleading endorsements ("CATERYA-Certified" without compliance)

**Enforcement**: Legal action if necessary (funded by foundation).

---

### 3. Conflict of Interest Policy

**Disclosure Required**:
- Employment by AI companies
- Consulting relationships with evaluated entities
- Financial stakes in competing projects

**Management**:
- Recuse from decisions where conflict exists
- Public disclosure in relevant discussions
- Steering Committee can bar participation if unmanageable

---

### 4. Fork-Friendly Architecture

**Design Principle**: Make forking easy, not punitive.

**Implementation**:
- Modular codebase (swap components without rewriting)
- Comprehensive documentation (enable independent development)
- No DRM, API keys, or phone-home mechanisms
- Encourage derivatives (they validate our approach)

**Rationale**: If we go off-mission, community can fork without fracturing ecosystem.

---

## Communication Channels

### Public Forums

1. **GitHub Discussions**: Primary venue for proposals, debates, announcements
2. **Discord/Slack** (Future): Real-time chat for contributors
3. **Mailing List** (Future): Low-traffic, important updates only
4. **Blog** (Future): Tutorials, case studies, research findings

### Private Channels

**Use Only For**:
- Security vulnerabilities (responsible disclosure)
- HR/personnel issues
- Legal consultations

**Transparency Commitment**: Summaries (redacted if needed) posted publicly after resolution.

---

## Code of Conduct

### Standards

We are committed to providing a welcoming, respectful, and harassment-free environment.

**Expected Behavior**:
- Respectful disagreement and constructive criticism
- Acknowledging contributions and giving credit
- Focusing on what is best for the community
- Showing empathy toward other community members

**Unacceptable Behavior**:
- Harassment, discrimination, or derogatory comments
- Personal attacks or ad hominem arguments
- Trolling, baiting, or deliberate misinformation
- Revealing others' private information without consent

### Enforcement

**Process**:
1. Warning (private message from maintainer)
2. Temporary suspension (1 week to 1 month)
3. Permanent ban (for severe or repeat violations)

**Appeals**: To Steering Committee (if not involved) or independent mediator.

**Transparency**: Anonymized summaries of incidents published quarterly.

---

## Amendment Process

This governance document can be amended via:

1. **RFC Process**: Propose changes in GitHub Discussions
2. **Community Feedback**: Minimum 4-week comment period
3. **Approval**: 
   - Phase 1: Founder decision (with strong community consensus)
   - Phase 2: Steering Committee 2/3 majority
   - Phase 3: Board of Directors 2/3 majority + community advisory vote

**Immutable Principles**: Founding Principles (top of document) require unanimous Steering Committee/Board + 75% contributor supermajority.

---

## Transition Plan (Founder → Community)

**Ary HH's Commitment**:

As founder, I commit to:
1. Actively building community capacity for self-governance
2. Transferring knowledge, not hoarding authority
3. Stepping back as community matures (no permanent dictatorship)
4. Remaining available as advisor/contributor after transition

**Timeline**:
- 2026: Build contributor base, establish norms
- 2027: Form Steering Committee, delegate decisions
- 2028: Establish foundation (if needed), transition complete

**Measures of Success**:
- Steering Committee makes >50% of decisions without founder involvement
- Community sustains development during founder's absence (sabbatical test)
- No single point of failure in project leadership

---

## Inspiration

This governance model draws from:
- **Linux Kernel**: Meritocracy + benevolent dictator transition
- **Python (PEP process)**: Structured decision-making with community input
- **Rust Foundation**: Balancing corporate sponsors with community control
- **Mozilla**: Public benefit mission + sustainable revenue
- **Wikimedia**: Transparent finances, global participation

We learn from their successes and failures.

---

## Final Word

Governance is not bureaucracy for its own sake. It is **how we embody our values in practice**.

If CATERYA succeeds, it will wield influence over AI development worldwide. That power must be checked, balanced, and accountable—not to shareholders, not to governments, but to the global community we serve.

This document is our promise to do so.

---

**Questions? Join the discussion**: [GitHub Discussions](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/discussions)

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Next Review**: July 2026
