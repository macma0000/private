"""Build the draft of Chapter 10, reframed around integration and disintegration (RELAY-from-job99-20261106b.md).

Reads the working master, writes ch10-draft.md (the new chapter) and BOOK2-ch10.md (the working master with it).
"""
import re

SP = "/tmp/claude-0/-home-user-private/08506865-a31e-5a6b-9772-f4733aaf6b07/scratchpad"
t = open(SP + "/working/BOOK2-working.md", encoding="utf-8").read()
a = t.index("## Chapter 10: The Figure's Own Lines\n")
b = t.index("## Chapter 11: Leans, and the Classical Wings\n")
ch = t[a:b]


def once(s, old, new, label):
    n = s.count(old)
    assert n == 1, (label, n)
    return s.replace(old, new)


# Title.
ch = once(ch, "## Chapter 10: The Figure's Own Lines\n", "## Chapter 10: Integration and Disintegration\n", "title")

# The opening (RELAY 20261106b item 4, approved 16:11), then the first paragraph led by the two directions (item 2).
opening = ("The classical Enneagram gives each type a direction of integration and a direction of disintegration, and draws both as arrows on two shapes, the triangle and the hexad. "
           "Both directions and both shapes follow from three orientations in two realms. "
           "When stress is low, a person shifts a little toward the types a step ahead of their own type, in one realm or in both, which is integration. "
           "Under stress, a person shifts a little toward the types a step behind instead, which is disintegration. "
           "The triangle joins the three aligned types, each a step ahead of the next in both realms, and the hexad joins the six mixed types, each a step ahead of the next in one realm, with the two realms taking turns. "
           "Twelve more one-step relations run between the mixed types and the aligned types, and the classical figure draws none of the twelve, though a person seems to shift a little toward those types too. "
           "A person who holds their orientation in a realm less strongly has some of the orientation a step ahead available, and so comes to resemble the type ahead in that realm while keeping their own type.")
old_first = ("The classical Enneagram draws two shapes inside its circle: a triangle joining 3, 6 and 9, and a six-pointed figure joining the other six. "
             "Arrows run along both, marking the directions a person is said to move under growth and under stress. "
             "Which type connects to which is simply given.")
new_first = ("In the classical Enneagram, every type has a direction of integration, which a person is said to move in when stress is low, and a direction of disintegration, which a person is said to move in under stress. "
             "The arrows for both directions run along two shapes inside the circle: a triangle joining 3, 6 and 9, and a six-pointed figure joining the other six. "
             "Which type connects to which is simply given.")
ch = once(ch, "## Chapter 10: Integration and Disintegration\n\n" + old_first,
          "## Chapter 10: Integration and Disintegration\n\n" + opening + "\n\n" + new_first, "opening + first paragraph")

# The types ahead and behind: disintegration's definition moves here from Reading it from either end.
disint_def = ("Disintegration is the same lines read backward. Behind replaces ahead throughout, each realm shifting a little toward the orientation behind it rather than the one ahead, "
              "and the two shapes close in the reverse order. The classical figure marks both directions on the same lines, for the same reason.")
ch = once(ch, "### The types ahead\n\nIntegration is the forward direction around the cycle of orientations, and one step forward in a realm is what ahead means. The types a person integrates toward are therefore the types ahead of them.\n\n",
          "### The types ahead and behind\n\nIntegration is the forward direction around the cycle of orientations, and one step forward in a realm is what ahead means. The types a person integrates toward are therefore the types ahead of them.\n\n" + disint_def + "\n\n",
          "types ahead and behind")
ch = once(ch, "Every type has three types ahead of it.", "Every type has three types ahead of it and three behind it.", "three behind")
ch = once(ch, "So a Nine integrates toward the Seven or the Two by a single step, and toward the Three by a double one.",
          "So a Nine integrates toward the Seven or the Two by a single step, and toward the Three by a double one. "
          "Read backward, the types a single step behind the Nine are the Five in the physical realm and the Four in the psychic, and the type a double step behind is the Six.",
          "Nine behind")

# The relations the figure does not draw (RELAY 20261106, approved 15:18).
ch = once(ch, "as that grip loosens they come to resemble those types more closely. That is what the classical arrows have always described.\n\nIf that is what an arrow reports, then it should hold wherever the relation holds.",
          "as that grip loosens they come to resemble those types more closely. When stress is low, a person also shifts a little toward those types for a while. "
          "The classical arrows describe both changes: the lasting one as the grip loosens, and the passing one when stress is low.\n\n"
          "If the arrows report the two changes, then the two changes should hold wherever the relation holds.", "arrows describe both")

# Integration, type by type: renamed, with the Three, the Six and the Nine added in numeric order.
ch = once(ch, "### As the grip loosens\n", "### Integration, type by type\n", "integration heading")
three_int = ("A Three less caught in the physical realm can stay with an attempt that fell short instead of turning to the next one. The type ahead of a Three in that realm is the Eight. "
             "A Three less caught in the psychic realm notices when an achievement fails to settle the question of their own worth. The type ahead there is the One. "
             "A Three less caught in both realms comes to resemble the Six, the type a double step ahead.")
six_int = ("A Six less caught in the physical realm can tell when enough has been checked. The type ahead of a Six in that realm is the Four. "
           "A Six less caught in the psychic realm can let a worry come to a stop instead of compounding. The type ahead there is the Five. "
           "A Six less caught in both realms comes to resemble the Nine, the type a double step ahead.")
nine_int = ("A Nine less caught in the physical realm notices what is there, and can then want something and act on it. The type ahead of a Nine in that realm is the Seven. "
            "A Nine less caught in the psychic realm notices a conflict and can then enter it. The type ahead there is the Two. "
            "A Nine less caught in both realms comes to resemble the Three, the type a double step ahead.")
ch = once(ch, "\n\nA Four less caught in the physical realm", "\n\n" + three_int + "\n\nA Four less caught in the physical realm", "Three")
ch = once(ch, "\n\nA Seven less caught in the physical realm", "\n\n" + six_int + "\n\nA Seven less caught in the physical realm", "Six")

# Disintegration, type by type: new, before Reading it from either end, which keeps only its second paragraph.
dis = open(SP + "/ch10/disintegration.md", encoding="utf-8").read().strip()
m = re.search(r"\n### Reading it from either end\n\n(Disintegration is the same lines read backward\..*?)\n\n(The correspondence can be read from either end\..*?)\n", ch, re.S)
assert m, "reading section"
ch = ch[:m.start()] + "\n\n" + nine_int + "\n\n" + dis + "\n\n### Reading it from either end\n\n" + m.group(2) + "\n" + ch[m.end():]

# RELAY 20261104 ([A] 19:34): why a person goes ahead of the center more often.
ch = once(ch, "goes ahead of the center more often than behind it, because ahead is the direction of the step.",
          "goes ahead of the center more often than behind it, because a fixation holds a person back from the orientation ahead. The person cannot easily bear what the next phase would bring. A less caught person can bear more of what the next phase would bring, and so goes ahead more easily.", "going ahead")

# [A] 11-07: integration as a shift toward the orientation one step forward.
ch = once(ch, "Integration is the forward direction around the cycle of orientations, and one step forward in a realm is what ahead means.",
          "Integration is the forward direction around the cycle of orientations: a shift toward the orientation one step forward. One step forward in a realm is what ahead means.", "integration shift")

# RELAY 20261106c item 2 ([A] 19:22), with Job105's join and "failing to get rewarded" in plain words ([A] 11-07 yes).
ch = once(ch, "What being less caught changes is how easily a person leaves the center and returns.\n\n",
          "What being less caught changes is how easily a person leaves the center and returns.\n\n" + 'A less caught person can bear more of what the next orientation brings, and so can anyone when stress is low. Where a person is enthusiastic, the person can bear the examining, even when the examining shows that the hoped-for reward may not come. Where a person is cautious, the person can bear losing control, and lets fears be settled. Where a person is detached, the person can bear a want arising, and the fears a want can bring.' + "\n\n", "integration matching paragraph")

open(SP + "/ch10/ch10-draft.md", "w", encoding="utf-8").write(ch)
full = t[:a] + ch + t[b:]
full = full.replace("10. The Figure's Own Lines[[#Chapter 10 The Figure's Own Lines]]", "10. Integration and Disintegration[[#Chapter 10 Integration and Disintegration]]", 1)
open(SP + "/ch10/BOOK2-ch10.md", "w", encoding="utf-8").write(full)
print("ok")
