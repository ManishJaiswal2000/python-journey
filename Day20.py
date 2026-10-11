# Day 20: GitHub and git push

# 📝 Steps

# Step 1: Create an account at github.com with a personal email.

# Step 2: Create a repository. Click New repository and name it python-journey. Leave it empty: don’t tick README, .gitignore or a license, because you already have them. Click Create repository.

# Step 3: Copy the repository URL GitHub shows (it ends in .git).

# Step 4: Connect and push. In your terminal, inside the project folder:

# git remote add origin <your-URL>
# git branch -M main
# git push -u origin main

# Step 5: Refresh the GitHub page and look at your files and commit history.

# 🔍 What each command does
# Command	Meaning
# git remote add origin <URL>	Names the GitHub copy origin
# git branch -M main	Renames master to main, the current default
# git push -u origin main	Sends your commits and links the two branches


# ⚠️ Things to know
# A sign-in window may open. Complete the login in the browser and the push continues.
# Never share your password or any token with anyone, including me.
# Your email is public in commits. Your commits use manishjai906@gmail.com. If you’d prefer to hide it, use GitHub’s “noreply” address under Settings → Emails. Old commits keep the old email.
# Use your personal laptop only for this.


# 🧪 Challenge
# Edit one line in README.md, commit it, then run git push. It’s now a single command, because -u linked the branches.
# On GitHub, open the commits page and find your very first commit.
# Check that best_score.txt is not on GitHub. That proves .gitignore works.