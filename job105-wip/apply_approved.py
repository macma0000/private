"""Rebuild the working master from BOOK2-20261102.md plus every change [A] has approved in Job105.

Each change is found by its words, never by line number, and must match exactly once.
"""
import sys

SRC = "/tmp/job105-work/BOOK2-20261102.md"
PROP = "/tmp/job105-work/PROPOSED-openings-job105-20261102.md"
SP = "/tmp/claude-0/-home-user-private/08506865-a31e-5a6b-9772-f4733aaf6b07/scratchpad"
OUT = SP + "/working/BOOK2-working.md"

t = open(SRC, encoding="utf-8").read()
prop = open(PROP, encoding="utf-8").read().split("\n")


def unbracket(s):
    s = s.strip()
    assert s.startswith("[") and s.endswith("]"), s[:60]
    return s[1:-1]


def once(old, new, label):
    global t
    n = t.count(old)
    if n != 1:
        sys.exit(f"{label}: expected 1 match, found {n}")
    t = t.replace(old, new)


def insert_after_heading(heading, text, label):
    once(heading + "\n\n", heading + "\n\n" + text + "\n\n", label)


# Part 1's opening (pilot, approved 11-02): three paragraphs, proposals lines 73-77.
part1 = "\n".join(prop[72:77])
part1 = part1[1:] if part1.startswith("[") else part1
part1 = part1[:-1] if part1.endswith("]") else part1
insert_after_heading("# Part 1 — The Model", part1, "Part 1 opening")

# Chapter 1's opening (pilot, approved 11-02).
insert_after_heading("## Chapter 1: A New Theory of the Enneagram", unbracket(prop[100]), "Chapter 1 opening")

# Chapter 2's opening (11-03) and the Overview change at line 100 (11-03).
insert_after_heading("## Chapter 2: The Nine Enneagram Types — Profiles and Self-Perception", unbracket(prop[156]), "Chapter 2 opening")
once("This chapter gives each type's story in its own voice, followed by what that type usually cannot see about itself. If you don't yet know your own type, this is the place to look for yourself.",
     "If you don't yet know your own type, look for yourself in these stories.", "line 100")

# Chapter 3's opening (11-03).
insert_after_heading("## Chapter 3: The Two Realms", unbracket(prop[184]), "Chapter 3 opening")

# Chapter 4 rebuilt in the new order, with its openings (11-03 to 11-04).
start = t.index("## Chapter 4: The Three Orientations\n")
end = t.index("## Chapter 5: Where the Types Come From\n")
ch4 = open(SP + "/working/ch4-approved.md", encoding="utf-8").read().rstrip("\n")
t = t[:start] + ch4 + "\n\n---\n\n" + t[end:]

# Chapter 5's opening ([A]'s version as merged, 11-05), line 434's join, line 696.
ch5 = ("Each of the nine Enneagram types is a combination of one of the three orientations in the physical realm and one in the psychic realm. "
       "The characteristics of the two orientations explain the characteristics of the type. "
       "A realm where a person is enthusiastic or cautious supplies motivation that the person can direct at a realm where the person is detached. "
       "Standards that belong to one realm fail when a person applies them in the other. "
       "People of each type, from the One to the Nine, get something from the two orientations together that neither gives alone, and fail to notice particular things because of the pair.")
insert_after_heading("## Chapter 5: Where the Types Come From", ch5, "Chapter 5 opening")
once("A person has one of these three in the physical realm", "A person has one of the three orientations in the physical realm", "line 434")
once("Nine pairs, nine types. If the nine pairs are the nine types, each type's", "Nine pairs, nine types. Each type's", "line 696")

# Part 2's opening (proposed 11-04; amended by [A] through Job99, RELAY-from-job99-20261104b.md, 19:46).
part2 = """The nine types fit together in a definite arrangement. How people change, and how people of different types get on with one another, both follow from the arrangement.

Three of the nine types hold the same orientation in both realms, and six hold a different orientation in each realm. The three orientations also come in a fixed order, and the order comes back to its start: the order runs from enthusiasm to caution, from caution to detachment, and from detachment back to enthusiasm. When stress is low, a person shifts a little toward the orientation one step forward along the order, and under stress a little toward the orientation one step back. The order also runs forward through every single thought a person has.

Comparing two people's orientations realm by realm shows which person is a step further along the order in each realm. From that comparison a person can understand much of who looks up to whom, and where the friction between two people comes from. The lines the classical Enneagram draws between the types follow from the order of the orientations, and so do twelve more one-step relations, not drawn on the classical figure, along which a person seems to grow. A person who becomes less caught in a realm comes to resemble the type a step ahead in that realm. Nobody holds an orientation purely. Each person leans a little toward the orientation before or after their own, and a lean in detachment changes what a detached person notices."""
insert_after_heading("# Part 2 — The Finer Structure", part2, "Part 2 opening")

# RELAY-from-job99-20261104b.md, points 2 and 3 ([A] 19:46, 19:53).
once("On every line, the type a person is pulled toward in growth is one step forward along the order, in one realm or in both. The type a person is pulled toward under stress is one step back, in one realm or in both.",
     "On every line, when stress is low, a person shifts a little toward the type one step forward along the order, in one realm or in both. Under stress, a person shifts a little toward the type one step back, in one realm or in both.", "Ch7 prediction")
once("The cycle is about which way the pull goes when circumstances pull: toward the next orientation,",
     "The cycle is about which way a person shifts a little when circumstances change: toward the next orientation,", "Ch7 directions")
once("which way they are pulled from it, and how far", "which way the person shifts from it, and how far", "Ch7 scale of character")
once("each realm pulled toward the orientation behind it", "each realm shifting a little toward the orientation behind it", "Ch10 either end")
once("A lean is a pull toward one of the two orientations", "A lean is a shading toward one of the two orientations", "Ch14 lean")

once("The classical Enneagram describes which way a person is pulled in growth and under stress,", "The classical Enneagram describes which way a person shifts a little in growth and under stress,", "line 740 (11-05)")

open(OUT, "w", encoding="utf-8").write(t)
print("ok", OUT)
