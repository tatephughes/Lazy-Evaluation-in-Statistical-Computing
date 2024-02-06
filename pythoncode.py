bool_func_1() or bool_func_2()

def bool_func_1():
   print("bool_func_1 was evaluated")
   return True

def bool_func_2():
   print("bool_func_2 was evaluated")
   return False

result = bool_func_1() | bool_func_2()
print(result)

result = bool_func_1() or bool_func_2()
print(result)

def my_or_function(bool1,bool2): return bool1 or bool2

print(my_or_function(bool_func_1(),bool_func_2()))

for i in range(1000000)
  do_something_interesting
  if condition: break

import scala.collection.mutable.ListBuffer

val n = 10
val fibs1 = new ListBuffer[Long]
fibs1 += (0,1)
for (i <- (1 to n)){
  fibs1 += fibs1(fibs1.size-1) + fibs1(fibs1.size-2)
}

fibs1
//res0: ListBuffer(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

def fibFrom(a: Long, b: Long): LazyList[Long] = a #:: nextfib(b, a + b)

val fibs2 = fibFrom(0,1)
//val fibs2: LazyList[Long] = LazyList(<not computed>)

fibs2(30)
// val res0: Long = 832040

fibs.take(30).toList
//val res12: List[Long] = List(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229)

lazy val fib: LazyList[Long] = 0L #:: 1L #:: fib.zip(fib.tail).map { case (a, b) => a + b }

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

import breeze.linalg._
import breeze.stats.distributions._
import breeze.stats.distributions.Rand.FixedSeed.randBasis
import scala.math
import java.util.concurrent.ThreadLocalRandom
def rng = ThreadLocalRandom.current()

def one_MRTH_step(x: DenseVector[Double],
  r: DenseMatrix[Double],
  q: DenseMatrix[Double]
): DenseVector[Double] = {

  val proposed_move = x.map((xi:Double) => Gaussian(xi, 0.01/d.toDouble).sample())
  val alpha = 0.5 * ((x.t * (r \ (q.t * x))) - (proposed_move.t * (r \ (q.t * proposed_move))))
  val log_acceptance_prob = math.min(0.0, alpha)
  val u = rng.nextDouble()
  if (math.log(u) < log_acceptance_prob) then proposed_move else x

}

LazyList.iterate(x0)((x:DenseVector[Double]) => one_MRTH_step(x,q,r)

val n = 100000

val xsum = mrth_sample.take(n).foldLeft(DenseVector.zeros[Double](d))(_+_)
val xxtvals = mrth_sample.map((x: DenseVector[Double]) => x * x.t)
val xxtsum = xxtvals.take(n).foldLeft(DenseMatrix.zeros[Double](d,d))(_+_)

val sample_var = (xxtsum :*= 1/n.toDouble) - ((xsum * xsum.t) :*= 1/(n*n).toDouble)
// 0.5798798360620974    -0.25268806862366644  -0.23151583712649304  
// -0.25268806862366644  2.3148740685967075    1.5463449917637646    
// -0.23151583712649304  1.5463449917637646    1.5615727189017325
