from collections import namedtuple, OrderedDict


def _set_list_stuff(od, obj, keys):
    for stuff in keys:
        item = getattr(obj, stuff)
        if item:
            od[stuff] = [o.to_data() for o in item]
            try:
                od[stuff].sort(key=lambda x: x['name'])
            except:
                print(od[stuff])
                # raise


param_key_order = ('name', 'type', 'optional', 'description')


def _fix_parameters(parameters):
    if not parameters:  # list empty
        return None

    new_params = []
    for param in parameters:
        param = OrderedDict([(k, param[k])
                             for k in param_key_order
                             if k in param])
        # Remove optional key if `False`
        if 'optional' in param and not param['optional']:
            del param['optional']
        # Add description key
        # param['description'] = ''  # 'TOADD'
        new_params.append(param)

    return new_params


class SublimeApi(namedtuple("SublimeApi", "modules")):
    # __slots__ is required because otherwise __dict__ will be overridden,
    # meaning ._asdict stops working
    __slots__ = ()

    def to_data(self):
        return [m.to_data() for m in self.modules]


class Module(namedtuple("Module", "name functions classes")):
    __slots__ = ()

    def to_data(self):
        m_data = OrderedDict()
        m_data['name'] = self.name
        _set_list_stuff(m_data, self, ('functions', 'classes'))
        return m_data


class Class(namedtuple("Class", "name constructors properties methods description")):
    __slots__ = ()

    def to_data(self):
        c_data = OrderedDict()
        c_data['name'] = self.name
        c_data['description'] = self.description
        _set_list_stuff(c_data, self, ('constructors', 'properties', 'methods'))
        return c_data


class Function(namedtuple("Function", "name parameters return_type description")):
    __slots__ = ()

    def to_data(self):
        f_data = self._asdict()  # returns an OrderedDict
        parameters = self.parameters[:]
        f_data['parameters'] = _fix_parameters(parameters)
        f_data['original'] = f_data['description']
        del f_data['description']
        return f_data


class Method(namedtuple("Method", "name parameters return_type description")):
    __slots__ = ()

    def to_data(self):
        # Basically the same thing currently, since there are no classmethods
        return Function.to_data(self)


class Property(namedtuple("Property", "name value_type description")):
    __slots__ = ()

    def to_data(self):
        p_data = self._asdict()  # returns an OrderedDict
        p_data['original'] = p_data['description']
        del p_data['description']
        return p_data


class Constructor(namedtuple("Constructor", "parameters description")):
    __slots__ = ()

    def to_data(self):
        # Function.to_data does exactly the same currently
        return Function.to_data(self)
