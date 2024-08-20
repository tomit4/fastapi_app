# FastAPI App

## Introduction

This repository contains a bare bones starter template for a backend using
[FastAPI](https://fastapi.tiangolo.com/)

**PreRequisite Dependencies:**

To use this as a basic template for future projects, you'll first need to have
[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
[python](https://www.python.org/downloads/),
[rye](https://rye.astral.sh/guide/installation/) installed.

You'll also probably want to have a basic familiarity with the command line
(examples here are in
[bash](https://www.gnu.org/software/bash/manual/bash.html)).

**Getting Started:**

Once those are installed, you can clone this repository in a directory of your
choosing:

```sh
git clone https://github.com/tomit4/fastapi_app &&\
cd fastapi_app
```

You'll also need to simply copy the included `env-sample` file as a `.env` to
adjust from the default `HOST` and `PORT`:

```sh
cp env-sample .env
```

Once cloned and inside the project's directory. go ahead and use rye to initiate
the virtual environment (defaults to a `.venv` directory):

```sh
rye sync
```

This will also install all necessary dependencies needed. After that, you'll
need to instantiate your virtual environment like so:

```sh
source .venv/bin/activate
```

After that, you can run the server itself using the `dev` script:

```sh
rye run dev
```

The default port utilized for this template is 5173. So once you see the
fastapi-cli's output, indicating successful startup of the server, you can
simply navigate in your browser to localhost:5173/docs to see the OpenAPI
documentation of the app.

### About The App

This App is just a template, but can be utilized as a model on how to organize
future applications/projects.

**The Rye Package Manager**

This project utilizes the modern python project/package manager
[Rye](https://rye.astral.sh/). Please see their
[Installation Instructions](https://rye.astral.sh/guide/installation/) if you
don't have it installed.

While the official [User Guide](https://rye.astral.sh/guide/) should provide you
with all the information you'll need to get started using Rye, Here are a few
common commands you might find yourself needing to use throughout building your
application

```sh
# Adding a package
rye add package_name
# Removing a package
rye remove package_name
# Adding a dev dependency
rye add --dev package_name
# Removing a dev dependency
rye remove --dev package_name
# Syncing Your Project With The Virtual Environment
# (run after installing/uninstalling dependencies)
rye sync
```

Should you find yourself ready to build/publish your application, please consult
Rye's Official Documentation on
[Building and Publishing](https://rye.astral.sh/guide/publish/).

**SQLAlchemy**

This App template uses the [SQLAlchemy ORM](https://www.sqlalchemy.org/), and
thusly can utilize any of the classic SQL databases including [SQLite](),
[Postgresql](https://www.postgresql.org/), [MySQL](https://www.mysql.com/) &
[MariaDB](https://mariadb.org/),
[Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Introduction-to-Oracle-SQL.html),
and [MS-SQL](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).

**Static Files**

FastAPI provides for use of static files very easily. To serve static files,
place them in the `public` folder. The server is set up to serve any static
files placed here by default. To view them in your browser, simply enter the url
<em>localhost:5173/public/<b>name_of_your_file.jpg</b></em> and you should see
your file displayed there.

Provided with this template is a sample jpeg of a cherry you can view from your
browser while the server is running. Simply visit
<em>localhost:5173/public/cherry.jpeg</em>

Should you wish to know more about static files in FastAPI, please see their
[tutorial on the subject](https://fastapi.tiangolo.com/tutorial/static-files/).

**Testing**

FastAPI favors using [pytest](https://docs.pytest.org/en/stable/) to run unit
tests for FastAPI applicactions. If you wish to run the tests, don't utilize
`pytest` directly. Instead, simply invoke `rye test` to run them (uses `pytest`
under the hood, do <em>not</em> invoke `pytest` directly as that will error out
when trying to import dependencies):

```sh
rye test
```

**Editor Tooling**

This project utilizes some additional editor tooling for use with python. These
include:

- [black](https://black.readthedocs.io/en/stable/index.html)
- [isort](https://pycqa.github.io/isort/)
- [pyright](https://github.com/microsoft/pyright)

You can install the [VSCode](https://code.visualstudio.com/) extensions via your
editor or you can download them directly from the
[Visual Studio Marketplace](https://marketplace.visualstudio.com/):

- [black](https://marketplace.visualstudio.com/items?itemName=mikoz.black-py)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [pyright](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)

Additionally, the Neovim equivalents can be downloaded directly, downloaded
using a extensions tool like
[Mason](https://github.com/williamboman/mason.nvim):

- [black](https://github.com/averms/black-nvim)
- [isort](https://github.com/stsewd/isort.nvim)
- [pyright](https://www.andersevenrud.net/neovim.github.io/lsp/configurations/pyright/)

I personally use [Neovim](https://neovim.io/) and an all in one formatter,
[conform](https://github.com/stevearc/conform.nvim).

## Conclusion

This is the most organized workflow I've found using FastAPI (or any Python
project for that matter). There are more features I plan on adding to this
template like the [Alembic](https://alembic.sqlalchemy.org/en/latest/) database
migration tool, as well as templates for working with
[OAuth2 and JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/).
This repository is mainly meant for my own personal use for scaffolding off of
into future projects, but perhaps you, dear reader, might also find it useful.
