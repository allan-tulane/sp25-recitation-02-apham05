from main import *
	
def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(15, 2, 3) == 29
	assert simple_work_calc(25, 3, 5) == 49
	assert simple_work_calc(40, 2, 4) == 68
	
def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(50, 2, 2, lambda n: n) == 276
	assert work_calc(40, 3, 2, lambda n: n * n) == 4942
	assert work_calc(25, 1, 2, lambda n: 2 * n) == 94
	
	
def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
		
	# create work_fn1
	work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n ** 0.5)
	# create work_fn2
	work_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n ** 3)
	res = compare_work(work_fn1, work_fn2)
	print_results(res)
	
	
def test_compare_span():
	#pass
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)
	res = compare_work(span_fn1, span_fn2)
	print_results(res)
	