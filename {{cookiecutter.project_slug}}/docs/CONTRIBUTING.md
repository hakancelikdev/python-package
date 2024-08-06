## Development and Contributing

## Issue

To make an improvement, add a new feature or anything else, please open a issue first.

**Good first issues are the issues that you can quickly solve, we recommend you take a
look.**
[Good first issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/labels/good%20first%20issue)

## Fork Repository

[fork the {{ cookiecutter.project_name }}.](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/fork)

## Clone Repository

```shell
$ git clone git@github.com:<USERNAME>/{{ cookiecutter.project_slug }}.git
$ cd {{ cookiecutter.project_slug }}
```

## Setup Branch

```shell
git checkout develop
git checkout -b {branch name}
```

If you have write access to the GitHub repository, please follow the following naming
scheme when pushing your branch(es):

- feat/foo-bar for new features
- fix/foo-bar for bug fixes
- tests/foo-bar when the change concerns only the test suite
- refactor/foo-bar when refactoring code without any behavior change
- style/foo-bar when addressing some style issue
- docs/foo-bar for updates to the README.md, this file, or similar documents
- perf/foo-bar for performance improvements
- chore/foo-bar for changes to the build process or auxiliary tools and libraries such
  as documentation generation

## How to Update My Local Repository

```shell
$ git remote add upstream git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
$ make sync-main
```

## Testing

Firstly make sure you have py3.10, py3.11 and py3.12 python versions installed on
your system.

After typing your codes, you should run the tests by typing the following command.

```shell
$ python3.12 -m pip install tox
$ tox
```

If tox pass.

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

```
git commit -m "#{issue-id} {Description your changes in shortly}"
```

- Keep it concise: The commit message should be brief, clear and to the point. Try to
  limit the message to 50 characters or less.
- Use the imperative mood: The commit message should be written in the imperative mood,
  as if you are giving an order. For example, use "Add feature" instead of "Added
  feature".
- Start with a capital letter: Always start the commit message with a capital letter.
- Do not end with a period: Do not end the commit message with a period.
- Use present tense: Use the present tense when describing the changes made in the
  commit.
- Use the body for more detailed explanation: If the commit message needs to be more
  detailed, use the body of the message to provide additional information.
- Reference issues: If the commit is related to a particular issue or task, reference it
  in the commit message. For example, "Fixes #1234".
- Be consistent: Be consistent with the format and style of your commit messages.
- Proofread: Always proofread your commit message before submitting it. Check for
  spelling and grammar errors.
- Remember, clear and concise commit messages can greatly improve the readability and
  maintainability of your codebase.

### Open PR

Then open the pull request to develop branch.
