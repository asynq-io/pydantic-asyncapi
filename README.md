![Tests](https://github.com/asynq-io/pydantic-asyncapi/workflows/Tests/badge.svg)
![Build](https://github.com/asynq-io/pydantic-asyncapi/workflows/Publish/badge.svg)
![License](https://img.shields.io/github/license/asynq-io/pydantic-asyncapi)
![Python](https://img.shields.io/pypi/pyversions/pydantic-asyncapi)
![Format](https://img.shields.io/pypi/format/pydantic-asyncapi)
![PyPi](https://img.shields.io/pypi/v/pydantic-asyncapi)
![Mypy](https://img.shields.io/badge/mypy-checked-blue)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# Pydantic AsyncAPI

Pydantic models for AsyncAPI

## Installation

```shell
pip install pydantic-asyncapi
```

## About

This package provides Pydantic models for [AsyncAPI](https://www.asyncapi.com/).
Currently versions `2.6.0` and `3.0.0` are supported.

The package can be used to:

1. Validate AsyncAPI documents
2. Generate AsyncAPI documents from code
3. Create Python frameworks/applications based on AsyncAPI specification

## Usage

```python
from pydantic_asyncapi import AsyncAPI

# v2 or v3 based on on 'asyncapi' version field
model = AsyncAPI.model_validate(...)

```
