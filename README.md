#Greengraph
This is a program which plots a graph quantifying the amount of green land between two locations on Earth.
It does this by counting the number of green pixels in a series of satellite images between the two locations.

##Installation
To install from source run `python setupy.py install`. Or to install from github use `pip install
git+git://github.com/MikeVasmer/GreenGraphCoursework`. To uninstall run `pip uninstall greengraph`
if installed using pip or manually delete the files if installed using `setup.py`.

##Usage
Once installed run the program using the command `greengraph`. The usage is as follows:
`greengraph [--help] [--start START] [--end END] [--steps STEPS] [--out OUT]`
The `--help` flag prints usage instructions. The `--start` flag specifies the starting location (default London).
The `--end` flag specifies the ending location (default Durham). The `--steps` flat specifies the number of
steps (default 10). The `--out` flag specifies the output file name `file`, saved as `file.png`.
Example: `greengraph --start London --end Birmingham --steps 5 --out LonBir` will produce an image 
`LonBir.png` containing the graph.
