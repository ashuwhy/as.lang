from .as_lexer import asLexer
from .as_parser import asParser

VERSION = "0.1"

names = {}

def get_obj_type(_obj):
    return str(type(_obj)).split("'")[1]

def evaluate(tree):
    global names
    undefined = "as says: {0} hasn't been defined!"
    type_error = "as says: You can't use '{op}' with types '{obj1}' and '{obj2}'!"
    single_te = "as says: You can't use '{op}' with type '{obj}'!"

    try:
        rule = tree[0]
    except TypeError:
        return print("as says: Error!!")

    if rule == 'main':
        evaluate(tree[1])
    elif rule == 'statements':
        results = []
        for i in tree[1]:
            results.append(evaluate(i))
        return results
    elif rule == 'statement-expr':
        value = evaluate(tree[1])
        return value
    elif rule == 'assign':
        value = evaluate(tree[2])
        name = tree[1]
        names[name] = value
        return value

    elif rule == 'times':
        multiplier = evaluate(tree[1])
        multiplicand = evaluate(tree[2])
        try:
            return multiplier * multiplicand
        except TypeError:
            return print(type_error.format(op="*", obj1=get_obj_type(multiplier), obj2=get_obj_type(multiplicand)))
    elif rule == 'plus':
        addend1 = evaluate(tree[1])
        addend2 = evaluate(tree[2])
        try:
            return addend1 + addend2
        except TypeError:
            return print(type_error.format(op="+", obj1=get_obj_type(addend1), obj2=get_obj_type(addend2)))
    elif rule == 'minus':
        minuend = evaluate(tree[1])
        subtrahend = evaluate(tree[2])
        try:
            return minuend - subtrahend
        except TypeError:
            return print(type_error.format(op="-", obj1=get_obj_type(minuend), obj2=get_obj_type(subtrahend)))
    elif rule == 'divide':
        dividend = evaluate(tree[1])
        divisor = evaluate(tree[2])
        try:
            return dividend / divisor
        except TypeError:
            return print(type_error.format(op="/", obj1=get_obj_type(dividend), obj2=get_obj_type(divisor)))
    elif rule == 'mod':
        a = evaluate(tree[1])
        n = evaluate(tree[2])
        try:
            return a % n
        except TypeError:
            return print(type_error.format(op="%", obj1=get_obj_type(a), obj2=get_obj_type(n)))
    elif rule == 'pow':
        target_num = evaluate(tree[1])
        exponent = evaluate(tree[2])
        try:
            return target_num ** exponent
        except TypeError:
            return print(type_error.format(op="^", obj1=get_obj_type(target_num), obj2=get_obj_type(exponent)))
    
    elif rule == 'equals':
        return int(evaluate(tree[1]) == evaluate(tree[2]))
    elif rule == 'ne':
        return int(evaluate(tree[1]) != evaluate(tree[2]))
    elif rule == 'gt':
        return int(evaluate(tree[1]) > evaluate(tree[2]))
    elif rule == 'gte':
        return int(evaluate(tree[1]) >= evaluate(tree[2]))
    elif rule == 'lt':
        return int(evaluate(tree[1]) < evaluate(tree[2]))
    elif rule == 'lte':
        return int(evaluate(tree[1]) <= evaluate(tree[2]))
    elif rule == 'and':
        return int(evaluate(tree[1]) and evaluate(tree[2]))
    elif rule == 'or':
        return int(evaluate(tree[1]) or evaluate(tree[2]))


    elif rule == 'uminus':
        return -evaluate(tree[1])
    elif rule == 'inc':
        name = tree[1]

        try:        
            oldval = names[tree[1]]
        except KeyError:
            return print(f"as says: {name} hasn't been defined!")        
        newval = oldval + 1
        
        names[name] = newval
        return newval
    elif rule == 'dec':
        name = tree[1]
        try:        
            oldval = names[tree[1]]
        except KeyError:
            return print(undefined.format(varname)) 

        newval = oldval - 1
        
        names[name] = newval
        return newval
    elif rule == 'number':
        try:
            return int(tree[1])
        except ValueError:
            return float(tree[1])
    elif rule == 'string':
        return str(tree[1])
    elif rule == 'list':
        #print(tree)
        results = []
        for i in tree[1][1]:
            results.append(evaluate(i))
        return results
    elif rule == 'name':
        varname = tree[1]
        try:
            return names[varname]
        except KeyError:
            print(undefined.format(varname))
    elif rule == 'index':
        op = evaluate(tree[1])
        index = evaluate(tree[2])
        try:
            return op[index]
        except IndexError as e:
            print(f'as says: {e}')
        except TypeError as e:
            print(f'Says says: Only lists and strings can be indexed')
    elif rule == 'paren':
        return evaluate(tree[1])
    elif rule == 'pass':
        pass
    elif rule == 'break':
        return Break()
    elif rule == 'print':
        value = evaluate(tree[1])
        print(value)
        return value
    elif rule == 'input':
        value = evaluate(tree[1])
        res = input(value)
        try:
            res = float(res)
        except ValueError:
            pass
        return res
    elif rule == 'if-elif-else':
        expr1 = evaluate(tree[1])
        expr2 = None if tree[3] is None else evaluate(tree[3])
        if expr1:
            return evaluate(tree[2])
        elif expr2:
            return evaluate(tree[4])
        else:
            if tree[5]:
                return evaluate(tree[5])
            else:
                pass
    elif rule == 'while':
        while evaluate(tree[1]):
            results = evaluate(tree[2])
            
            if any([isinstance(res,Break) for res in results]):
                break
    elif rule == 'array1d':
        size = evaluate(tree[1])
        return [0] * size

    elif rule == 'array2d':
        rows = evaluate(tree[1])
        cols = evaluate(tree[2])
        return [[0] * cols for _ in range(rows)]

    elif rule == 'array_access1d':
        array_name = tree[1]
        index = evaluate(tree[2])
        try:
            return names[array_name][index]
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index {index} is out of range!")

    elif rule == 'array_access2d':
        array_name = tree[1]
        row = evaluate(tree[2])
        col = evaluate(tree[3])
        try:
            return names[array_name][row][col]
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{row}][{col}] is out of range!")
    elif rule == 'array_assign1d':
        array_name = tree[1]
        index = evaluate(tree[2])
        value = evaluate(tree[3])
        try:
            names[array_name][index] = value
            return value
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index {index} is out of range!")

    elif rule == 'array_assign2d':
        array_name = tree[1]
        row = evaluate(tree[2])
        col = evaluate(tree[3])
        value = evaluate(tree[4])
        try:
            names[array_name][row][col] = value
            return value
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{row}][{col}] is out of range!")
    elif rule == 'array3d':
        dim1 = evaluate(tree[1])
        dim2 = evaluate(tree[2])
        dim3 = evaluate(tree[3])
        return [[[0] * dim3 for _ in range(dim2)] for _ in range(dim1)]

    elif rule == 'array4d':
        dim1 = evaluate(tree[1])
        dim2 = evaluate(tree[2])
        dim3 = evaluate(tree[3])
        dim4 = evaluate(tree[4])
        return [[[[0] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

    elif rule == 'array_access3d':
        array_name = tree[1]
        idx1 = evaluate(tree[2])
        idx2 = evaluate(tree[3])
        idx3 = evaluate(tree[4])
        try:
            return names[array_name][idx1][idx2][idx3]
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{idx1}][{idx2}][{idx3}] is out of range!")

    elif rule == 'array_access4d':
        array_name = tree[1]
        idx1 = evaluate(tree[2])
        idx2 = evaluate(tree[3])
        idx3 = evaluate(tree[4])
        idx4 = evaluate(tree[5])
        try:
            return names[array_name][idx1][idx2][idx3][idx4]
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{idx1}][{idx2}][{idx3}][{idx4}] is out of range!")

    elif rule == 'array_assign3d':
        array_name = tree[1]
        idx1 = evaluate(tree[2])
        idx2 = evaluate(tree[3])
        idx3 = evaluate(tree[4])
        value = evaluate(tree[5])
        try:
            names[array_name][idx1][idx2][idx3] = value
            return value
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{idx1}][{idx2}][{idx3}] is out of range!")

    elif rule == 'array_assign4d':
        array_name = tree[1]
        idx1 = evaluate(tree[2])
        idx2 = evaluate(tree[3])
        idx3 = evaluate(tree[4])
        idx4 = evaluate(tree[5])
        value = evaluate(tree[6])
        try:
            names[array_name][idx1][idx2][idx3][idx4] = value
            return value
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except IndexError:
            print(f"as says: Index [{idx1}][{idx2}][{idx3}][{idx4}] is out of range!")
    else:
        #print(rule, tree)
        pass

    if rule in ('array1d', 'array2d', 'array3d', 'array4d'):
        dims = []
        for i in range(1, len(tree)):
            dims.append(evaluate(tree[i]))
        try:
            dims = validate_array_dims(dims)
            return create_nd_array(dims)
        except ValueError as e:
            print(f"as says: {e}")
            return None

    elif rule.startswith('array_access'):
        array_name = tree[1]
        indices = [evaluate(tree[i]) for i in range(2, len(tree))]
        try:
            if array_name not in names:
                raise KeyError(array_name)
            array = names[array_name]
            indices = validate_array_indices(array, indices)
            return get_array_element(array, indices)
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except (ValueError, IndexError) as e:
            print(f"as says: {e}")

    elif rule.startswith('array_assign'):
        array_name = tree[1]
        indices = [evaluate(tree[i]) for i in range(2, len(tree)-1)]
        value = evaluate(tree[-1])
        try:
            if array_name not in names:
                raise KeyError(array_name)
            array = names[array_name]
            indices = validate_array_indices(array, indices)
            set_array_element(array, indices, value)
            return value
        except KeyError:
            print(f"as says: Array '{array_name}' hasn't been defined!")
        except (ValueError, IndexError) as e:
            print(f"as says: {e}")

class Break:
    pass

def execute(fp):
    with open(fp, "r") as f:
        text = f.read()

    lexer = asLexer()
    parser = asParser()
    tree = parser.parse(lexer.tokenize(text))
    evaluate(tree)

def shell():
    lexer = asLexer()
    parser = asParser()
    print(f"aslang {VERSION}")
    while True:
        try:
            text = input('as > ')
        except EOFError:
            break
        tree = parser.parse(lexer.tokenize(text))
        evaluate(tree)

def validate_array_dims(dims):
    """Validate array dimensions"""
    for dim in dims:
        if not isinstance(dim, (int, float)) or dim < 0:
            raise ValueError(f"Array dimension must be a positive number, got {dim}")
        if int(dim) != dim:
            raise ValueError(f"Array dimension must be an integer, got {dim}")
    return [int(dim) for dim in dims]

def create_nd_array(dims):
    """Create an n-dimensional array initialized with zeros"""
    if not dims:
        return 0
    if len(dims) == 1:
        return [0] * dims[0]
    return [create_nd_array(dims[1:]) for _ in range(dims[0])]

def validate_array_indices(array, indices):
    """Validate array indices"""
    current = array
    for i, idx in enumerate(indices):
        if not isinstance(current, list):
            raise ValueError(f"Too many indices for array dimension {i}")
        if not isinstance(idx, (int, float)) or int(idx) != idx:
            raise ValueError(f"Array index must be an integer, got {idx}")
        idx = int(idx)
        if idx < 0 or idx >= len(current):
            raise IndexError(f"Index {idx} is out of range for dimension {i}")
        current = current[idx]
    return [int(idx) for idx in indices]

def get_array_element(array, indices):
    """Get element from n-dimensional array"""
    current = array
    for idx in indices:
        current = current[idx]
    return current

def set_array_element(array, indices, value):
    """Set element in n-dimensional array"""
    current = array
    for idx in indices[:-1]:
        current = current[idx]
    current[indices[-1]] = value

