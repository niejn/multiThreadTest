import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
    mp.set_start_method('spawn')
    q1 = mp.Queue()
    p1 = mp.Process(target=foo, args=(q1,))
    p1.start()
    print(q1.get())
    p1.join()