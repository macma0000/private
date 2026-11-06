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

insert_after_heading("## Chapter 6: The Grid", "The nine types can be laid out in a table, with the three orientations in the physical realm along the top and the three orientations in the psychic realm down the side. Three of the nine types hold the same orientation in both realms. A person with the same orientation in both realms seems to have only ever noticed in one way, and takes their own way of noticing to be how things are. Six of the nine types hold a different orientation in each realm. The classical Enneagram joins the three types with the same orientation in both realms by a triangle, and joins the six types with two different orientations by a six-sided figure. A step from one type to a neighboring type in the table changes the orientation in one realm, or in both realms at once. Three pairs of types are made of the same two orientations with the realms exchanged: the One and the Eight, the Two and the Seven, and the Four and the Five.", "Chapter 6 opening (11-05)")

insert_after_heading("## Chapter 7: The Cycle", "The three orientations follow one another in a fixed order, and the order comes back to its start: the order runs from enthusiasm to caution, from caution to detachment, and from detachment back to enthusiasm. A person's orientation in a realm does not ordinarily change, but when circumstances change, a person shifts a little either forward along the order or back against the order. When stress is low, a person shifts a little forward, and under stress a little back. The order predicts the directions the classical Enneagram gives each of the nine types for growth and for stress. Each step forward asks something particular of a person, and each step back is a particular way of coming apart under stress. A detached person handles a fear in one of two ways, depending on whether the person is nearer caution or nearer enthusiasm. The order also runs forward through processes much smaller than a character, such as a project, and a single thought, which passes through a place for each of the three orientations in a fraction of a second.", "Chapter 7 opening (11-05)")

insert_after_heading("### Forward", "A person tends toward the next orientation along the order: from enthusiasm toward caution, from caution toward detachment, and from detachment back toward enthusiasm. Each shift forward asks a person to accept something the person's orientation habitually resists. A less caught person can bear more of what a shift forward asks.", "Forward opening (11-05)")

once("In the case of each orientation, what the step requires is what such a person habitually resists. That is why the forward direction says what has to be true before a person takes a step, and not when they will take it. The less caught a person is in the orientation they hold, the more of what the step requires they can bear.",
     "In the case of each orientation, what the shift requires is what such a person habitually resists. That is why the forward direction says what has to be true before a person shifts forward, and not when the person will shift. The less caught a person is in the orientation they hold, the more of what the shift requires they can bear.", "line 752 (11-05)")

insert_after_heading("### Backward", 'Under stress, a person shifts a little toward the orientation one step back, and lands in a poor version of it: an enthusiastic person collapses into numb withdrawal, a detached person falls into anxious worry, and a cautious person panics into recklessness.', "Backward opening (11-05)")

insert_after_heading("### The two faces of detachment", 'Detachment borders caution at one end and enthusiasm at the other, and a detached person handles a fear differently near each end: near caution the person looks at the fear, and near enthusiasm the person turns away from the fear.', "Two faces opening (11-05)")

insert_after_heading("### The smallest scale", 'A thought passes through three places, one for each orientation, in the forward order, and when one thought ends the next thought begins. Thoughts run this way in everyone, whatever their type, many times a minute, and anyone can check the claim in their own thinking.', "Smallest scale opening (11-05)")
once("It is a fact, completing many times an hour, in everyone", "It is a fact, completing many times a minute, in everyone", "line 788 (11-05)")

insert_after_heading("## Chapter 8: Relational Positions", "How two people get on depends partly on how their orientations compare, realm by realm. In each realm, either the two people hold the same orientation, or one of the two holds the orientation a step further along the order. The two comparisons together put every pair of types into one of six relative positions, and knowing two people's types is enough to know their relative position. Because the order comes back to its start, being a step further along is a place on a circle and not a rank, so no type is at the top. Every type has the same number of types in each relative position.", "Chapter 8 opening (11-05)")

once("The three aligned types reach one another only through the double positions. The Three is Double Ahead of the Nine, the Nine of the Six, and the Six of the Three, each by one step in each realm. The classical system",
     "Between any two of the three aligned types, the position is always a double one. The Three is Double Ahead of the Nine, the Nine of the Six, and the Six of the Three, each by one step in each realm. With each of the six mixed types, an aligned type is Ahead, Behind or Equal, and never in a double position. The classical system", "line 816 (RELAY 20261104c item 2, yes 11-05)")

insert_after_heading("### What passes between them", 'Between two people a step apart in a realm, two different things pass: appreciation, which runs both ways, and looking up, which runs only from the person behind to the person ahead. Respect is a third thing, and respect does not depend on where anyone stands. Because the order of the orientations is a circle, three people can each correctly look up to the next, all the way round.', "What passes between them opening (11-06)")

once("This is checkable, and it is where the account differs sharply from most descriptions of human development, which assume that someone further along than a second person, who is further along than a third, must be further along than the third. Here three people can each sincerely, and correctly, see the next one as further along, all the way around the circle. What would count is a closed circle of three: each of the three reporting that they look to the next, and the third reporting that they look to the first.",
     "Because the order of the orientations is a circle of three, two steps ahead is one step behind, so each of three people can be ahead of the next, all the way round. Three people who each look up to the next, around the circle, would show it.", "line 845 (11-06)")

open(OUT, "w", encoding="utf-8").write(t)
print("ok", OUT)
