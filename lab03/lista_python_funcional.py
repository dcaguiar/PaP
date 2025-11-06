# lista_python_funcional.py
# Soluções da "Lista Python Funcional" - implementação puramente recursiva.
# Cada questão é uma função: q1, q2, ..., q32.
# Todas as funções evitam laços e mutação: usam recursão e expressões.

from typing import List, Tuple, Any

# ---------- Helpers recursivos ----------

def _head(lst: List[Any]) -> Any:
    if not lst:
        raise ValueError("head de lista vazia")
    return lst[0]

def _tail(lst: List[Any]) -> List[Any]:
    def _tail_i(i: int) -> List[Any]:
        if i >= len(lst):
            return []
        return [lst[i]] + _tail_i(i+1)
    return _tail_i(1)

def _init(lst: List[Any]) -> List[Any]:
    def _init_i(i: int) -> List[Any]:
        if i >= len(lst)-1:
            return [] if i >= len(lst) else [lst[i]] if i == len(lst)-1 and False else []
        return [lst[i]] + _init_i(i+1)
    # simpler: build until index len-2
    def _build(i):
        if i >= len(lst)-1:
            return []
        return [lst[i]] + _build(i+1)
    return _build(0)

def _last(lst: List[Any]) -> Any:
    if not lst:
        raise ValueError("last de lista vazia")
    def _last_i(i: int):
        if i == len(lst)-1:
            return lst[i]
        return _last_i(i+1)
    return _last_i(0)

def q1(lst: List[Any]) -> Any:
    "Questão 1: head"
    return _head(lst)

def q2(lst: List[Any]) -> List[Any]:
    "Questão 2: tail"
    return _tail(lst)

def q3(lst: List[Any]) -> List[Any]:
    "Questão 3: init (toda a lista exceto o último)"
    return _init(lst)

def q4(lst: List[Any]) -> Any:
    "Questão 4: last"
    return _last(lst)

# ---------- Funções da lista ----------

def q5(n: int) -> int:
    "Questão 5: n-ésimo termo de Fibonacci (0-indexado: q5(0)=0, q5(1)=1)"
    if n < 0:
        raise ValueError("n negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return q5(n-1) + q5(n-2)

def q6(a: List[Any], b: List[Any]) -> List[Any]:
    "Questão 6: concatenação recursiva de listas (a + b)"
    if not a:
        return b
    return [a[0]] + q6(_tail(a) if len(a)>1 else [], b)

def q7(x: Any, lst: List[Any]) -> bool:
    "Questão 7: verifica se x pertence a lst (recursivo)"
    if not lst:
        return False
    if lst[0] == x:
        return True
    return q7(x, _tail(lst) if len(lst)>1 else [])

def q8(a: List[Any], b: List[Any]) -> List[Any]:
    "Questão 8: união recursiva sem repetições (preserva ordem de a, depois b)"
    def _union(acc: List[Any], rest: List[Any]) -> List[Any]:
        if not rest:
            return acc
        h = rest[0]
        tailr = _tail(rest) if len(rest)>1 else []
        if q7(h, acc):
            return _union(acc, tailr)
        else:
            return _union(acc + [h], tailr)
    return _union(a, b)

def q9(lst: List[int], n: int) -> int:
    "Questão 9: conta elementos > n"
    if not lst:
        return 0
    head = lst[0]
    tail = _tail(lst) if len(lst)>1 else []
    return (1 if head > n else 0) + q9(tail, n)

def q10(lst: List[int], n: int) -> List[int]:
    "Questão 10: retorna lista contendo apenas elementos > n"
    if not lst:
        return []
    head = lst[0]
    tail = _tail(lst) if len(lst)>1 else []
    if head > n:
        return [head] + q10(tail, n)
    else:
        return q10(tail, n)

def q11a(lst: List[Any]) -> List[Any]:
    "Questão 11a: inverter lista (recursivo)"
    if not lst:
        return []
    head = lst[0]
    tail = _tail(lst) if len(lst)>1 else []
    return q11a(tail) + [head]

def q12(s: str) -> str:
    "Questão 12: gera palíndromo (s + reverse(s))"
    def _reverse_str(i: int) -> str:
        if i < 0:
            return ''
        return s[i] + _reverse_str(i-1)
    return s + _reverse_str(len(s)-1)

def q13(lst: List[Any]) -> int:
    "Questão 13: tamanho (sem len)"
    if not lst:
        return 0
    tail = _tail(lst) if len(lst)>1 else []
    return 1 + q13(tail)

def q14(n: int) -> bool:
    "Questão 14: ehPrimo (recursivo)"
    if n < 2:
        return False
    def _check(d: int) -> bool:
        if d * d > n:
            return True
        if n % d == 0:
            return False
        return _check(d+1)
    return _check(2)

def q15(rem: List[Any], lst: List[Any]) -> List[Any]:
    "Questão 15: strip - remove todos elementos de rem da lista lst"
    if not lst:
        return []
    head = lst[0]
    tail = _tail(lst) if len(lst)>1 else []
    if q7(head, rem):
        return q15(rem, tail)
    else:
        return [head] + q15(rem, tail)

def _is_consonant(ch: str) -> bool:
    return ch.isalpha() and ch.lower() not in "aeiou"

def _extract_consonants_list(word: List[str]) -> List[str]:
    "Extrai consoantes de uma lista de caracteres (recursivo)"
    if not word:
        return []
    head = word[0]
    tail = _tail(word) if len(word)>1 else []
    return ([head] if _is_consonant(head) else []) + _extract_consonants_list(tail)

def _is_subsequence(sub: List[Any], seq: List[Any]) -> bool:
    "verifica se sub é subsequência (ordem) de seq"
    if not sub:
        return True
    if not seq:
        return False
    if sub[0] == seq[0]:
        return _is_subsequence(_tail(sub) if len(sub)>1 else [], _tail(seq) if len(seq)>1 else [])
    else:
        return _is_subsequence(sub, _tail(seq) if len(seq)>1 else [])

def q16(a: List[Any], b: List[Any]) -> bool:
    "Questão 16: todas as consoantes de b, com repetições, aparecem em a na mesma ordem?"
    # extrair consoantes de b (supondo b como lista de chars)
    cons_b = _extract_consonants_list(b)
    return _is_subsequence(cons_b, a)

def q17(dic: List[str], cons_seq: str) -> List[str]:
    "Questão 17: matches - retorna palavras do dicionário cuja sequência de consoantes == cons_seq"
    def _chars(word: str, i: int) -> List[str]:
        if i >= len(word):
            return []
        rest = _chars(word, i+1)
        return ([word[i]] if _is_consonant(word[i]) else []) + rest if False else ([] if not _is_consonant(word[i]) else [word[i]] + rest)
    # mais direta sem complicar: construir consonant string por recursão
    def _consonants_str(word: str, i: int) -> str:
        if i >= len(word):
            return ''
        ch = word[i]
        return (ch + _consonants_str(word, i+1)) if _is_consonant(ch) else _consonants_str(word, i+1)
    def _check_word(w: str) -> bool:
        return _consonants_str(w, 0) == cons_seq
    if not dic:
        return []
    head = dic[0]
    tail = dic[1:]
    if _check_word(head):
        return [head] + q17(tail, cons_seq)
    else:
        return q17(tail, cons_seq)

def q18(n: int) -> int:
    "Questão 18: menor primo maior que n"
    def _next(m):
        if q14(m):
            return m
        return _next(m+1)
    return _next(n+1)

def q19(n: int) -> List[int]:
    "Questão 19: lista de fatores primos (com repetições)"
    def _smallest_factor(m, d=2):
        if d*d > m:
            return m
        if m % d == 0:
            return d
        return _smallest_factor(m, d+1)
    if n <= 1:
        return []
    f = _smallest_factor(n)
    return [f] + q19(n//f)

def q20(n: int) -> List[Tuple[int,int]]:
    "Questão 20: primeFactors -> lista de pares (fator, frequência)"
    def _group(primes: List[int]) -> List[Tuple[int,int]]:
        if not primes:
            return []
        h = primes[0]
        # contar repetidos iniciais
        def _count_run(lst):
            if not lst:
                return (0, [])
            if lst[0] != h:
                return (0, lst)
            cnt, rem = _count_run(lst[1:])
            return (1+cnt, rem)
        cnt, rem = _count_run(primes)
        return [(h, cnt)] + _group(rem)
    return _group(q19(n))

def q21(token: Any, lst: List[Any]) -> List[List[Any]]:
    "Questão 21: splitToken - divide lst usando token como marcador (não incluir token nas sublistas)"
    def _split(acc: List[List[Any]], cur: List[Any], rest: List[Any]):
        if not rest:
            return acc + ([cur] if cur != [] else [])
        h = rest[0]
        tail = rest[1:]
        if h == token:
            return _split(acc + ([cur] if cur != [] else []), [], tail)
        else:
            return _split(acc, cur + [h], tail)
    return _split([], [], lst)

def q22(token: Any, lsts: List[List[Any]]) -> List[Any]:
    "Questão 22: joinToken - junta sublistas usando token entre elas"
    if not lsts:
        return []
    if len(lsts) == 1:
        return lsts[0]
    return lsts[0] + [token] + q22(token, lsts[1:])

def q23(lst: List[Any]) -> Tuple[List[Any], List[Any]]:
    "Questão 23: splitHalf - divide em duas metades (diferença até 1)"
    def _len(l):
        return q13(l)
    n = _len(lst)
    mid = n // 2
    def _take(l, k):
        if k <= 0 or not l:
            return []
        return [l[0]] + _take(l[1:], k-1)
    def _drop(l, k):
        if k <= 0 or not l:
            return l
        return _drop(l[1:], k-1)
    return (_take(lst, mid), _drop(lst, mid))

def q24(n: int) -> List[Tuple[int,int,int]]:
    "Questão 24: pyths - todas triplas pitagóricas com componentes em [1..n] (list comprehension)"
    return [(x,y,z) for x in range(1, n+1) for y in range(1, n+1) for z in range(1, n+1) if x*x + y*y == z*z]

def _divisors(m: int) -> List[int]:
    if m <= 1:
        return []
    def _check(d):
        if d > m//2:
            return []
        return ([d] if m % d == 0 else []) + _check(d+1)
    return _check(1)

def q25(limit: int) -> List[int]:
    "Questão 25: perfects até limit"
    def _sum_proper(n):
        return sum(_divisors(n))
    return [i for i in range(1, limit+1) if _sum_proper(i) == i]

def q26(v: List[int], w: List[int]) -> int:
    "Questão 26: produto escalar (dot product) - recursivo"
    if not v or not w:
        return 0
    return v[0]*w[0] + q26(v[1:], w[1:])

def q27(pos: Tuple[int,int], others: List[Tuple[int,int]]) -> bool:
    "Questão 27: ataca - verifica se pos ataca alguma posição em others"
    if not others:
        return False
    r,c = pos
    r1,c1 = others[0]
    if r == r1 or c == c1 or abs(r-r1) == abs(c-c1):
        return True
    return q27(pos, others[1:])

def q28(s: str) -> bool:
    "Questão 28: isPalindrome (recursivo, ignora não alfanuméricos e case-insensitive)"
    def _clean(st):
        if st == "":
            return ""
        ch = st[0]
        rest = _clean(st[1:])
        return (ch.lower() + rest) if ch.isalnum() else rest
    cs = _clean(s)
    def _isp(st):
        if len(st) <= 1:
            return True
        if st[0] != st[-1]:
            return False
        return _isp(st[1:-1])
    return _isp(cs)

def q29(lst: List[Any]) -> List[Any]:
    "Questão 29: compress - elimina duplicadas consecutivas"
    if not lst:
        return []
    if len(lst) == 1:
        return [lst[0]]
    first = lst[0]
    second = lst[1]
    rest = lst[1:]
    if first == second:
        return q29(rest)
    else:
        return [first] + q29(rest)

def q30(lst: List[Any]) -> List[List[Any]]:
    "Questão 30: pack - empacota duplicadas consecutivas em sublistas"
    if not lst:
        return []
    def _pack_run(l):
        if not l:
            return ([], [])
        h = l[0]
        # contar sequência inicial
        def _take_run(xs):
            if not xs or xs[0] != h:
                return []
            return [xs[0]] + _take_run(xs[1:])
        run = _take_run(l)
        rest = l[len(run):]
        return (run, rest)
    run, rest = _pack_run(lst)
    return [run] + q30(rest)

def q31(s: List[Any]) -> List[Tuple[int,Any]]:
    "Questão 31: encode - run-length encoding de sequência"
    packed = q30(s)
    def _encode(plist):
        if not plist:
            return []
        h = plist[0]
        return [(q13(h), h[0])] + _encode(plist[1:])
    return _encode(packed)

def q32(encoded: List[Tuple[int,Any]]) -> List[Any]:
    "Questão 32: decode - expande lista codificada (count, element)"
    if not encoded:
        return []
    cnt, el = encoded[0]
    def _repeat(k):
        if k <= 0:
            return []
        return [el] + _repeat(k-1)
    return _repeat(cnt) + q32(encoded[1:])

# Fim do arquivo de funções.
