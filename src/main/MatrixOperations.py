from pygraphblas import Matrix


def transitive_closure_sqr(matrix: Matrix) -> Matrix:
    result = matrix.dup()
    changed = True
    while changed:
        old_nvals = result.nvals
        result += result @ result
        new_nvals = result.nvals
        if old_nvals == new_nvals:
            changed = False
    return result


def transitive_closure_adj(matrix: Matrix) -> Matrix:
    adj = matrix.dup()
    result = matrix.dup()
    changed = True
    while changed:
        old_nvals = result.nvals
        result += adj @ result
        new_nvals = result.nvals
        if old_nvals == new_nvals:
            changed = False
    return result
