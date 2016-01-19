def dumps(value, varname=None, indent=None):
    NL = "\n" if indent else ""
    s = varname + '=' + NL if varname else ''
    indentcount = 0 if indent is None else indent

    if isinstance(value, dict):
        e = []
        for key in value:
            child = value[key]
            KNL = "\n" if indent and isinstance(child, (dict, list)) else ""
            selem = '\t' * indentcount
            selem += '["{key}"]={nl}'.format(key=key, nl=KNL)
            selem += dumps(value[key], indent=indent + 1 if indent else None)
            e.append(selem)
        s += '\t' * (indent-1) if NL else ""
        s += "{"
        if e:
            s += NL + ",{nl}".format(nl=NL).join(e)
        s += NL + '\t' * (indentcount-1) + "}"
    elif isinstance(value, list):
        e = []
        i = 1
        for v in value:
            selem = '\t' * indentcount + "[{i}]=".format(i=i)
            selem += dumps(v, indent=indent + 1 if indent else None)
            e.append(selem)
            i += 1
        s += '\t' * (indent-1) if NL else ""
        s += "{"
        if e:
            s += NL + ",{nl}".format(nl=NL).join(e)
        s += NL + '\t' * (indentcount-1) + "}"
    elif isinstance(value, str):
        s += '"{val}"'.format(val=value.replace('"', '\\"'))
    elif isinstance(value, bool):
        s += "true" if value else "false"
    else:
        s += str(value)

    return s
