#Day 21: Branches

# 📝 Steps

# Step 1: Check where you are.

# git status
# git branch

# You should be on main with a clean tree. The * marks your current branch.

# Step 2: Create and switch to a new branch.

# git switch -c add-difficulty

# Run git branch again. You should now see * add-difficulty.

# Step 3: Make a small change in Guessing_Game.py. For example, let the player choose 5 or 7 tries at the start. Keep it small, and run it to confirm it works.

# Hint: the 7 in while attempt <= 7: is the limit. What if that came from a variable, such as max_tries, that the player sets at the start? Use get_number() style validation if you want to check the choice, or just ask with input and keep it simple.

# Step 4: Commit it with a clear message:

# git add Guessing_Game.py
# git commit -m "Let player choose number of tries"

# Step 5: Test your prediction. Run a plain git push and read the message. Then use the command Git suggests:

# git push -u origin add-difficulty

# Step 6: Merge into main.

# git switch main
# git merge add-difficulty
# git push

# Step 7: Look at the result.

# git log --oneline
# git branch
# 🧪 Challenge

# Make a second branch, change something, then delete it without merging:

# git switch -c experiment
# git switch main
# git branch -D experiment

# Notice that main never saw those changes.