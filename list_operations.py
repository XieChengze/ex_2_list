participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements

if len(participants) != len(scores):
    print("not same length")
else:
    print("same length")

# First, display all the current participants with their scores. Use zip()
print("")

zipped_data = zip(participants,scores)
zipped_list = list(zipped_data)
print(zipped_list)

# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
print("")

new_name = "a"
new_score = "66"

if new_name is None:
    print("name is none")
elif not new_score.isdigit():
    print("score is not digit")
else:
    new_score2 = int(new_score)
    if not (0 <= new_score2 <= 100):
        print("error, number must be 0 to 100")
    elif new_name in participants:
        print(f"error, '{new_name}' exist")
    else:
        participants.append(new_name)
        scores.append(new_score2)
        print(f"Success, name: '{new_name}' scores: {new_score2}")


# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
print("")

search_name = "Chen Wei"

if search_name in participants:
    idx = participants.index(search_name)
    sor = scores[idx]
    print(f"name: {search_name} ,score: {sor}")
    if sor > distinction_score:
        print("DISTINCTION")
    elif sor > qualification_score:
        print("QUALIFIED")
    else:
        print("NOT QUALIFIED")
else:
    print(f"Without {search_name}")


# Display every participant's name, score, and whether they are qualified or not. 
print("")

for name, score in zip(participants, scores):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f" name: {name}  score: {score}   {status}")



# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
print("\n")

any_distinction = any(score > distinction_score for score in scores)

all_passed = all(score >= 50 for score in scores)


# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
print("")

update_name = "Hana Lee"
update_score = "88"

if update_name in participants:
    update_score_int = int(update_score)
    if not (0 <= update_score_int <= 100):
        print("error: number is 0 to 100")
    else:
        idx = participants.index(update_name)
        scores[idx] = update_score_int
        print(f"{update_name} new score is {update_score_int}")
else:
    print(f"error: not find '{update_name}'")


# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
print("")

remove_name = "a"

if remove_name in participants:
    idx = participants.index(remove_name)
    removed_score = scores[idx]
    participants.pop(idx)
    scores.pop(idx)
    # removed_score = scores[idx]
    print(f"name {remove_name} score {removed_score} is remove")
else:
    print(f"error: can not find {remove_name}")


# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
print("")

scoreboard = sorted(zip(participants, scores), key=lambda x: x[1],reverse=True)

for i,(name,score) in enumerate(scoreboard,start=1):
    
    print(f"{i}. {name} {score}")
    


# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
print("")

max_score = max(scores)

min_score = min(scores)

avg_score = sum(scores) / len(scores)


max_count = scores.count(max_score)

min_count = scores.count(min_score)



distinction_count = 0
qualified_count = 0
not_qualified_count = 0

for s in scores:
    if s > distinction_score:
        distinction_count = distinction_count + 1
    if s > qualification_score:
        qualified_count = qualified_count + 1
    else:
        not_qualified_count = not_qualified_count + 1


# not_qualified_count = len(scores) - qualified_count

# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
print("-----------list------------")

for i, (name, score) in enumerate(scoreboard, start=1):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"{i}. name: {name} score: {score} status: {status}")


print(f"max score is {max_score}")
print(f"min score is {min_score}")
print(f"avg score is {avg_score}")
print(f"max score count is {max_count}")
print(f"min score count is {min_score}")
print(f"distinction: {distinction_count}")
print(f"qualified: {qualified_count}")
print(f"not qualified: {not_qualified_count}")


