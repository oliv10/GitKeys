[![CodeQL](https://github.com/oliv10/GitKeys/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/oliv10/GitKeys/actions/workflows/github-code-scanning/codeql)

# GitKeys
GitKeys is a collection of simple scripts written in multiple languages that can be run to get your GitHub public keys installed on any linux based machine.

Each script is designed to need no dependecies other than the base language it is written.

## Download One Liners
```
curl -O -sSL https://raw.githubusercontent.com/oliv10/GitKeys/main/keys.{lang}
```
OR
```
wget https://raw.githubusercontent.com/oliv10/GitKeys/main/keys.{lang}
```
and then run your script!

## Add your own Script!
This wiki page will go over how the script should function at its core.
[Wiki Page](https://github.com/oliv10/GitKeys/wiki/Keys-Script-Design)

## Scripts Testing Status

[![Bash Script](https://github.com/oliv10/GitKeys/actions/workflows/test_bash.yml/badge.svg)](https://github.com/oliv10/GitKeys/actions/workflows/test_bash.yml)
[![Python Script](https://github.com/oliv10/GitKeys/actions/workflows/test_python.yml/badge.svg)](https://github.com/oliv10/GitKeys/actions/workflows/test_python.yml)
