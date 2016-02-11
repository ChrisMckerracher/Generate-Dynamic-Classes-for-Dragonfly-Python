from dragonfly import Grammar, CompoundRule


class genericFilter(CompoundRule):
    spec = ''
    def _process_recognition(self, node, extras):
        print self.spec
        #specify generic functionality here

class metafilters(type):
    def __new__(meta, classname,bases, classDict):
        return type.__new__(meta, classname, (genericFilter,),classDict)


class filter():
    phrases = ["genericclass1", "genericclass2", "genericclass3"]
    grammar = Grammar("generic")


for i in filter.phrases:
    filter.grammar.add_rule(metafilters.__new__(metafilters, i, (genericFilter,), {'spec': i})())

filter.grammar.load()
