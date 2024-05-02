import requests


class CatFacts:
    def __init__(self, req):
        self.req = req
        
    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        res = self.req.get("https://catfact.ninja/fact")
        return res.json()
    
    
cat_facts = CatFacts(requests)
print(cat_facts.provide())