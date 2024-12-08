from typing import AnyStr
Rule = tuple[set[AnyStr], AnyStr]
RuleList = list[Rule]
Fact = AnyStr
FactSet = set[AnyStr]

class InferenceEngine:
    def __init__(self, rules: RuleList, facts: FactSet):
        self._rules = rules
        self._facts = facts

    def infer(self, fact: Fact) -> bool:
        applied_rules = [False]  * len(self._rules)
        changed = True
        while changed and not fact in self._facts:
            changed = False
            for i, rule in enumerate(self._rules):
                if applied_rules[i]:
                    continue
                body, head = rule
                if self._facts.issuperset(body):
                    self._facts.add(head)
                    changed = True
                    applied_rules[i] = True
        return fact in self._facts


    def __str__(self) -> str:
        rules_str = "\n".join([f"{body} -> {head}" for body, head in self._rules])
        facts_str = ", ".join(self._facts)
        return f"Rules:\n{rules_str}\n\nFacts:\n{facts_str}"

