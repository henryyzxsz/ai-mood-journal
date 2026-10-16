# Methods (draft for your revision)

*First pass from your study design and repo setup. Rewrite in your own words before any UC application or paper submission.*

## Participant

This was a single-subject (N-of-1) longitudinal study. The participant was one high school student who designed the protocol, produced a short journal entry each day, and completed daily self-ratings of mood.

## Materials

**Daily journal.** Each day the participant wrote a brief free-text entry (about 3 to 5 sentences) describing events and feelings from that day. Entries were kept in the participant's own wording, with only typo fixes, so automated scoring would not be skewed by later polishing.

**Self-reported affect (PANAS-style).** Each day the participant rated 20 emotion words on a 1 to 5 scale (1 = very slightly or not at all, 5 = extremely). Ten words formed a positive-affect set (interested, excited, strong, enthusiastic, proud, alert, inspired, determined, attentive, active). Ten words formed a negative-affect set (distressed, upset, guilty, scared, hostile, irritable, ashamed, nervous, jittery, afraid). Daily positive and negative scores were the sums of each set (possible range 10 to 50 for each).

**Automated sentiment.** Each journal entry was scored with VADER (Valence Aware Dictionary and sEntiment Reasoner). The analysis used VADER's compound score, which ranges from -1 (most negative) to +1 (most positive).

**Data storage.** Entries were stored in a public project repository (`dataset/entries.csv`) with fields for day number, date, journal text, positive PANAS sum, negative PANAS sum, and AI compound score.

## Procedure

Data collection was planned for 40 days (October 11 through November 20, 2026). Each evening the participant completed (1) the journal entry and (2) the 20 emotion ratings. The entry was then scored with VADER and appended to the dataset. A mid-study look at the accumulating data was planned around November 8. After collection ended, planned analyses included the association between the AI compound score and a self-report mood index (for example, positive minus negative PANAS), plus a time-series chart of both measures.

## Planned analysis

After data collection, scripts in `analysis/` will load `dataset/entries.csv`, compute the correlation between `ai_score` and a PANAS-derived mood index, and save a figure to `analysis/chart.png`. Results will be reported in the manuscript Results section.

## Status of this draft

- Matches the README research question and measures as of the draft date.
- Does not invent citations; add APA references (PANAS, VADER) when you revise.
- Update the exact start date, any missed days, and analysis details once collection is further along.
