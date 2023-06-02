cd git-practice-03

git branch branch1
git branch branch2
cp dir3/bar dir3/bar_copy
git add .
git commit -m 'for main'

git checkout branch1
mv dir1/dir2/foo dir1
rm -r dir1/dir2
touch newfile1
git add .
git commit -m 'for branch1'

git checkout branch2
mv dir1/dir2/foo dir1/dir2/foo_modified
rm dir3/bar && touch dir3/newfile2
git add .
git commit -m 'for branch2'

