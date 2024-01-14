def cross(A, B):
    """Cross product of elements in A and elements in B."""
    return [a + b for a in A for b in B]

digits = '123456789ABCDEFG'
rows = 'ABCDEFGHIJKLMNOP'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABCD', 'EFGH', 'IJKL', 'MNOP') for cs in ('1234', '5678', '9ABC', 'DEFG')])

units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values


def grid_values(grid):
    """Convert grid into a dict of {square: char} with '0' or '.' for empties."""
    chars = [c for c in grid if c in digits or c in '0.']
    return dict(zip(squares, chars))


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values  # Already eliminated
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False  # Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values


def display(values):
    """Display these values as a 2-D grid."""
    width = 1 + max(len(values[s]) for s in squares)
    line = '+'.join(['-' * (width * 4)] * 4)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '37' else '') for c in cols))
        if r in 'DHL': print(line)
    print()


def solve(grid):
    return search(parse_grid(grid))


def search(values):
    """Using depth-first search and propagation, try all possible values."""
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values  # Solved!
    # Choose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def some(seq):
    """Return some element of seq that is true."""
    for e in seq:
        if e:
            return e
    return False


# Example Sudoku grid
#grid = '003000090400000C020D00000001..0D0006.00F9.00C0..9A00..D.....0900000A0..7.0..1009F8..60'
grid='123456789ABCDEFG56789ABCDEFG12349ABCDEFG12345678CDEFG123456789AB23456789ABCEFG116789ABCDEF2345ABCDEFG123456789DEFG123456789ABC3456789ABCEFG123789ABCDEFG123456BCDEFG123456789AEFG123456789ABC456789ABCEFG123489ABCDEFG1234567G123456789ABCDEF123456789ABCDEFG'

result = solve(grid)
if result:
    for row in rows:
        print(' '.join(result[row + col] for col in cols))
else:
    print("No solution exists.")
