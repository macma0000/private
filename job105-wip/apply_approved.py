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

once("The classical Enneagram describes which way a person is pulled in growth and under stress,", "The classical Enneagram describes which way a person shifts a little when stress is low and under stress,", "line 740 (11-05)")

insert_after_heading("## Chapter 6: The Grid", "The nine types can be laid out in a table, with the three orientations in the physical realm along the top and the three orientations in the psychic realm down the side. Three of the nine types hold the same orientation in both realms. A person with the same orientation in both realms seems to have only ever noticed in one way, and takes their own way of noticing to be how things are. Six of the nine types hold a different orientation in each realm. The classical Enneagram joins the three types with the same orientation in both realms by a triangle, and joins the six types with two different orientations by a six-sided figure. A step from one type to a neighboring type in the table changes the orientation in one realm, or in both realms at once. Three pairs of types are made of the same two orientations with the realms exchanged: the One and the Eight, the Two and the Seven, and the Four and the Five.", "Chapter 6 opening (11-05)")

insert_after_heading("## Chapter 7: The Cycle", "The three orientations follow one another in a fixed order, and the order comes back to its start: the order runs from enthusiasm to caution, from caution to detachment, and from detachment back to enthusiasm. A person's orientation in a realm does not ordinarily change, but when circumstances change, a person shifts a little either forward along the order or back against the order. When stress is low, a person shifts a little forward, and under stress a little back. The order predicts the two directions the classical Enneagram gives each of the nine types: one when stress is low, and one under stress. Each step forward asks something particular of a person, and each step back is a particular way of coming apart under stress. A detached person handles a fear in one of two ways, depending on whether the person is nearer caution or nearer enthusiasm. The order also runs forward through processes much smaller than a character, such as a project, and a single thought, which passes through a place for each of the three orientations in a fraction of a second.", "Chapter 7 opening (11-05)")

insert_after_heading("### Forward", "A person tends toward the next orientation along the order: from enthusiasm toward caution, from caution toward detachment, and from detachment back toward enthusiasm. Each shift forward asks a person to accept something the person's orientation habitually resists. A less caught person can bear more of what a shift forward asks.", "Forward opening (11-05)")

once("In the case of each orientation, what the step requires is what such a person habitually resists. That is why the forward direction says what has to be true before a person takes a step, and not when they will take it. The less caught a person is in the orientation they hold, the more of what the step requires they can bear.",
     "In the case of each orientation, what the shift requires is what such a person habitually resists. That is why the forward direction says what has to be true before a person shifts forward, and not when the person will shift. The less caught a person is in the orientation they hold, the more of what the shift requires they can bear.", "line 752 (11-05)")

insert_after_heading("### Backward", 'Under stress, a person shifts a little toward the orientation one step back, and lands in a poor version of it: an enthusiastic person collapses into numb withdrawal, a detached person falls into anxious worry, and a cautious person panics into recklessness.', "Backward opening (11-05)")

insert_after_heading("### The two faces of detachment", 'Detachment lies between caution and enthusiasm, and a detached person can lean toward either. A detached person leaning toward caution looks at a fear, and a detached person leaning toward enthusiasm turns away from the fear.', "Two faces opening (11-05)")

insert_after_heading("### The smallest scale", 'A thought passes through three places, one for each orientation, in the forward order, and when one thought ends the next thought begins. Thoughts run this way in everyone, whatever their type, many times a minute, and anyone can check the claim in their own thinking.', "Smallest scale opening (11-05)")
once("It is a fact, completing many times an hour, in everyone", "It is a fact, completing many times a minute, in everyone", "line 788 (11-05)")

insert_after_heading("## Chapter 8: Relational Positions", "How two people get on depends partly on how their orientations compare, realm by realm. In each realm, either the two people hold the same orientation, or one of the two holds the orientation a step further along the order. The two comparisons together put every pair of types into one of six relative positions, and knowing two people's types is enough to know their relative position. Because the order comes back to its start, being a step further along is a place on a circle and not a rank, so no type is at the top. Every type has the same number of types in each relative position.", "Chapter 8 opening (11-05)")

once("The three aligned types reach one another only through the double positions. The Three is Double Ahead of the Nine, the Nine of the Six, and the Six of the Three, each by one step in each realm. The classical system",
     "Between any two of the three aligned types, the position is always a double one. The Three is Double Ahead of the Nine, the Nine of the Six, and the Six of the Three, each by one step in each realm. With each of the six mixed types, an aligned type is Ahead, Behind or Equal, and never in a double position. The classical system", "line 816 (RELAY 20261104c item 2, yes 11-05)")

insert_after_heading("### What passes between them", 'Between two people a step apart in a realm, two different things pass: appreciation, which runs both ways, and looking up, which runs only from the person behind to the person ahead. Respect is a third thing, and respect does not depend on where anyone stands. Because the order of the orientations is a circle, three people can each correctly look up to the next, all the way round.', "What passes between them opening (11-06)")

once("This is checkable, and it is where the account differs sharply from most descriptions of human development, which assume that someone further along than a second person, who is further along than a third, must be further along than the third. Here three people can each sincerely, and correctly, see the next one as further along, all the way around the circle. What would count is a closed circle of three: each of the three reporting that they look to the next, and the third reporting that they look to the first.",
     "Because the order of the orientations is a circle of three, two steps ahead is one step behind, so each of three people can be ahead of the next, all the way round. Three people who each look up to the next, around the circle, would show it.", "line 845 (11-06)")

once(" All three statements are true at once. On a ladder that would be nonsense; on a circle it is geography.", " All three statements are true at once.", "line 843 (11-06)")

once("All three statements are true at once.\n\nBecause the order of the orientations is a circle of three,", "All three statements are true at once. Because the order of the orientations is a circle of three,", "lines 843 and 845 joined (11-06)")

insert_after_heading("### Position by position", "Each relative position gives two people something and can go wrong in its own way: Ahead and Behind can become mentorship or resentment, Equal is usually the easiest, and two people in the Identical position share each other's blind spots. A relative position harms a relationship only when the two people do not recognize it.", "Position by position opening (11-06)")

once("one of six relative positions, and knowing two people's types is enough to know their relative position.",
     "one of six relational positions, and knowing two people's types is enough to know their relational position.", 'Ch8 opening relational (11-06)')
once('Every type has the same number of types in each relative position.',
     'Every type has the same number of types in each relational position.', 'Ch8 opening relational 2 (11-06)')
once('Each relative position gives two people something',
     'Each relational position gives two people something', 'Position opening relational (11-06)')
once('A relative position harms a relationship',
     'A relational position harms a relationship', 'Position opening relational 2 (11-06)')
once('sort every possible pair of types into one of six positions.',
     'sort every possible pair of types into one of six relational positions.', 'l836 (11-06)')
once('Ahead here is a position on a circle, not a rank.',
     'Ahead here is a relational position on a circle, not a rank.', 'l838 (11-06)')
once('A double position is one step in each realm',
     'A double relational position is one step in each realm', 'l853 (11-06)')
once('Reading a position off the grid',
     'Reading a relational position off the grid', 'l855 (11-06)')
once('the position is always a double one.',
     'the relational position is always a double one.', 'l816 a (11-06)')
once('and never in a double position.',
     'and never in a double relational position.', 'l816 b (11-06)')
once('A position is a fact about two types.',
     'A relational position is a fact about two types.', 'Ch9 first (11-06)')
once('In every position except Equal and Identical',
     'In every relational position except Equal and Identical', 'Ch9 every (11-06)')
once('an accurate reading of position from curdling',
     'an accurate reading of relational position from curdling', 'Ch9 reading (11-06)')
once('These name relative positions on the cycle',
     'These name relational positions on the cycle', 'Ch9 relative (11-06)')
once('This is the position with the clearest structure',
     'This is the relational position with the clearest structure', 'Ch9 clearest (11-06)')
once('Double positions carry the same dynamic',
     'Double relational positions carry the same dynamic', 'Ch9 double (11-06)')
once('A position is a liability only when it goes unrecognized.',
     'A relational position is a liability only when it goes unrecognized.', 'Ch9 liability (11-06)')
once('Left unnamed, the same positions curdle',
     'Left unnamed, the same relational positions curdle', 'Ch9 curdle (11-06)')
once('real lives contain several positions at once',
     'real lives contain several relational positions at once', 'Ch9 several (11-06)')
once('Maya can mistake his position for his worth',
     'Maya can mistake his relational position for his worth', 'Ch9 Maya (11-06)')
once('their position is the reason',
     'their relational position is the reason', 'Ch9 Elena (11-06)')
once('Position was given earlier as a fact about two people',
     'Relational position was given earlier as a fact about two people', 'Ch10 (11-06)')
once('Equal and Identical were the two arrangements in which neither person holds the forward position,',
     'Equal and Identical were the two relational positions in which neither person is ahead,', 'Ch11 (11-06)')
once('### Equal positions, and the mirror pairs',
     '### Equal relational positions, and the mirror pairs', 'heading (11-06)')
once('### Aligned and mixed\n\nTwo aligned types together',
     '### Orientation by orientation\n\nSome dynamics come from which orientations the two people hold. Two aligned types together', 'relay 1 (11-06)')
once("### Friction from the detached realm\n\nEverything above comes from where two people's orientations sit on the cycle. A second source of friction comes from the realms themselves. A person detached in a realm",
     'A person detached in a realm', 'relay 2a (11-06)')
once('each can insist on false ideas in the realm the other understands. This friction is independent of relational position, and it can sharpen or soften any of the dynamics above.',
     'each can insist on false ideas in the realm the other understands. Undervaluing a realm can sharpen or soften the dynamics of every relational position except Identical, where the two people are detached in the same realms.', 'relay 2b (11-06)')

once('Maya and Daniel show both mechanisms at once.',
     'Maya and Daniel show both sources at once.', 'Maya first sentence (11-06)')
once('None of it has anything to do with Maya being Double Ahead, which is what made Daniel admire her. Position and realm friction are separate mechanisms, and in this marriage',
     "The undervaluing comes from the realms, and Daniel's admiration comes from Maya being Double Ahead. Relational position and the orientations the two people hold are separate sources, and in this marriage", 'relay 3 (11-06)')

once('A relational position is a fact about two types. What it is like from inside is a different matter — who looks up to whom, where the irritation comes from, and what each person has that the other needs.',
     'A relational position is a fact about two types. What it is like from inside is a different matter — who looks up to whom, where the irritation comes from, and what each person has that the other needs. These dynamics come from the relational position, whichever orientations fill it. Other dynamics come from which orientations the two people hold. The orientations change what happens within a relational position, and decide how easily each person sees their own orientation as an orientation, whether each person undervalues the realm where the other is competent, and how widely the two people differ.', 'Ch9 opening paragraph (11-06)')
once('Some dynamics come from which orientations the two people hold. Two aligned types together',
     'Some dynamics come from which orientations the two people hold. Within one relational position, what happens also differs with the orientations that fill it. Two aligned types together', 'Orientation by orientation sentence (11-06)')
once("knowing two people's types is enough to know their relational position. Because the order comes back to its start,",
     "knowing two people's types is enough to know their relational position. In a given realm, a person tends to be energized by someone a step further along the order and burdened by someone a step back. So comparing two people's orientations helps explain who looks up to whom, where irritation between the two comes from, and what the two have to give each other. Because the order comes back to its start,", 'RELAY 20261105b item 1 (11-06)')
once('Maya is Double Ahead of Daniel, and Daniel Double Behind of Maya.',
     "Maya is Double Ahead of Daniel, and Daniel Double Behind of Maya. Daniel looks up to Maya, and Maya sees in Daniel's carefulness something she has moved past.", 'RELAY 20261105b item 2 (11-06)')
once("Maya does not experience herself as ahead of anyone, but Daniel's carefulness",
     "Maya does not think of herself as above Daniel, but Daniel's carefulness", 'RELAY 20261105b item 3 (11-06)')

once('### In everyday life\n\nFour sketches, and the same handful of people recur, because real lives contain several relational positions at once.',
     '### In everyday life\n\nRelational positions show up in ordinary marriages, workplaces and friendships: a husband who admires his wife as better at life than he is, two colleagues who differ in one realm only, two business partners who are each ahead in one realm, and two friends of one type whose worries grow when shared.\n\nA few people appear in more than one of these relationships, because real lives contain several relational positions at once.', 'In everyday life opening and first sentence (11-06)')

once('Within one relational position, what happens also differs with the orientations that fill it. Two aligned types together',
     "Within one relational position, what happens also differs with the orientations that fill it. Whether each person is an aligned or a mixed type changes how easily each sees their own orientation, and a person detached in a realm tends to undervalue another person's competence there.\n\nTwo aligned types together", 'Orientation by orientation opening (11-06)')

once("and gives each line a direction of growth and a direction of stress.", "and gives each line a direction a person shifts in when stress is low and a direction a person shifts in under stress.", "Ch7 lines growth (11-07)")

once('### Opposite\n\nSix positional relationships have already been set out — Double Ahead, Ahead, Equal, Behind, Double Behind and Identical. There is a seventh arrangement that belongs to none of them.',
     '### Opposite\n\nTwo people can stand exactly opposite each other on the circle in both realms. Only a lean can put two people there, because no two of the three orientations stand exactly opposite. Between two opposite people neither is ahead of the other, whatever relational position the two would otherwise be in.\n\nBesides the six relational positions — Double Ahead, Ahead, Equal, Behind, Double Behind and Identical — opposition is one more important relation between two people.', 'Opposite opening and first sentences (11-08)')
once('whatever class they otherwise stand in,',
     'whatever relational position they otherwise stand in,', 'Opposite class (11-08)')
once('That symmetry matters for the asymmetry set out earlier. Equal and Identical were the two relational positions in which neither person is ahead, and opposite is a third — balanced not because opposition is a kind of equality, but because the symmetry cancels the ahead and behind of whatever class it arises from.',
     'That symmetry puts opposition beside Equal and Identical, the two relational positions in which neither person is ahead. In all three, the two people stand symmetrically, so neither is ahead.', 'Opposite last paragraph (11-08)')

once('The eight combinations are read the same way whichever orientation a person rests at, and for enthusiasm and caution that is right: a lean shades the orientation without altering what it does. A lean in detachment alters what it does.',
     'Everything about leans and wings holds for detachment just as it does for enthusiasm and caution. For enthusiasm and caution, a lean shades the orientation without altering what it does. A lean in detachment also alters what it does, in a way that has nothing to do with types or wings.', 'lean in detachment first paragraph (11-08)')

once('In each realm one of the three orientations settles and hardens into habit. A hardened orientation is what this book calls a **fixation**.',
     'In each realm, one of the three orientations hardens into habit. A hardened orientation is called a **fixation**.', 'Part 3 first paragraph (11-08)')

once('This is what Parts 1 and 2 have been describing throughout. A realm was called detached, or enthusiastic, or cautious, and what that named was the fixation a person holds in the realm. A person was called more or less caught, and what varied was how strongly a person holds the fixation.',
     "Wherever a person is enthusiastic, cautious or detached in a realm, the orientation is the person's fixation in that realm. Fixation is a new name, not a new thing: it is the orientation a person holds, with the hardening brought out. How deeply caught a person is in a realm is how strongly the person holds the fixation.", 'Part 3 second paragraph (11-08)')

once('caution is what they have, and enthusiasm and detachment are not available to them.',
     'caution is what they have, and enthusiasm and detachment are not available to them. Having fixations is normal, since each of the nine types is a pair of fixations. What the word judges is the limitation, not the person. Each fixation also comes with the competence of its orientation, and the competence is real.', 'RELAY 20261107 item 2 ([A] 16:59)')

once('and Claudio Naranjo developed them into the enneatypes in use today. The claim in both is that a type is a fixation. This book keeps that claim. What this book adds is that a person holds two fixations, one in each realm, and that the nine types',
     'and Claudio Naranjo developed them into what he called enneatypes. The claim in both is that a type is a fixation. That claim holds, with one addition: a person holds two fixations, one in each realm, and the nine types', 'Part 3 third paragraph (RELAY 20261107 item 1, yes 11-08)')

once("carried it to Berkeley in 1971 and worked it into the detailed descriptions in use today. From Naranjo's students it passed into Jesuit retreat work, and from there outward, until Helen Palmer, Don Riso, Russ Hudson and others made it one of the most widely used accounts of personality anywhere.",
     "carried it to Berkeley in the early 1970s and developed the types further. From Naranjo's students it passed into Jesuit retreat work, and from there outward. Don Riso, later joined by Russ Hudson, expanded the types into the detailed descriptions in use today and added the Levels of Development. Helen Palmer and others helped make it one of the most widely used accounts of personality anywhere.", 'Introduction history (11-08)')

once('would mind nothing at all. Buddhism calls such a person an arhat. An arhat is not the same as a detached person with no lean.',
     'would mind nothing at all. Such a person is not the same as a detached person with no lean. A detached person with no lean still wants peace, and minds whatever disturbs it.', 'RELAY 20261107b ([A] 17:13)')

once('Every orientation comes with something a person cannot easily bear, and detachment does too. A detached person minds being disturbed, even a detached person with no lean either way.',
     'Detachment is a fixation too: like every orientation, it comes with something a person cannot easily bear. A detached person minds being disturbed, even a detached person with no lean either way.', 'Part 3 detachment paragraph join (11-08)')

once('Parts 1 and 2 described the orientations, the nine types they make, and how people of different types meet one another. None of that needed the word fixation.',
     "People have a capacity to track other minds: they can guess what someone else will do. A person's inner world, and the self in it, are what that capacity produces when directed at the very mind doing the tracking. A person's own fixation never shows up in the picture of the self. A fixation shapes everything the person pictures, and is not itself one of the things pictured. So a person cannot find their own fixation by looking inward. Enthusiasm and caution are directed at things. Detachment is directed at a person's own reactions, so any way out of a fixation runs through detachment.", 'Part 3 sixth paragraph (11-08)')
once('The self seems to be what a capacity built for tracking other minds produces when the capacity is directed at the mind doing the tracking.',
     'The self is what a capacity built for tracking other minds produces when the capacity is directed at the mind doing the tracking.', 'Ch13 self (11-08)')

once('show in how the fixation runs a thought.\n\nPeople also differ in how deeply they are caught in their fixations.',
     "show in how the fixation runs a thought.\n\nEach thought ends in the detached phase, and what becomes of a fear is decided there. A fear can be settled: what to do about the matter the fear is about is found, or the want behind it is given up. A fear can also be left alone, and then it comes back with the problem. Or a fear can be turned away from until it is no longer noticed.\n\nA fear that grows past what a person can bear is turned away from in panic, and then it stays out of view. Whenever anything comes near the fear, a fresh anxiety arises, and the person turns away from the anxiety too. What a person turns away from goes on working on the person unseen. Aversions that are left alone or turned away from leave a lasting unease, felt with nothing to explain it.\n\nFixations differ in how they handle fears. How likely a fear is to be settled depends on the person's fixation in the realm the fear is about. A fixation might come from two sources: a person's constitution, and what happened in the person's earliest years, before the person could understand any of it. Once a fixation is laid down, habit keeps it running. Nothing has to be believed for habit to keep running, so a fixation can last a whole life.\n\nPeople also differ in how deeply they are caught in their fixations.", 'Part 3 new paragraphs (11-08)')
once('The fear can be worked through, which means the thought finds what to do about the fear.',
     'The fear can be worked through, which means what to do about the matter the fear is about is found.', 'Ch14 worked through (11-08)')
once('A fear can be worked through, which means the thought finds what to do about the fear.',
     'A fear can be worked through, which means what to do about the matter the fear is about is found.', 'Ch15 worked through (11-08)')
once('*Worked through* — the thought has found what to do about the fear, so the fear is settled. Nothing has been turned away from. What the thought finds may be',
     '*Worked through* — what to do about the matter the fear is about has been found, so the fear is settled. Nothing has been turned away from. What is found may be', 'line 1270 (11-08)')
once('A fear worked through ends because the thought found what to do about the fear.',
     'A fear worked through ends because what to do about the matter the fear is about was found.', 'line 1294 (11-08)')
once('The thought finds what to do about the fear: the person decides to call the agent in the morning.',
     'What to do about the matter the fear is about is found: the person decides to call the agent in the morning.', 'unease loop example (11-08)')

once('## Chapter 13: Where the Inner World Came From\n\n### A part of the world that contains the rest',
     "## Chapter 13: Where the Inner World Came From\n\nThe physical realm is about things. The physical realm is the outside world everyone shares. The psychic realm is the inner world of thoughts and feelings, which can be somewhat different for different people.\n\nThoughts and feelings are themselves part of the psychic realm. So a person can think about thoughts and feelings, including the person's own, and the thinking becomes part of what the person is thinking about. Thinking about thinking has consequences the physical realm does not have: a person comes to see a self, a mistake in the psychic realm can go uncorrected for a long time, and a person cannot find their own fixation by looking inward.\n\n### A part of the world that contains the rest", 'RELAY 20261108 item 1 ([A] 08:47)')
once('in the only sense anything inner is ever there. What it is not is an object.',
     "in the only sense anything inner is ever there. What it is not is an object. An animal predicting another animal pictures a cause inside the other animal for what the other animal does. The cause is never seen; the picture only holds a place for the cause. Turned on oneself, the capacity does the same. The self is a placeholder for a person's behavior as observed from the outside.", 'RELAY 20261108 item 2 ([A] 08:48)')

once('Until now the cycle has been used to put the three orientations in order:',
     'The cycle puts the three orientations in order:', 'Ch14 first sentence (11-08)')

once('### Where a fear meets its fate\n\nA thought finishes in the detached phase. A fear the thought is still carrying meets its fate in the detached phase.',
     '### Where a fear meets its fate\n\nA fear a thought is still carrying meets its fate in the detached phase, where the thought finishes.', 'Where a fear meets its fate first sentence (11-08)')

once('### What a thought leaves\n\nWhen a thought ends, the next thought is a separate thought. What the ended thought was still carrying is laid down.',
     '### What a thought leaves\n\nWhen a thought ends, what the thought was still carrying is laid down. The next thought is a separate thought.', 'What a thought leaves first sentences (11-08)')

once('## Chapter 15: What Becomes of a Fear\n\n### Disregarding',
     "## Chapter 15: What Becomes of a Fear\n\nEveryone has had a worry that keeps coming back, and an unease with nothing to explain it. Both come from what happens to fears. A fear can be settled, and then it leaves little behind. A fear can be left alone, and then it comes back with the problem. And a fear can be turned away from, sometimes so completely that the person can no longer notice the problem the fear was about. A fear turned away from like that goes on shaping the person's life, though the person never decided anything.\n\n### Disregarding", 'Ch15 introduction (11-08)')

insert_after_heading("### How a fear comes to be buried", 'A single piece of bad news raises several fears in a person. Some of the fears are ignored or blocked by discomfort and come back stronger, until one is more than the person can bear and panic turns the person away from that fear. After the panic, layers of fear of the fear build up, and the turning away comes sooner and reaches further.', "How a fear comes to be buried opening (11-08)")

insert_after_heading("### The unease loop", 'Unease about a matter that does not resolve keeps a person going from a fear, to bodily tension, to a new fear, with nothing turned away from. People of each orientation go round differently, and each orientation has its own way out. A person takes a way out when the unease hurts more than doing what the way out requires. A person can also turn a matter over in the same way while the outcome can still be changed.', "Unease loop opening (11-08)")

insert_after_heading("### Lasting unease", 'Unease can be present without being noticed, and noticed without being acted on. Letting go of a tension in the body and a skill for handling fear help with unease in different ways. Most people feel uneasy when completely idle, and look for a distraction, and every distraction wears off. Unease that lasts has three sources: ignored aversions, blocked aversions, and being less able to handle life than others are. Lasting unease also produces habitual fears, which usually ease when the source of the unease ends.', "Lasting unease opening (11-08)")

once('Integration is the direction natural experience leads as a person meets the drawbacks of the orientation they hold.',
     "Integration is the natural direction toward the next orientation, which would remedy the drawbacks of a person's own orientation, and which holding on to that orientation inhibits.", 'line 740 integration (11-08)')

once('But the fear arriving meets the want for peace, and the discomfort',
     'But wanting brings fears with it, and the discomfort', 'Z to A (11-08)')

once('since each meets their own two orientations in the other realm.',
     'since each sees their own two orientations in the other person, held in the opposite realms.', 'mirror pair meet (11-08)')

once('so when either meets genuine stillness in someone, both read it as something being wrong.',
     'so genuine stillness in someone is something neither of them relates to.', 'Elena and Marcus meet (11-08)')

once('The fear is raised again when the person next meets the problem of the sale.',
     'The fear is raised again when the problem of the sale next comes up.', 'sale meet (11-08)')

once('Everyone meets conflict; what differs',
     'Conflict comes to everyone; what differs', 'conflict meet (11-08)')

once('practiced enough to meet a feeling as a feeling.',
     'practiced enough to experience a feeling as a feeling.', 'feeling meet (11-08)')

once('## Chapter 16: The Fixations Themselves\n\n### The range of detachment',
     "## Chapter 16: The Fixations Themselves\n\nA person does not handle every fear the same way. How a fear is handled depends on the fixation the person holds in the realm the fear is about, so a mixed type handles fears differently in each realm. Detachment is more complicated than the other two fixations, because a detached person can stand anywhere along a range between caution and enthusiasm, and where the person stands decides much of what becomes of a fear. Following one undertaking through a person of each fixation shows where each person's attention goes, and what each person does when the undertaking runs into trouble. A fixation might begin in infancy, when one of the three orientations comes to predominate, first by constitution and then by how the people around the child respond. The orientation becomes the place where the child is comfortable, and habit keeps it running even when what the person believes changes.\n\n### The range of detachment", 'Ch16 introduction (11-08)')

insert_after_heading("### The range of detachment", "A detached person wants peace, and wanting peace pulls a person's noticing nowhere until something disturbs the person. When something does disturb the person, a person leaning toward caution looks at the trouble and tries to solve it, and a person leaning toward enthusiasm wants the disturbance gone and reaches for a distraction. A person with no lean either way does both, about equally.", "Range of detachment opening (RELAY 20261108b item 1)")
once('**Pure detachment.** For enthusiasm and caution, having no lean is simply the orientation at full strength, because their leans only shade intensity. Detachment is different, because its two leans are opposite functions rather than two degrees of one. Pure detachment is no lean either way. A person with no lean does not go looking, which would be a lean toward caution. The person does not look away either, which would be a lean toward enthusiasm. Where a person with no lean fails to notice something, nothing was defended. There was simply no motive to notice the thing.\n\nWhen something does disturb a person with no lean, peace means not being drawn into what troubles other people — their practical worries in the physical realm, their emotions in the psychic one.',
     "**Pure detachment.** For enthusiasm and caution, having no lean is simply the orientation unshaded. A lean in enthusiasm or caution shades the orientation without changing what the orientation does. Detachment is different, because its two leans are opposite ways of achieving the same goal, peace. Pure detachment is no lean either way, the point in the middle of the range between leaning toward caution and leaning toward enthusiasm. While nothing is disturbing a person with no lean, the whole realm stays open to the person's noticing, and peace means not being drawn into what troubles other people — their practical worries in the physical realm, their emotions in the psychic one. Anything the person fails to notice at such a time goes unnoticed only because nothing gave the person a motive to notice the thing.\n\nWhen something does disturb a person with no lean, the person looks at the trouble and tries to solve it, as a person leaning toward caution does, and wants what is not solved gone and reaches for a distraction, as a person leaning toward enthusiasm does. A person with no lean gives the caution end and the enthusiasm end of the detached phase about equal attention.", 'Pure detachment (RELAY 20261108b item 2, [A] 18:36, with the rule)')

once('Everything about leans and wings holds for detachment just as it does for enthusiasm and caution. For enthusiasm and caution, a lean shades the orientation without altering what it does. A lean in detachment also alters what it does, in a way that has nothing to do with types or wings. Leaning back toward caution, detachment keeps the realm in view. Leaning forward toward enthusiasm, detachment has already turned toward what attracts, and anything that would disturb the attraction is not noticed. Which face appears',
     "For enthusiasm and caution, a lean shades the orientation without changing what the orientation does. A lean in detachment changes how a detached person reaches peace. Every thought passes through a detached phase, with a caution end and an enthusiasm end, and a detached person's lean sets how much attention each end gets. While nothing is disturbing a detached person, the whole realm is open to noticing, whichever way the person leans. When something disturbs a person leaning toward caution, the caution end of the detached phase gets the most attention, and the person looks at the disturbance and tries to solve it. When something disturbs a person leaning toward enthusiasm, the enthusiasm end of the detached phase gets the most attention, and the person wants the disturbance gone, reaches for a distraction, and at such a moment notices very little. Which face appears", 'Ch11 lean in detachment (RELAY 20261108b item 3, yes 11-09)')

once('Because they arrive by way of understanding, they enter detachment at its caution end.',
     'Because they arrive by way of understanding, they come to detachment leaning toward caution.', 'ends sweep (11-09)')
once('What differs between the two faces of detachment is what happens to the fear. At the caution end, the person looks at the fear and wants to solve what is disturbing them. Nearer the enthusiasm end, the person simply wants the fear to go away, and turns away from the fear. When a fear has grown to be more than the person can bear, the person panics at the caution end. Panic raises a want to be rid of the fear, and the want carries the person to the enthusiasm end, where the fear is no longer noticed.',
     'What differs between the two faces of detachment is what happens to the fear. A person leaning toward caution looks at the fear and wants to solve what is disturbing them. A person leaning toward enthusiasm simply wants the fear to go away, and turns away from the fear. When a fear has grown to be more than the person can bear, the person panics at the caution end of the detached phase. Panic raises a want to be rid of the fear, and the want carries the fear on to the enthusiasm end of the detached phase, where the fear is no longer noticed.', 'ends sweep (11-09)')
once('A process reaches the detached phase at the caution end, where fears are still noticed, and leaves by the enthusiasm end, where the turning away has gone furthest.',
     'A process comes first to the caution end of the detached phase, where fears are still noticed, and leaves the phase by the enthusiasm end, where the turning away has gone furthest.', 'ends sweep (11-09)')
once('A burial crosses the detached phase. At the caution end, the fear is still in view, and the caution end is where the fear is found to be more than the person can bear. Panic raises a want to be rid of the fear, and the want carries the person toward the enthusiasm end.',
     'A burial crosses the detached phase. At the caution end of the detached phase, the fear is still in view, and the caution end is where the fear is found to be more than the person can bear. Panic raises a want to be rid of the fear, and the want carries the fear toward the enthusiasm end.', 'ends sweep (11-09)')
once('A detached person at the caution end of the detached phase can settle the fear.',
     'A detached person can settle the fear at the caution end of the detached phase.', 'ends sweep (11-09)')
once('A person near the enthusiasm end of the detached phase runs the unease loop in a different way. Suppose the person waiting on the house sale leans toward the enthusiasm end.',
     'A detached person leaning toward enthusiasm runs the unease loop in a different way. Suppose the person waiting on the house sale leans toward enthusiasm.', 'ends sweep (11-09)')
once('The failures at the enthusiasm end show. The competence at the caution end stays quiet.',
     'The failures of a person leaning toward enthusiasm show. The competence of a person leaning toward caution stays quiet.', 'ends sweep (11-09)')
once('Near the caution end what a person wants is to be rid of the discomfort',
     'What a person leaning toward caution wants is to be rid of the discomfort', 'ends sweep (11-09)')
once('When something does disturb a person near the caution end, peace means',
     'When something does disturb a person leaning toward caution, peace means', 'ends sweep (11-09)')
once('Near the enthusiasm end what a person reaches for is a distraction',
     'What a person leaning toward enthusiasm reaches for is a distraction', 'ends sweep (11-09)')
once('When something does disturb a person near the enthusiasm end, peace means',
     'When something does disturb a person leaning toward enthusiasm, peace means', 'ends sweep (11-09)')
once('so a person near the enthusiasm end notices less at such a moment',
     'so a person leaning toward enthusiasm notices less at such a moment', 'ends sweep (11-09)')
once('A process reaches the caution end first and the enthusiasm end after.',
     'A process reaches the caution end of the detached phase first and the enthusiasm end after.', 'ends sweep (11-09)')
once('At the caution end an enthusiastic person often gives up on a fear',
     'At the caution end of the detached phase an enthusiastic person often gives up on a fear', 'ends sweep (11-09)')
once('At the caution end a cautious person may work a fear through',
     'At the caution end of the detached phase a cautious person may work a fear through', 'ends sweep (11-09)')
once('A detached person leaning toward caution gives the caution end the most attention, so a fear is more likely to be settled.',
     'A detached person leaning toward caution gives the caution end of the detached phase the most attention, so a fear is more likely to be settled.', 'ends sweep (11-09)')
once('A detached person leaning toward enthusiasm gives the caution end little attention, so a fear is less likely to be settled.',
     'A detached person leaning toward enthusiasm gives the caution end of the detached phase little attention, so a fear is less likely to be settled.', 'ends sweep (11-09)')
once('from the caution end of detachment, through caution, through appetite, to the enthusiasm end.',
     'from detachment leaning toward caution, through caution, through appetite, to detachment leaning toward enthusiasm.', 'ends sweep (11-09)')
once('run in the same direction, from the caution end to the enthusiasm end —',
     'run in the same direction, from detachment leaning toward caution to detachment leaning toward enthusiasm —', 'ends sweep (11-09)')
once('from the enthusiasm end of detachment the next step is appetite again.',
     'from detachment leaning toward enthusiasm the next step is appetite again.', 'ends sweep (11-09)')
once('A detached person leaning toward caution gives the caution end the most attention, and an arriving fear',
     'A detached person leaning toward caution gives the caution end of the detached phase the most attention, and an arriving fear', 'ends sweep (11-09)')
once('At the caution end a person is already willing to look at an arriving fear',
     'At the caution end of the detached phase a person is already willing to look at an arriving fear', 'ends sweep (11-09)')
once('The skill at the enthusiasm end is the harder of the two to use',
     'The skill at the enthusiasm end of the detached phase is the harder of the two to use', 'ends sweep (11-09)')

once('Two things have to be put together. The orientations are in hand already: the orientation a person holds',
     'Two things have to be put together. One is the orientation a person holds', 'Ch17 introduction (11-09)')
once("The scale itself is not this book's. It is the Levels of Development described by Don Riso and Russ Hudson, borrowed here and used as a measure of depth.",
     'The scale itself is the Levels of Development described by Don Riso and Russ Hudson, used as a measure of depth.', 'Ch17 introduction (11-09)')

once('## Chapter 18: Falling and Rising\n\n### What actually descends',
     '## Chapter 18: Falling and Rising\n\nMost people know someone who has slowly become harder to reach and less able to see what is happening to them, and someone who has slowly become freer. Both changes happen one fear at a time. A person falls when fears are turned away from, and with each fall the person notices less and can bear less. Nobody watches themselves go down, and yet most people stop somewhere in the middle, because the consequences of falling push back. A person rises when a buried fear is faced, and a skill for handling fear helps make the facing possible. Trying harder does not change a person, because whatever a person does about their own condition, the person does it as they already are.\n\n### What actually descends', 'Ch18 introduction (11-11)')

once('### Why this does not take everyone to the bottom\n\nSet out so far, the mechanism has a hole in it. The lower a person is,',
     "### Why this does not take everyone to the bottom\n\nMost people stay in the middle levels for decades, because a fall is slow and because the consequences of a fall push back. The pain that consequences bring keeps rising until staying as the person is becomes unbearable, and only then is the person open to trying something new. Everything a person turns away from is still taken in and laid down, and that is how recognition of the person's own condition slowly builds.\n\nThe lower a person is,", 'Why this does not take everyone opening and cut (11-11)')

insert_after_heading("### What reaches someone who cannot see their own condition", "A person far down still feels consequences, and another person who can see the person's condition can help in two ways: by steadying the person, and by giving the truth about the person's condition a little at a time. Urging does harm, because urging is pressure, and pressure lowers how much a person can bear.", "What reaches someone opening (11-11)")

insert_after_heading("### A skill for handling fear", 'The capacity to bear discomfort can be built on any kind of pain, as one woman found when she learned to stay with extreme migraine pain. A skill for handling fear can also be taught, and the skill goes in most easily in a child, before the child has any occasion to use the skill. What motivates a person to take up such a skill is the pain of life not working, weighed against the imagined pain associated with facing buried material. The skill does not move a person up the levels by itself; it changes how often a fear is handled instead of blocked, and the change, when it comes, tends to come suddenly after a long flat stretch.', "A skill for handling fear opening (11-11)")

once('All of that is method. What it is for can now be said, and it has been at stake since the first fear was turned away from.',
     'Every method for handling fear serves one end, which has been at stake since a fear was first turned away from: undoing the blocked fears.', 'What is actually being undone first paragraph (11-11)')

once("### The summit, and what counterfeits it\n\nAt the top there is nothing above to arrive at, so what happens there is not residence. The last crossing of the detached phase lands back in engagement, and then again, and the state is renewed rather than held.\n\nIt could not be held in any case, and the reason is the same one that runs the whole book. A state maintained is maintained by a habit of maintaining it, and that habit would need its own maintaining, and there is no floor to that. Habit is what carries a fixation and habit is what carries an attainment; it does not become a different faculty at the top of the ladder.\n\nThere is also something that looks like the summit and is not. Every thought passes through the detached phase, whatever a person's fixation. A person can train themselves to abide in the detached phase, giving the detached phase more attention than their fixation would give it. The training can be done for thoughts about one realm and not the other. No orientation is trained, and the person's type does not change.\n\nTake a person trained to work on a bleeding body, or to keep moving under fire. At such a moment the person abides in the detached phase of thoughts about physical matters, and does not flinch or look away. The training is real, and so is the steadiness. The person reaches for the training when fear would get in the way, and uses the training as a tool at those moments. Nothing about the person's type has changed.\n\nTake a person trained to sit with someone in the worst hour of their life and stay level, hearing what is said without being pulled into it. At such a moment the person abides in the detached phase of thoughts about psychic matters. Again the training is real, and again it is a tool used at moments. Nothing about the person's type has changed here either.\n\nObservers see the marks of the training in one realm and take the person to be like that throughout. What observers recognize as holiness is mostly these marks — austerity, fearlessness, unconcern with comfort and pain, a steadiness nothing seems to shake. The marks are real, and the mistake is the observers'. So the attainment behind the counterfeit summit is not faked. The counterfeit summit is a genuine, hard-won attainment in one realm, wearing the visible marks of the whole one, with the person's other realm running entirely unchecked behind the attainment.\n\nIn every case the attainment is real. What can differ is whether the person makes use of how others read the attainment. Suppose a person has trained to abide in the detached phase of thoughts about physical matters. Pain, hardship and danger no longer move the person, and the person shows no fear of harm or of death. Observers take that fearlessness as a sign of clarity about the inner life as well. The training has not touched the person's psychic realm. The person still has the wants they had before about psychic matters, such as wanting to be admired or to be seen as righteous. The person may then present the fearlessness as the summit on purpose, because being taken for someone at the summit brings admiration and followers. Presenting the fearlessness that way is a fraud.\n\nA person who has trained to abide in the detached phase of thoughts about psychic matters is no longer moved by praise, blame or other people's feelings. The person still wants money and comfort as before. The steadiness lets the person pursue those wants among other people without being moved by what those people feel. Others take the steadiness for the summit. Presenting the steadiness that way on purpose is a fraud as well. Nothing in the person checks what the attainment is used for.\n\nConscience is caution in the psychic realm: understanding the disadvantages of hurting others. For a person cautious in the psychic realm, conscience is their own fixation at work. While the person abides in the detached phase of thoughts about psychic matters, conscience is not raised. When the person stops abiding, conscience is there as before. A person enthusiastic in the psychic realm examines little of what their wants would do to others, so whatever conscience the person has was learned as a rule. A person who works for long without the rule may stop invoking the rule, and then stop having it. If that happens, the long working without the rule is the cause, and the training is not.\n\nIt would be reasonable to expect that training to abide in the detached phase weakens the person's fixation in the trained realm, when the fixation is enthusiastic or cautious. An enthusiastic fixation and a cautious fixation are both ways of engaging with a realm, and abiding in the detached phase works against engaging.\n\n### Why trying harder",
     "### The summit, and what counterfeits it\n\nAt the top there is nothing further to reach, and a person does not stay at the top either. Even at the top, every thought's detached phase ends at the arising, which takes the thought back into engagement, and the next thought does the same. So the clarity at the top needs to be renewed rather than held.\n\nIt could not be held in any case, and the reason is the same one that runs the whole book. A state maintained is maintained by a habit of maintaining it, and that habit would need its own maintaining, and there is no floor to that. Habit is what carries a fixation and habit is what carries an attainment; it does not become a different faculty at the top of the ladder.\n\nThere is also something that looks like the summit and is not. Clarity is detachment without distraction. Detachment in one realm can look, from outside, like clarity in both.\n\nCalm in one realm can come without any training. A person whose fixation in a realm is detached gives the detached phase of thoughts about that realm more attention than an enthusiastic or cautious person does. Training to abide in the detached phase does the same on purpose. While nothing is disturbing a person detached in a realm, nothing in that realm pulls at the person, and nothing shows whether the person would reach for a distraction if something did. Observers can take the calm for clarity in both realms.\n\nEvery thought passes through the detached phase, whatever a person's fixation. A person can train themselves to abide in the detached phase, giving the detached phase more attention than their fixation would give it. The training can be done for thoughts about one realm and not the other. No orientation is trained, and the person's type does not change.\n\nObservers see the marks of the training in one realm and take the person to be like that throughout. What observers recognize as holiness is mostly these marks — austerity, fearlessness, unconcern with comfort and pain, a steadiness nothing seems to shake. The marks are real, and the mistake is the observers'. In every case the attainment is real. The counterfeit summit is a genuine, hard-won attainment in one realm, wearing the visible marks of the whole one, with the person's other realm running entirely unchecked behind the attainment. What can differ is whether the person makes use of how others read the attainment.\n\nTake a person trained to work on a bleeding body, or to keep moving under fire. At such a moment the person abides in the detached phase of thoughts about physical matters, and does not flinch or look away. The training is real, and so is the steadiness. The person reaches for the training when fear would get in the way, and uses the training as a tool at those moments. Nothing about the person's type has changed.\n\nPain, hardship and danger no longer move the person, and the person shows no fear of harm or of death. Observers take that fearlessness as a sign of clarity about the inner life as well. The training has not touched the person's psychic realm. The person still has the wants they had before about psychic matters, such as wanting to be admired or to be seen as righteous. The person may then present the fearlessness as the summit on purpose, because being taken for someone at the summit brings admiration and followers. Presenting the fearlessness that way is a fraud.\n\nTake a person trained to sit with someone in the worst hour of their life and stay level, hearing what is said without being pulled into it. At such a moment the person abides in the detached phase of thoughts about psychic matters. Again the training is real, and again it is a tool used at moments. Nothing about the person's type has changed here either.\n\nSuch a person is no longer moved by praise, blame or other people's feelings. The person still wants money and comfort as before. The steadiness lets the person pursue those wants among other people without being moved by what those people feel. Others take the steadiness for the summit. Presenting the steadiness that way on purpose is a fraud as well. Nothing in the person checks what the attainment is used for.\n\nConscience is caution in the psychic realm: understanding the disadvantages of hurting others. For a person cautious in the psychic realm, conscience is their own fixation at work. While the person abides in the detached phase of thoughts about psychic matters, conscience is not raised. When the person stops abiding, conscience is there as before. A person enthusiastic in the psychic realm examines little of what their wants would do to others, so whatever conscience the person has was learned as a rule. A person who works for long without the rule may stop invoking the rule, and then stop having it. If that happens, the long working without the rule is the cause, and the training is not.\n\nIt would be reasonable to expect that training to abide in the detached phase weakens the person's fixation in the trained realm, when the fixation is enthusiastic or cautious. An enthusiastic fixation and a cautious fixation are both ways of engaging with a realm, and abiding in the detached phase works against engaging.\n\n### Why trying harder", 'Summit rearranged (RELAY 20261110, [A] 17:19, 17:29)')
once('It is experienced as clarity, and from where they stand that is precisely what it is.',
     'It is experienced as clarity.', 'Five clarity (RELAY 20261110, [A] 17:20, 17:23)')

insert_after_heading("### The summit, and what counterfeits it", "Something else is often mistaken for the clarity at the top: detachment in one realm, which can look from outside like clarity in both. The detachment may come with a person's type, or from training for thoughts about one realm, and either way the detachment is in one realm only. A person may present a trained steadiness as the summit on purpose, to be admired or to pursue wants the training never touched.", "Summit opening (RELAY 20261110b, [A] 17:56)")

once('It could not be held in any case, and the reason is the same one that runs the whole book.',
     'It could not be held in any case.', 'summit book-reference cut (11-11)')

once('The signal works by producing its copy in whoever is near. All of this is automatic, and none of it is a fault.\n\n',
     "The signal works by producing its copy in whoever is near. All of this is automatic, and none of it is a fault.\n\nSome of an infant's fears are instinctual: a situation sets them off directly, with no want behind them. The fear of being abandoned may be one of them. An infant can do nothing about such a fear, so relief has to come from a parent. When the fear is repeated and no relief comes, the fear is buried, and a buried fear from infancy can have major consequences in adult life.\n\n", 'Two channels instinctual fears (RELAY 20261103, 11-11)')

once('Descent is fear turned into want, over and over, each level a strategy for coping with the one above it. Descent is seeded at the top by the basic fear. Like every fear, the basic fear has a want behind it. Descent ends at the bottom when the basic fear is finally realized.',
     "Each step down a level is a fear turned into a want, and the step takes many thoughts. Each time the fear above comes up, the person turns away from the fear once more, until the connection between the fear and the want is no longer noticed and the want is wanted for its own sake. The want then brings a fear of its own, the fear of failing at the strategy. When that fear is turned away from in its turn, the next step down begins. Descent is the gradual accumulation of turning away. Fears are turned away from until they are no longer noticed, and each is replaced by a fear that a more limited want will fail. Descent is seeded at the top by the basic fear. Riso and Hudson describe every type's basic fear as a variant of the fear of not existing. Behind the basic fear is the imaginary self's want to go on existing. The basic fear is close to an infant's instinctual fear of being abandoned, and is what the infant's fear becomes once there is a self. Both are a fear of helplessness in the face of the future. Descent ends at the bottom when the basic fear is finally realized.", "descent paragraph (RELAY 20261111 [A] 09:33; RELAY 20261103 item 2; 'Like every fear' out per 11-03)")

once('Ignoring does not move a person down, because an ignored fear stays in view.\n\n',
     'Ignoring does not move a person down, because an ignored fear stays in view.\n\nRiso and Hudson describe the same step as succumbing to a fear: a person who "succumbs to the fear" at one level "will pursue a compensating desire" at the next (*Personality Types*, p. 474). Succumbing to a fear (which Riso and Hudson do not define) is turning away from the fear: the fear is not settled, and the person turns away from the fear each time the fear comes up, until the fear is no longer noticed. Turning away is what moves a person down.\n\n', 'succumbing paragraph (RELAY 20261111b, yes 11-11)')

once('*Given up on* — the want behind the fear is dropped, and with the want gone the fear is gone with it. Giving up a want sometimes leaves something behind.',
     '*Given up on* — the want behind the fear is dropped, and with the want gone the fear is gone with it. Where the want is to be rid of something, giving up the want means accepting that the thing may come. An instinctual fear has no want behind it, so an instinctual fear cannot be given up on. Giving up a want sometimes leaves something behind.', 'Given up on (RELAY 20261103 item 3, yes 11-11)')

once('Ignoring does not leave the fear, and it does not leave the want behind the fear.',
     'Ignoring does not leave the fear, and where a want is behind the fear, ignoring does not leave the want either.', 'line 1290 (RELAY 20261103 item 4, yes 11-11)')

open(OUT, "w", encoding="utf-8").write(t)
print("ok", OUT)
