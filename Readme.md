# Django based app, that lets you save name and email adress to a SQLite database.

## Used versions and tools

* Tested with Python 3.6.3 .
* Written with Visual Studio Code.
* Tested with Google Chrome 64.0.3282.186 and Safari 11.0.3.
* Version control through GitHub Desktop.
* The Django built in support for SQLite was used.

## About the code

### Settings

* Local time is set to UTC.
* Sensitive settings were removed from the settings.py and put into an alternative file, which is not served to GitHub.
* If the app is tested with the Django dev server: debug has to be set to true. Alternatively the dev server can be run with '--insecure'.

### Structure

* This Django project has only one included app: leadsDatabase. Its called leadsDatabase, because the information of a potential customer in marketing is often called a 'Lead'.
* The app leadsDatabase contains one model: A lead. A lead contains a name and an email adress. (see models.py)
* The app leadsDatabase contains various views (views.py). Every function in the views.py corresponds to one of the pages, that can be accessed in the browser. E.g. the function list(request) corresponds to the page, where a list/table of all currently saved leads are shown.
* Each view has its own template. All template inherit from a base template. The file inputButtons.html is not used as a template but included in other templates.
* A style.css is served as a static file and included in the base.html template. It styles all elements of all templates. For a larger project, it would make sense to spread the stylesheet over different files.
* SQLite is used as a database. In this case we do not need user management, so we don't need to use a more complex database. Performance could be an issue if we had high write volumes, which we probably do not have in this case. It is also natively built into Django and can be accessed with low additional complexity.

### Additional comments are in the code... See especially files in '/leadsDatabase/'

