story_template = (
    "Today I went to the zoo. I saw a(n) {adjective1} {animal1} jumping up and down in its tree. "
    "He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun1}. "
    "I got some peanuts and passed them through the cage to a gigantic gray {animal2} towering "
    "above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop "
    "of ice cream. It filled my stomach. Afterwards, I had to {verb2} {adverb2} to catch our bus. "
    "When I got home I {past_tense_verb} my mom for a {adjective4} day at the zoo."
)
adjective1 = input("Enter an adjective: ")
animal1 = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
adverb1 = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
animal2 = input("Enter another animal: ")
adjective3 = input("Enter another adjective: ")
verb2 = input("Enter another verb: ")
adverb2 = input("Enter another adverb: ")
past_tense_verb = input("Enter a past tense verb: ")
adjective4 = input("Enter one last adjective: ")
story = story_template.format(
    adjective1=adjective1,
    animal1=animal1,
    verb1=verb1,
    adverb1=adverb1,
    adjective2=adjective2,
    noun1=noun1,
    animal2=animal2,
    adjective3=adjective3,
    verb2=verb2,
    adverb2=adverb2,
    past_tense_verb=past_tense_verb,
    adjective4=adjective4
)


print("\nHere's your Mad Libs story:\n")
print(story)