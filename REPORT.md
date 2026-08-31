# Audit fix report — zeeyadkhan.com

Executed 2026-08-28 against the Aug 28 audit. Nine sections, nine commits (plus one addendum), all local.

**Nothing has been pushed.** The repo deploys on push, and the Legaleey page now contains two visible `[ZEEYAD: ...]` placeholders (section 3). Fill or cut them, review the flagged items below, then push. Every image removed from a page was moved to `archive/` (excluded from deploy along with `tools/`, `drafts/`, and this file via `.vercelignore`), so any cut can be restored.

---

## 1. What changed, per section

### Section 1 — Process book rebuilds (commit `4b5782b` + addendum `121c22a`)
- Explorius 107 → 28 images (1,095 KB), WonderBudi 83 → 28 (1,440 KB), Baloo 79 → 27 (1,283 KB). All under the 30 image / 1.5 MB caps.
- Every title slide, duplicate, and hero repeat cut. Hi fi runs collapsed into grids of paired screens captioned by decision. Every h2/h3 opens with a synthesis sentence before its first image; synthesis sentences use only facts already present in the page's alt text, captions, or prose.
- **Addendum (important):** the deck exports have systematically unreliable filenames and alt text. Every one of the 83 displayed images was read and visually verified. Findings:
  - The Explorius hero was actually the process book's closing "Thank you! From Explorius" slide. Replaced with a crop of the same artwork (logo + "Lets get away" over the crater lake) with the goodbye text removed: `explorius_brand_hero_crater_lake.webp`. The original is in `archive/explorius-photos/`. **Review the crop; if you have a real cover asset, swap it in.**
  - Explorius's six "high fidelity screens" files were mislabeled: files named after app screens contained text slides ("Design Phase", "Features Overview", "Chosen Topic"). The grid now uses the verified real screens: Dashboard (file `events_detail_screen_with_going_interested.webp`), map (`excursion_detail_screen_with_cost_attendees.webp`), Explore split (`itinerary_active_trip_with_stored_travel.webp`), booking flow (`profile_settings_and_visibility_controls.webp`), itinerary (`explore_tab_showing_events_near_current.webp`), profiles (`connection_request_screen_with_nomad_profile.webp`). Filenames no longer describe content; alts now do.
  - Wording corrections across all three pages where alt/caption contradicted the visible artifact (details in §4 and `tools/*-audit.txt`).

### Section 2 — Lumi content bugs (commit `725ec40`)
The "structured extraction" exists as unplaced images in `lumi-photos/`. Core Features (6 labeled items), Evaluation Questions (7 questions from the two Sprint 1 slides), and Goals (3 items) are now rendered as lists using the exact slide content. A small `.content-list` style was added to Lumi's inline stylesheet (blue markers matching the site accent).

### Section 3 — Legaleey precision edits (commit `deec95c`)
- "measurable margin" → placeholder; "high engagement" → placeholder (see §3 below).
- "15 participants, legal professionals and non lawyers" added to At a Glance as a Research line, and to the Research section intro.
- Method phrasing unified in My Role and Research (see §4).

### Section 4 — About page claims (commit `c0bec80`)
- "a series of consumer and wellness products built around ritual and habit" → "two consumer **brand and packaging systems**, Zarrin and Adey", linked to both pages.
- The NOMADO "digital menu system" clause was **cut** because the NOMADO case study is a draft pending your approval, not shipped. When it ships, restore the clause with a link to `/projects/nomado`.

### Section 5 — Professional work (commit `ac0549f`)
- **Git history contains no retired NOMADO or Park North pages or assets.** The repo begins at "Initial portfolio deploy" without them, so there was nothing to restore. Both drafts are built from resume facts only.
- `drafts/nomado/index.html`: full case study on the Legaleey template (Overview, Problem, Research, Principles, Key Flows, Decisions, Outcome, At a Glance). Populated: role, timeline, 10 rounds of usability testing, +30% order completion, −20% user friction, categorization / responsive layouts / branded visuals. Everything else is a placeholder (§3).
- `drafts/parknorth/at-a-glance.html`: At a Glance block only, framed as design system and brand system work per your instruction, using the resume's 20% engagement / 25% inquiries figures. Stopped there.
- Homepage NOMADO card staged at position 02, commented out, with enable instructions in the comment (renumber or drop a student project — your call).

### Section 6 — Technical fixes (commit `c470572`)
- **a.** Width/height attributes injected on every img site wide from intrinsic pixel dimensions (`tools/inject_dims.py`, sips). All image contexts have CSS `width: 100%` (or `object-fit`) with `height: auto`, so attributes only reserve aspect ratio.
- **b.** One `<main>` landmark per page. About/Contact/404 wrap divs converted; homepage and Explorations content wrapped in a new `<main>`.
- **c.** Skip link first in body on all 16 pages → `#main-content` (`tabindex="-1"`), visually hidden until focused (`.skip-link` in main.css).
- **d.** `assets/js/lightbox-a11y.js` shared across the 11 project pages: dialog role/aria-modal/label where missing (Lumi's dynamic overlay), focus moves to close on open, Tab trapped, focus returned to the opening thumbnail. Alt was already copied by every page's own script. All four lightbox variants tested in Playwright.
- **e.** JSON LD Person on homepage and About: name, jobTitle AI Product Designer, url, sameAs LinkedIn, locality San Francisco. No email, no phone. Validates.
- **f.** Plausible snippet on all 16 pages. **There is no shared head include, so the snippet is duplicated per file** (as is all head markup on this site).
- **g.** Playwright verification of every page at 390 and 1280: no overflow, no console errors. One real offender found and fixed: the WonderBudi hero title (one unbreakable 10 character word at the 4rem clamp minimum) overflowed below 480px; scoped title clamp added in that page's own style block. Adey and Zarrin untouched.

### Section 7 — Footer and contact path (commit `f90d101`)
- Footer on all 16 pages: email and LinkedIn anchors in the existing footer text style, stacked under the right column, left aligned when the footer stacks on phones.
- Homepage closes with "I am open to full time roles. Say hello" linking to /contact, in the same rhythm as the Explorations bridge line.

### Section 8 — Resume PDF
No source found in the repo or its history (only the exported PDF). **Not touched.** Manual item in §5.

### Section 9 — Copy consistency (commit `cd85283`)
65 hyphenated compounds split or rephrased across the five case studies that used them (the four tool pages, Adey, and Zarrin were already clean). Em dashes in Lumi captions became commas; one soft hyphen removed. Alt text quoting slides, file paths, URLs, and code untouched. **USB-C kept** on Baloo: it is the standard's name and "USB C" would misspell it.

---

## 2. Keep and cut lists

### Explorius — kept 28
Hero (cropped brand art) · research methods slide (2 surveys / 73 / 15 / 4) · 60% non nomads chart · nomad interview quote board · affinity map (416/46/20/6) · Ryan persona · Marley persona · HMW board · competitive positioning chart · concept 1 features diagram · concept 2 community board · merged concepts visual · brand identity · card sort "People Want" board · site map · six verified hi fi screens (Dashboard, map, Explore split, booking flow, itinerary, profiles) · testing: lo fi Explore before + updated after, lo fi Dashboard before + updated after, old nav + new nav · Business Model Canvas.

Cut (79), one line each:
- `process_book_cover_slide_with_a` — cover slide, decorative
- `topic_of_interest_fixing_pain_points` — text slide; overview prose states it
- `research_executive_summary_2_surveys_73` — duplicate numbers of the kept methods slide
- `secondary_research_section_title_over_a` / `_2` — two consecutive title slides
- `49_increase_in_the_amount_of` — the 49% figure already lives in Problem prose
- `how_long_do_they_travel_for` — secondary chart; trip length not load bearing to the narrative
- `primary_research_section_title_over_a` — title slide
- `research_goals_understand_nomad_trip_planning` — goals list slide; rendered as the synthesis sentence
- `survey_data_section_title_over_a` — title slide
- `how_do_you_feel_while_working` — survey chart; its 30%/20% numbers moved into the Survey Data synthesis sentence, kept the 60% chart as the one survey artifact
- `nomad_quote_i_feel_more_isolated` — quote covered by the kept interview quote board
- `non_nomad_quote_i_like_having` + `_2` — duplicate pair (identical content, two files)
- `88_of_non_nomads_like_to` — number moved to prose; 60% chart is the keeper
- `interview_data_section_title_over_a` — title slide
- `non_nomad_interview_quotes_would_like` — second quote board; findings moved into the Interview synthesis sentence
- `affintization_section_title_over_a_joyful` — title slide
- `main_insights_nomads_love_the_freedoms` — text slide; insights live in prose and captions
- `target_audience_25_to_55_year` / `archetypes_wants_to_be_a_digital` / `extreme_cases_diagram_two_axes_showing` — audience covered by the persona set; heading removed
- `marley_s_experience_section_title_over` — title slide
- Marley scenario slides ×6 (`marley_is_currently…`, `she_has_been…`, `she_has_attempted…`, `marley_procrastinates…`, `marley_also_has…`, `marley_wants_to…`) — six text slides collapsed into one narrative paragraph
- `concept_1_section_title_over_a` / `concept_2_section_title_over_a` — title slides
- `find_your_plan_pick_all_aspects` — concept 1 text slide; features diagram is the keeper
- `insights_from_comparing_both_concepts_being` — text slide; convergence sentence covers it
- `planning_or_connection_decision_diagram` — near duplicate of the kept merged concepts visual
- `competitive_position_chart_showing_explorius_in` — duplicate of the kept positioning chart
- Feature definition cards ×5 (`map_that_shows_location…`, `map_that_shows_close_by…`, `easily_find_free_events…`, `book_nearby_excursions…`, `let_nomads_connect…`) — five text cards rendered as one sentence listing the five features
- Rory slides ×7 (`rory_s_story_section_title…` + six scenario slides) — the section's two paragraphs narrate the scenario
- `branding_section_title_over_a_woman` — title slide
- `concept_validation_section_title_over_two` — title slide
- `card_sorting_20_open_card_sort` — method numbers moved to the synthesis sentence; findings board kept
- `site_map_section_title_over_travelers` — title slide
- `ideating_wall_of_sticky_notes_exploring` — process shot; cut for the 30 cap, ideation named in the Two Concepts sentence
- Hi fi run ×19 originally named (`explorius_onboarding_profile_setup`, `dashboard_showing_close_by_nomads_and`, `dashboard_notifications_and_upcoming_events_modules`, `map_view_with_public_nomads_visible`, `explore_tab_showing_bookable_excursions`, `itinerary_showing_upcoming_trips_and_saved`, `itinerary_past_trips_view`, `messaging_thread_between_two_connected_nomads`, `explore_destinations_tab_with_curated_city`, `explore_partnerships_tab_with_premium_experience`, `onboarding_travel_style_and_preference_selection`, `map_view_showing_nomad_cluster_in`, `excursion_booking_confirmation_screen`, `itinerary_event_added_confirmation`, `explorius_home_screen_after_full_onboarding`, plus the three text slides masquerading as screens: `dashboard_with_all_four_utility_modules`, `map_view_in_stealth_mode_with`, `profile_page_with_connections_list_and`) — 25 screen run collapsed to the six that map to the Decisions section; several of these files are actually text slides or flow fragments (see addendum)
- `explorius_logo_over_a_volcanic_crater` ×3 uses — hero repeat in hi fi and closing; the file itself is the goodbye slide, replaced by the crop
- `lo_fi_and_user_testing_section` — title slide
- `explore_users_said_we_needed_a` / `dashboard_users_said_the_dashboard_was` — board images duplicated verbatim by the adjacent callout quotes
- `updated_excursions_screens_showing_marriot_pool` — redundant with the updated Explore screens and the kept booking flow
- `navigation_feedback_users_said_navigation_was` — quote board replaced by a matching callout
- `travel_photo_collage_showing_diverse_groups` — decorative closing collage

### WonderBudi — kept 28, cut 54 (agent executed, verified in the addendum)
Kept: hero banner · 1 in 5 stat · participants breakdown (4/5/5/2, 16 interviews, 22 insights) · child trauma quote board · 50 of 52 parents survey card · 763 point affinity map · Tommy + Peter personas · Tommy's journey map · concept 1 vs concept 2 boards · emoticon scale + routing outcomes storyboards · robot with Budibands intro · nine step flow · session steps 4–5 and 6–8 · anger voice script · Budiband hardware slide · parent app: trips + counselor notes, health status, dashboard, settings · card sorting observation photos · card sort results (100% biometrics) · 5 category grouping dendrogram · tree test results (90%/75%) · core values diagram.

Cut, by reason: 1 hero repeat; 3 title slides (`primary_research_and_affinitization_section_divider`, `personas_and_user_journeys_section`, `final_deliverables_section`); ~24 text slides whose content the prose already states (`children_may_not_recognize…`, `there_are_too_many_students…`, `current_problems…`, `problem_statement…`, `what_is_a_mandated_reporter…`, `in_regard_to_mental_health…`, `insights_from_secondary_research…`, `affinity_mapping_process…`, `how_might_we_statements…`, `overarching_how_might_we…`, `pivot_from_adolescent…`, `the_last_thing_schools_needed…`, `solution_a_device…`, `wonderbudi_is_not_an_everyday…`, `what_we_know…`, `what_we_need…`, `expected_outcomes…`, `final_solution_statement…`, `wonderbudi_ecosystem_before…`, `what_happens_in_school_step_1`, `six_educators_and_counselors…`, `user_testing_methods…`, `user_test_1_closed…`, `user_test_2_open…`); duplicates and second-of-pair artifacts (`secondary_research_nearly_a_third`, `only_31_of_public_schools`, `findings_from_survey…`, two extra quote boards, `overall_insights…`, `peter_s_journey_map`, `archetype_table…`, `wonderbudi_components_list…`, `budiband_detail…`, `wonderbudi_parents_companion_app…`, `card_sorting_results_the_word…`, `wonderbudi_final_product_shot…`, `wonderbudi_manufacturing_components…`, `wonderbudi_ecosystem_overview…`, `potential_storylines_three…` on Baloo's pattern); collapsed runs (3 storyboard setup slides, 2 session step slides, 2 chat scenarios, hi fi app overview); `crazy_8_ideation_exercise` (heaviest file; decision carried by the concept pair — restore if you prefer the sketches over the weight budget, page goes to ~1.56 MB); `business_model_canvas` (pricing survives in Future Directions — flag if you want it back).

### Baloo — kept 27, cut 51 (agent executed, verified in the addendum)
Kept: hero (bear + app) · 63% screen time stat · 33% distraction pie · Parent 1 quotes · emotion timeline · cultural probe kit · affinity map · Cindy persona + journey map · Bethany persona · Codi capabilities · Snappy + Tori concept diagrams · 3 ways decision tree · storyboard panels · initial sketches · charging illustrations · parent app library + settings pair · round 1 + round 2 feedback · four storyline branches · mid fi insights · narrowed form · six color variations · finalized form · final product photo.

Cut, by reason: cover/closing posters (2, duplicate hero content); topic and process slides (`chosen_topic…`, `project_approach_10_week_gantt`, `introduction…`, `initial_topics…`, `technology_s_negative_effects…`, `user_group…`, `topic_of_interest…`); method description text slides (~10: survey, interviews, observation, probes, affinity, archetypes/personas, competitive, lo fi testing ×2, `questions_to_answer`); second-of-pair artifacts (`opinion_of_parents…` weaker stat chart, `results_children_s_screen_time` second survey chart, `user_interviews_insights_wall` duplicate affinity, three extra parent quote boards, `participants_…photo grid` decorative, `korean_version…` duplicate kit, Andrew and Lucia persona + journey duplicates of Cindy, `archetype_table…`, `codi_an_ai_learning_system` duplicate, YouTube ×2 and Woobo ×2 competitor slides collapsed into prose, `potential_storylines_three…` duplicate of detailed branches, `main_features_compared…`, `why_baloo…`, `snappy_transition…`/`tori_reduce…` text versions of kept diagrams, `baloo_eliminate…` concept text); collapsed app wireframe run (2); insight text slides whose content lives in cards/prose (~5); `business_model_canvas` (heavy text canvas; $300 tier survives in Future Directions); hero repeat (1).

---

## 3. Placeholders to fill (one pass)

**Live pages (blockers before push):**
1. `projects/legaleey/index.html`, drop zone caption: "Side by side testing showed the circular variant reduced time to first upload by **[ZEEYAD: exact figure or percentage]**." — If you have no figure, delete this whole sentence; the first sentence of the caption stands alone.
2. `projects/legaleey/index.html`, Outcome insight card: "The persistent filter panel saw **[ZEEYAD: engagement figure]**." — If no figure, delete this sentence; the observation sentence after it stands alone.

**Draft page (not deployed):** `drafts/nomado/index.html` —
3. Hero image (no NOMADO assets exist in the repo).
4. Overview: what NOMADO is as a business, who the customers are, state of the product on arrival.
5. My Role: who else was involved; owned vs directed.
6. Platform: where the menu ran (tablets, QR, web, kiosk).
7. Problem: one line problem statement (h2) + what was broken, any baseline numbers.
8. Research: participants per round, who they were, tasks, publishable verbatims (nothing under NDA).
9. Principles: h2 + one sentence rationale per principle.
10. Key Flows: names of the flows + screen exports.
11. Decisions: the two or three before/feedback/after decisions.
12. Outcome: how the 30%/20% were measured, what happened after launch.

---

## 4. Flagged for your review

1. **Lumi goals wording.** The audit suggested "stop the escalation, build coping methods, understand emotional patterns over time." The actual studio slide (`lumi-photos/our_goals_stop_the_escalation_of.png`) says: **Stop** the escalation of the anger · **Build** an empathetic relationship with the robot · **Understand** the patterns of anger within themselves and others. I rendered the slide's wording, not the suggestion — goal two differs materially ("empathetic relationship with the robot" vs "coping methods"). Confirm.
2. **Legaleey method wording.** Both My Role and Research now say "interviews and observation sessions with 15 legal professionals and non lawyers" (Research adds "supported by secondary research" to preserve that fact). Confirm this matches what actually happened.
3. **NOMADO draft** (`drafts/nomado/index.html`) and the commented homepage card. Approve, fill placeholders, then: move to `projects/nomado/`, restore its canonical/OG tags, add to sitemap, uncomment the card, renumber or drop a student project, add a thumbnail, and relink the About clause.
4. **Park North At a Glance draft** (`drafts/parknorth/at-a-glance.html`), framed as system work. Your call whether it ships at all.
5. **Explorius hero crop** — a derivative I generated (goodbye text cropped off the closing slide). Replace with a real cover export if one exists.
6. **Questionable outcome slide, not used:** `archive/explorius-photos/dashboard_notifications_and_upcoming_events_modules.webp` is titled "The Solution: Key Usability Challenges" and carries outcome stats (completion 52%→86%, time on task −40%, errors −50%, trust 3.1→4.4, engagement +32%, cognitive load −28%). Its visual style doesn't match the rest of the deck and it's written in first person singular for a five person team project. I did not surface these numbers anywhere. If they're real, they belong in the Outcome section; confirm their provenance first.
7. **WonderBudi Crazy 8 sketches and both Business Model Canvases** were cut for the caps; restorable from `archive/` (WonderBudi goes ~60 KB over the 1.5 MB target if the sketches return).
8. **USB-C** kept as spelled on Baloo (standard's name); the style rule was applied everywhere else.

---

## 5. Manual items (only you can do these)

1. **Resume PDF** — the source is not in the repo (only the exported PDF; git history has nothing else). Edit your source document and re-export to `/Zeeyad_Khan_Resume.pdf` (same path and filename):
   - Title: "Product Designer | AI Design Specialist" → **AI Product Designer**.
   - Tools line: remove **Adobe XD, Sketch, InVision, Principle, Balsamiq**; add **Relume** and **HTML and CSS** so it matches the About page (Figma, Framer, Claude Code, Adobe Firefly, Illustrator, Photoshop, After Effects, Premiere Pro, Webflow, Squarespace, Miro, Notion, WordPress, JavaScript, Relume, HTML and CSS).
   - The Legaleey 15 participant bullet now matches the site — no change needed there.
2. **Plausible account** — create the site `zeeyadkhan.com` at plausible.io. The snippet is already on every page; it does nothing until the account exists.
3. **Push to deploy** — after filling/cutting the two Legaleey placeholders and reviewing §4. Everything is committed locally in section order.

---

## 6. Verification checklist results

Run on all 16 HTML pages (the audit's 15 sitemap pages plus the designed 404), locally served, headless Chromium (Playwright) for the browser checks.

| Check | Result |
|---|---|
| Exactly one h1 per page | PASS — 16/16 |
| One main landmark; skip link is first focusable | PASS — 16/16; verified by tab order test on project pages |
| Every img has alt, width, height | PASS — the only alt less imgs are the empty `src=""` lightbox holders that receive src and alt from JS at open; no decorative empty alts exist |
| No orphan headings (h2/h3 followed by heading or section end) | PASS — 0 found |
| Explorius / WonderBudi / Baloo ≤ 30 images and < 1.5 MB | PASS — 28 / 1,095 KB · 28 / 1,440 KB · 27 / 1,283 KB |
| No horizontal overflow at 390px | PASS — all 16 pages; rebuilt pages also pass at 320 and 375 |
| No console errors on load | PASS — all 16 pages at 390 and 1280 |
| Sitemap and canonicals unchanged and valid | PASS — zero diff on sitemap.xml/robots.txt since start; sitemap parses; 15 URLs each matched by a canonical |
| JSON LD validates as Person | PASS — homepage and About parse; jobTitle AI Product Designer; no email/phone present |
| No hyphens or em dashes in prose copy | PASS — one deliberate exception: USB-C on Baloo (standard name, flagged in §4); code blocks, URLs, and alt text quoting slides exempt per instructions |
| Desktop regression (1280/1440) | PASS — all pages; rebuilt pages spot checked visually |

Audit trail: `tools/explorius-audit.txt`, `tools/wonderbudi-audit.txt`, `tools/baloo-audit.txt` (per image visual verification), `tools/verify_checklist.py` (re-runnable), cut lists in `tools/*-cuts.txt`.
