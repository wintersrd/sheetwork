[![CodeFactor](https://www.codefactor.io/repository/github/bastienboutonnet/sheetload/badge)](https://www.codefactor.io/repository/github/bastienboutonnet/sheetload)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![codecov](https://codecov.io/gh/bastienboutonnet/sheetload/branch/dev%2Fnicolas_jaar/graph/badge.svg)](https://codecov.io/gh/bastienboutonnet/sheetload)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bastienboutonnet_sheetload&metric=alert_status)](https://sonarcloud.io/dashboard?id=bastienboutonnet_sheetload)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Actions Status](https://github.com/bastienboutonnet/sheetload/workflows/Sheetload/badge.svg?branch=dev/nicolas_jaar)](https://github.com/bastienboutonnet/sheetload/actions)

Package Version: `v1.0.0a3`

# sheetload 💩🤦
*A name inspired by [GitLab Data Team](https://gitlab.com/gitlab-data/analytics/tree/master/extract/sheetload)*

A handy package to load Google Sheets to Snowflake

Loads Google sheets from Data Team shared drive and uploads them to Snowflake.
Performs some cleanups on column names and string (such as removing trailing spaces etc.)

**BIG DISCLAIMER** Sheetload is still very early. Do not use in production jobs unless you tested it extensively and know whether it does what you want it to do!

## Documentation
Head over to the [official documentation](https://bastienboutonnet.gitbook.io/sheetload/) to learn about:
- how to set up sheetload
- how to use sheetload
