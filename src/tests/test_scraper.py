import pytest
from src.scraper import parse_react_docs, parse_aws_docs


def test_parse_react_docs():
    html = "<html><nav><a href='/test'>Test Section</a></nav></html>"
    result = parse_react_docs(html)
    assert result["source"] == "react"
    assert len(result["sections"]) == 1
    assert result["sections"][0]["title"] == "Test Section"


def test_parse_aws_docs():
    html = "<html><li class='nav-link'><a href='/test'>Test AWS Section</a></li></html>"
    result = parse_aws_docs(html)
    assert result["source"] == "aws_lambda"
    assert len(result["sections"]) == 1
    assert result["sections"][0]["title"] == "Test AWS Section"
