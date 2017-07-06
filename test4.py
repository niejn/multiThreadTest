import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
    ctx = mp.get_context('spawn')
    q1 = ctx.Queue()
    p1 = ctx.Process(target=foo, args=(q1,))
    p1.start()
    print(q1.get())
    p1.join()