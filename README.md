# software-construction

Build systems, or rather the systems that construct software from source code is a complex area. 
I feel I need to know more about how software is constructed. Not because Im unfamilar, but rather to build more expertise.
Quite often I find that build systems (and build tools) are considered a means to an end, that is, to make the code useable, it must be built.
This often starts simple in that we are building a few source files into one or more executable binaries, and those are copied in place and run.
As software projects expand, the build system often expands. I assert that this expansion add more build time, and that makes developers sad. 
Developers then try to make themselves happier by making the build system faster, which would commonly start with parallelization.
So yay, now that everything is running in parallel then it takes the same net time as the build took when it was just one binary.
All is well until there becomes a need for one thing that is getting built, become dependant on another thing that is being build. 
With dependencies added, how we have the beginnings of a graph and that expands to many nodes and branches.
At some point, such as when we have multiple developers, many of which are working on their own schedule and their own features, a local build isnt enough.
Now enters the need to schedule the build starts.

And so it goes. We've gone from a few text files and one or more tools to run, to a set of files that are changing all the time in lots of different ways and scheduling and maybe even doing things like zipping up a set of the resultant files, and maybe moving around some of those files into a strucutre, and maybe even some config files that need to have specific content and location. Maybe a developer has spent time to auto-generate those config files, which is very useful when there are new items being added that need to be configured and so on.  

Now, before we know it, we have a pipeline.


