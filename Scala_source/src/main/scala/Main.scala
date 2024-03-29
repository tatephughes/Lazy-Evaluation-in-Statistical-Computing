import breeze.plot._
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

    val proposed_move = x.map((xi:Double) => Gaussian(xi, 1/x.size.toDouble).sample())
    val alpha = 0.5 * ((x.t * (r \ (q.t * x))) - (proposed_move.t * (r \ (q.t * proposed_move))))
    val log_acceptance_prob = math.min(0.0, alpha)
    val u = rng.nextDouble()
    if (math.log(u) < log_acceptance_prob) then proposed_move else x

  }

def plotter(sample: LazyList[DenseVector[Double]], 
            n: Int, 
            j: Int,
            file_path: String): Unit = {

    val xvals = Array.tabulate(n)(i => i.toDouble)
    val yvals = sample.map((x: DenseVector[Double]) => x(0)).take(n).toArray

    val f = Figure()
    val p = f.subplot(0)


    p += plot(xvals,yvals)
    p.xlabel = "Index"
    p.ylabel = "x_j"

    p.title = "Trace Plot of x_j"

    f.saveas(file_path)

  }

@main def run(): Unit =


  // Fibonacci Sequence
  //val fibs: LazyList[Int] = 0 #:: fibs.scanLeft(1)(_ + _)

  // Metropolis-Hastings
  val d = 3

  val data = Gaussian(0,1).sample(d*d).toArray.grouped(d).toArray
  val M = DenseMatrix(data: _*)
  val sigma = M.t * M

  val x0 = DenseVector.zeros[Double](d)

  val qr.QR(q,r) = qr(sigma)

  val mrth_sample = LazyList.iterate(x0)((x:DenseVector[Double]) => one_MRTH_step(x,q,r))

  print(mrth_sample(30))

  // Computing the 100000th sample 
  val n = 100000

  val xsum = mrth_sample.take(n).foldLeft(DenseVector.zeros[Double](d))(_+_)
  val xxtvals = mrth_sample.map((x: DenseVector[Double]) => x * x.t)
  val xxtsum = xxtvals.take(n).foldLeft(DenseMatrix.zeros[Double](d,d))(_+_)
  
  val sample_var = (xxtsum :*= 1/n.toDouble) - ((xsum * xsum.t) :*= 1/(n*n).toDouble)

  print(sample_var)

  // Plotting the first 10000 points
  plotter(mrth_sample, 100000, 1, "MHplot.png")
