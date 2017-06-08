#!/bin/bash

pytest --cov=ppboilerplate --cov-report=html && firefox htmlcov/index.html
