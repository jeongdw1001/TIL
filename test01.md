user@JEONGDABIN MINGW64 ~ (master)
$ mkdir TIL2

user@JEONGDABIN MINGW64 ~ (master)
$ cd TIL2

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git init
Initialized empty Git repository in C:/Users/user/TIL2/.git/       

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git status 
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "UXUI\355\212\271\352\260\225.md"

nothing added to commit but untracked files present (use "git add" 
to track)

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git add .

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git commit -m "20221231 14:30"
[master (root-commit) 80c400f] 20221231 14:30
 1 file changed, 46 insertions(+)
 create mode 100644 "UXUI\355\212\271\352\260\225.md"

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git log --oneline
80c400f (HEAD -> master) 20221231 14:30

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git remote add origin https://github.com/jeongdw1001/TIL2.git    

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git remote -v
origin  https://github.com/jeongdw1001/TIL2.git (fetch)
origin  https://github.com/jeongdw1001/TIL2.git (push)

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git status 
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)       
  (use "git restore <file>..." to discard changes in working directory)
        modified:   "UXUI\355\212\271\352\260\225.md"

no changes added to commit (use "git add" and/or "git commit -a")  

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 1.54 KiB | 525.00 KiB/s, done.        
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/jeongdw1001/TIL2.git
 * [new branch]      master -> master

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git add .

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git commit -m "20221231 14:35"
[master a3d62fb] 20221231 14:35
 1 file changed, 2 insertions(+), 2 deletions(-)

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git log --oneline
a3d62fb (HEAD -> master) 20221231 14:35
80c400f (origin/master) 20221231 14:30

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git status
On branch master
nothing to commit, working tree clean

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git remote -v
origin  https://github.com/jeongdw1001/TIL2.git (fetch)
origin  https://github.com/jeongdw1001/TIL2.git (push)

user@JEONGDABIN MINGW64 ~/TIL2 (master)
$ git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes | 109.00 KiB/s, done.       
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jeongdw1001/TIL2.git
   80c400f..a3d62fb  master -> master