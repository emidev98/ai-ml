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

If you want to run the project this are the freez dependencies that I used
```bash
bokeh==2.0.2
Jinja2==2.11.2
MarkupSafe==1.1.1
numpy==1.18.4
packaging==20.4
Pillow==7.1.2
pyparsing==2.4.7
python-dateutil==2.8.1
PyYAML==5.3.1
six==1.15.0
tornado==6.0.4
```