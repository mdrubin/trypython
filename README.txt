No proper documentation yet, sorry.

To run this demo you need to first generate the xaml for the tutorial.

This requires rst2xaml on your path and runs under CPython (version 2.5 or more recent) rather than IronPython.

* http://code.google.com/p/rst2xaml/

You may well have to use the latest version of rst2xaml from SVN rather than a released version...

With this in place run:

    ``python maketutorial.py``
    
Once the tutorial files are in place you should start Chiron which will serve the application locally. This works under both Mono and .NET. Run either silverlight.bat or silverlight.sh. This should automatically open a browser to show the application.

If you change the ReStructured Text source files in the 'tutorial' directory and run maketutorial.py then new xaml files will be generated for the new source documents.