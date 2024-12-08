import re
from .knowledge_base import RuleList, FactSet
from typing import AnyStr

FACT_PATTERN =r"-\|\s*([a-zA-Z_]+)\s*;"
RULE_PATTERN =r"([a-zA-Z_]+(?:,\s*[a-zA-Z_]+)*)\s*->\s*([a-zA-Z_]+);"

def parse_rules(input_str: AnyStr) -> RuleList:
    retval = []
    p = re.compile(RULE_PATTERN)
    matches = re.finditer(p, input_str)
    for m in matches:
        body, head = m.group(1), m.group(2)
        body_clauses = {x.strip() for x in body.split(',')}
        retval.append((body_clauses, head))
    return retval
    
def parse_facts(input_str: AnyStr) -> FactSet:
    retval = set()
    p = re.compile(FACT_PATTERN)
    matches = re.finditer(p, input_str)
    for m in matches:
        fact = m.group(1).strip()
        retval.add(fact)
    return retval