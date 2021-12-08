import time,os
import multiprocessing


def run():
    print("%s Process run " % os.getpid())
    time.sleep(1)
    print('%s process end' % os.getpid())


if __name__ == '__main__':
    print('mainProcess start')
    start_time = time.time()
    # 创建三个子进程
    pool = multiprocessing.Pool(3)
    print('Child start')
    for i in range(10):
        pool.apply_async(run)
    pool.close()
    pool.join()
    print('mainProcess done time:%s s' % (time.time() - start_time))
