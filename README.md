# J4462 crime project

Cheat sheet time! So, so many of the problems folks were having when I was in Columbia last week
were related to individualized computer setups, version conflicts, and other things that have very 
little to do with the code we're here to learn.

On one hand, that's great. It gives you exposure to some of the real frustrations that come with programming.
The problems you encounter aren't just going to be limited to code; they're going to come from all kinds of
sources. On the other hand, the code is much, much more interesting.

SO. Here's what we're going to do. First, everyone should install this app by typing the following into their
command line. First, navigate to your Desktop (or working area of choice). Then copy and paste this and press enter:

**git clone git://github.com/cjdd3b/crime-j4462.git newcrime**

You should see a new folder called newcrime that will contain a bunch of files you're probably pretty familiar
with by now. This is a working copy of the entire application we're trying to build, and from now on we'll be
working from this to prevent things like path and dependency issues.

Just to make sure it works, go into the new directory and run your server (python manage.py runserver) then visit
127.0.0.1:8000 and you should (hopefully) see a list of crimes. If you don't, let me or Ted know!