SP="/tmp/claude-0/-home-user-private/08506865-a31e-5a6b-9772-f4733aaf6b07/scratchpad"
r=open("/tmp/job105-work/WORD-RULINGS-book2-20261102.md",encoding="utf-8").read()
def once(old,new):
    global r
    assert r.count(old)==1, (r.count(old), old[:70]); r=r.replace(old,new)
once("# WORD RULINGS — book 2\n\n**Letter `t`",
 "# WORD RULINGS — book 2\n\n**Letter `u`, cut 2026-11-11 by `Job105 drafting 20261102`.** Supersedes `WORD-RULINGS-book2-20261102.md` (letter `t`); "
 "quarantine the parent. Carries the word rulings `[A]` gave in `Job105`, directly and through `Job99`'s relays of 11-03 to 11-11, each with his words, "
 "in the new §8, *Job105 block*: **relational position** for the relation between two types; **when stress is low** for the direction of integration, and "
 "**shifts a little** for what a person does, with **step** kept for the distance on the cycle; **the caution end** and **the enthusiasm end** for the two ends "
 "of the detached phase only, never a person's lean, with *of the detached phase* in full in every paragraph that uses either; **instinctual fears**; "
 "**worked through** as *what to do about the matter the fear is about* being found; the **arhat** name out of the book; **meet** never with a person meeting a "
 "thing; **secondary fears** credited to Riso and Hudson. Entries in §4, §4a, §5 and §7 that these supersede are marked in place. Eight patterns are added; "
 "each fires on `BOOK2-20261102.md` at the sites it is for and on none of `BOOK2-20261111.md`. The sites are in `CHANGES-job105-20261111.md`.\n\n"
 "*What letter `t` said of itself, retained:* **Letter `t`")
once("Attach\n  *of the detached phase* at the first mention in each section, then the bare form runs (RULED\n  09-13).",
     "Attach\n  *of the detached phase* at the first mention in each section, then the bare form runs (RULED\n  09-13). **SUPERSEDED 2026-11-08, see §8: the ends name the detached phase's ends only, and *of the detached phase* is written in full in every paragraph that uses either end.**")
once("Craving, coveting and hatred involve the will. Every fear has a",
     "Craving, coveting and hatred involve the will. [**SUPERSEDED 2026-11-03, see §8, instinctual fears:**] Every fear has a")
once("wording approved by `[A]` to `Job82` 2026-10-15 (*yes*):** *the thought has found what to do about the fear, so",
     "wording approved by `[A]` to `Job82` 2026-10-15 (*yes*) — **AMENDED 2026-11-08, see §8:** *what to do about the matter the fear is about has been found*; *What is found may be …*. The 10-15 wording, kept for history:** *the thought has found what to do about the fear, so")
once("- **arhat** (was **buddha**) — RULED 2026-10-05 in `Job76`.",
     "- **arhat** (was **buddha**) — **SUPERSEDED 2026-11-07, see §8: the name goes from the book; the person is described without it.** RULED 2026-10-05 in `Job76`.")
block=open(SP+"/close/register-block.md",encoding="utf-8").read()
once("\n---\n\n```patterns\n", "\n"+block+"---\n\n```patterns\n")
once("buddha | \\bbuddh\\w*|\\barhat\\w* | all | arhat, not buddha (RULED 10-05); lower case, class defined first, Part 3 opening only",
     "buddha | \\bbuddh\\w*|\\barhat\\w* | all | RULED 11-07: the name is out of the book; describe the person who has given up all attraction and all aversion")
once("desire | \\bdesir\\w* | all | RULED 10-28: want, everywhere; only 'Riso and Hudson call this want a desire.' and the Naval Ravikant sentence stay",
     "desire | \\bdesir\\w* | all | RULED 10-28: want, everywhere; only 'Riso and Hudson call this want a desire.', the Naval Ravikant sentence, Riso and Hudson's quoted words, and Ch 9's ordinary 'desirable' stay")
pats=open(SP+"/close/register-patterns.txt",encoding="utf-8").read().rstrip("\n")
i=r.index("```patterns\n"); j=r.index("\n```", i+12)
r=r[:j]+"\n"+pats+r[j:]
open(SP+"/close/WORD-RULINGS-book2-20261111.md","w",encoding="utf-8").write(r)
print("ok")
