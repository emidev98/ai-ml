# How to create a project

The virtual environments are important for Python because otherwise we will run in the global environment and it is a bad practice.

The next command will create a Python virtual environment inside the current directoy.
> py -m venv env

The next command will activate the virtual environment
> source env/Scripts/activate

To install **bokeh** library inside the virtual environment once we activated it we should use the next command
> pip install bokeh

Finally to exit the virtual environment we can use the next command
> deactivate