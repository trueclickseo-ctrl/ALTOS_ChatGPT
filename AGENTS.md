# AGENTS.md

# ATOS Engineering Guide

**Project:** Algorithmic Trading Operating System (ATOS)

This document defines the engineering standards for the ATOS project.

---

# Vision

ATOS is a modular, production-grade Algorithmic Trading Operating System designed for:

- Historical Backtesting
- Paper Trading
- Live Trading
- Portfolio Management
- Risk Management
- Multi-Strategy Execution
- AI-assisted Decision Support
- Saxo Bank Integration

The objective is to build a maintainable and extensible trading platform rather than a collection of scripts.

---

# Engineering Principles

## 1. Single Responsibility

Each module must have one responsibility.

Example:

Market module

Responsible only for obtaining market data.

It must NOT:

- calculate indicators
- place trades
- calculate risk

---

## 2. Loose Coupling

Modules communicate through interfaces.

Never import unrelated packages directly.

---

## 3. High Cohesion

Everything inside a package should serve one purpose.

---

## 4. Configuration Driven

Never hardcode:

- symbols
- broker credentials
- timeframes
- commissions
- risk limits

Everything belongs in configuration.

---

## 5. Testability

Business logic must be testable without:

- Saxo
- Internet
- Database

---

## 6. Broker Agnostic

The core system must not depend on Saxo.

Future brokers should be plug-ins.

---

## 7. Strategy Agnostic

Strategies are plug-ins.

The engine must never know strategy details.

---

# Project Architecture

```
Market
    ↓
Indicators
    ↓
Strategies
    ↓
Decision
    ↓
Risk
    ↓
Portfolio
    ↓
Broker
    ↓
Execution
    ↓
Reports
```

---

# Directory Responsibilities

## atos/market

Market data only.

Responsible for:

- CSV
- API
- Streaming

---

## atos/indicators

Technical indicators.

Examples:

- EMA
- SMA
- RSI
- ATR
- VWAP
- ADX
- MACD

---

## atos/strategies

Trading strategies.

Every strategy implements the same interface.

---

## atos/risk

Risk calculations.

Examples:

- Position sizing
- ATR stops
- Daily loss
- Portfolio heat

---

## atos/backtest

Historical execution engine.

---

## atos/broker

Broker implementations.

Initially:

- Paper Broker
- Saxo Broker

---

## atos/reports

Performance reporting.

---

## atos/ui

Future dashboard.

---

# Coding Standards

Python 3.12+

Required:

- Type hints
- Google Docstrings
- Logging
- Small functions
- Readable code

Avoid:

- print()
- magic numbers
- duplicated code

---

# Git Workflow

Main branches:

main

develop

Feature branches:

feature/<feature-name>

Bug fixes:

hotfix/<issue>

---

# Commit Convention

feat:

fix:

docs:

refactor:

test:

perf:

build:

ci:

chore:

Example:

feat: add ATR position sizing

---

# Documentation Policy

Every feature must update:

README

CHANGELOG

Relevant docs

---

# Testing Policy

Every important module should eventually have unit tests.

Business logic first.

Broker integration later.

---

# Release Policy

Semantic Versioning

v0.x

Development

v1.0.0

First production release

---

# Definition of Done

A task is complete only when:

✓ Code works

✓ Documentation updated

✓ Tests added where appropriate

✓ No duplicated logic

✓ Ready for Git commit

---

This document is the engineering contract for the ATOS project.