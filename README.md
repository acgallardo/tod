`$ todo_`
============

todo is a command line todo app for `unix`. It stores all the tasks in a sqlite database and you can interact with the app using the terminal (see Usage).

### Installation:
`todo` can be installed from pypi using `pip install pytodo`.

### Usage:
```
Usage:
  t  add <task>
  t  check <id>
  t  uncheck <id>
  t  clear
  t  count
  t  ls [--all]
  t  -h | --help
  t  --version

Commands:
  add           Add a new task
  check         Check a new task as done
  uncheck       Uncheck a task as done
  clear         Refresh the database
  ls            List all tasks

Options:
  -h --help     Show this screen.
  --version     Show version.
  --all         List all tasks
```
- Add a task using, `$ t add "Buy Bugatti Veryon"` (a string is passed in)
- Check as task as done by specifying the id, `$ t check 1`
- Uncheck a task again by, `$ t uncheck 1`
- List all pending tasks, `$ t ls`
- List all tasks, `$ t ls --all`
- Flush the database, `$ t clear`
- For more help, `$ t --help`

License:
---------
`todo` is distributed under MIT license, see `LICENSE` for more details
