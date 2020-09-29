from pyformlang.cfg import Variable, Production, CFG


class CNF(CFG):
    def __init__(self,
                 cfg: CFG,
                 is_reduced: bool = False):
        if not is_reduced:
            if any(p.body.__contains__(cfg.start_symbol) for p in cfg.productions):
                new_start_variable_name = 'S\''
                name_is_used = cfg.variables.__contains__(new_start_variable_name)
                while name_is_used:
                    new_start_variable_name += '\''
                    name_is_used = cfg.variables.__contains__(new_start_variable_name)
                new_start_variable = Variable(new_start_variable_name)
                cfg._productions.add(Production(new_start_variable, [cfg._start_symbol]))
                cfg._variables.add(new_start_variable)
                cfg._start_symbol = new_start_variable
        generate_epsilon = cfg.generate_epsilon()
        cfg = cfg.to_normal_form()
        if generate_epsilon:
            cfg._productions.add(Production(cfg.start_symbol, []))
        super().__init__(cfg.variables, cfg.terminals, cfg.start_symbol, cfg.productions)


def from_file(path: str, is_reduced: bool = False):
    file = open(path)
    productions = ''
    for production in file.read().split('\n'):
        head, product = (production, 'epsilon') if production.find(' ') == -1 else (production.split(' ', 1))
        productions += f'{head} -> {product}\n'
    file.close()
    cfg = CFG.from_text(productions)
    return CNF(cfg, is_reduced)
