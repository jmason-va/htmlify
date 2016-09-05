# htmlify

- a group of functions that take in any type of file, convert it to an html file and style it
- a replacement file which is basically a python dictionary, the keys will be replaced with the values
- a publish script that will continually publish your files to a published directory and serve it to your browser (currently only chrome supported)

please add the following to your profile/bash_profile/zshrc/etc
`alias book='chrome ~/path/to/indexfile.html; ~/path/to/htmlify/publish.sh'`
