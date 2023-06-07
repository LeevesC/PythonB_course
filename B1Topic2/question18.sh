cd git-practice-04
git branch -a

for branch in $(git branch -r | grep 'ready'); do
    git branch ${branch#origin/} $branch
done

git merge ready1
git merge ready2
git merge ready3

git branch -d ready1
git branch -d ready2
git branch -d ready3

git branch update1
git merge update1

git branch update2
git merge update2
