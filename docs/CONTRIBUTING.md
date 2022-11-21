## Development and Contributing

## Issue

To make an improvement, add a new feature or anything else, please open a issue first.

**Good first issues are the issues that you can quickly solve, we recommend you take a
look.**
[Good first issue](https://github.com/hakancelikdev/{{project-name}}/labels/good%20first%20issue)

## Fork Repository

[fork the {{project-name}}.](https://github.com/hakancelikdev/{{project-name}}/fork)

## Clone Repository

```shell
$ git clone git@github.com:<USERNAME>/{{project-name}}.git
$ cd {{project-name}}
```

## Setup Branch

```shell
git checkout -b i{your issue number}
```

## How to Update My Local Repository

```shell
$ git remote add upstream git@github.com:hakancelikdev/{{project-name}}.git
$ git fetch upstream # or git fetch --all
$ git rebase upstream/main
```

## Testing

Firstly make sure you have py3.8, py3.9, py3.10 and py3.11 python versions installed on your
system.

After typing your codes, you should run the tests by typing the following command.

```shell
$ python3.10 -m pip install tox
$ tox
```

If all tests pass.

## The final step

After adding a new feature or fixing a bug please report your change to
[changelog.md](CHANGELOG.md) and write your name, GitHub address, and email in the
[authors.md](AUTHORS.md) file in alphabetical order.

### Changelog Guide

```
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - YYYY-MM-DD

### Added | Fixed | Changed | Removed
- [{Use the emoji below that suits you.} {Explain the change.} @{Add who solved the issue.}]({Add PR link})

{You can provide more details or examples if you wish.}

```

### Commit Messages

If you want, you can use the emoji about the commit message you will throw, this can
help us better understand the change you have made and also it is fun.

- When you make any support commit; 💪
- When you make any tests commit; 🧪
- When you make any fix commit; 🐞
- When you make any optimization commit; 💊
- When you make any new feature commit; 🔥
- When you make any drop or delete existing feature; 👎

## License

{{project-name}} is GPL-3.0 licensed, as found in the LICENSE file.
