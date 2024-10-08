//The base class for Poisson Solvers. It defines the interface for solves

#ifndef SC_POISSON_SOLVER_BASE_2D_H
#define SC_POISSON_SOLVER_BASE_2D_H

//MPI Function Wrappers
#include "orbit_mpi.hh"
#include "wrap_mpi_comm.hh"

#include <cstdlib>
#include <cmath>
#include <string>

//pyORBIT utils
#include "CppPyWrapper.hh"

#include "Grid2D.hh"

using namespace std;

/**
  The PoissonSolver2D class calculates electrostatic
  potential of a 2D charge distribution.
*/

class PoissonSolver2D: public OrbitUtils::CppPyWrapper
{
public:

	/** Constructor */
	PoissonSolver2D(int xSize, int ySize);

	/** Constructor */
	PoissonSolver2D(int xSize, int ySize,
		              double xMin, double xMax,
									double yMin, double yMax);

  /** Destructor */
  virtual ~PoissonSolver2D();

  /** Returns the grid size in x-direction */
  int getSizeX();

  /** Returns the grid size in y-direction */
  int getSizeY();

  /** Returns the maximal value of the grid in x-axis */
  double getMaxX();

  /** Returns the minimal value of the grid in x-axis */
  double getMinX();

  /** Returns the maximal value of the grid in y-axis */
  double getMaxY();

  /** Returns the minimal value of the grid in y-axis */
  double getMinY();

  /** Returns the grid step along x-axis */
  double getStepX();

	/** Returns the grid step along y-axis */
  double getStepY();

  /** Sets x-grid. This method is virtual, because the setting of limits may involve
	  * some subclass specific actions.
		*/
  virtual void setGridX(double xMin, double xMax) = 0;

  /** Sets y-grid. This method is virtual, because the setting of limits may involve
	  * some subclass specific actions.
		*/
  virtual void setGridY(double yMin, double yMax) = 0;

  /** Sets x-grid and y-grid simultaneously. This method is virtual, because the setting of limits may involve
	  * some subclass specific actions.
		*/
	virtual void setGridXY(double xMin, double xMax, double yMin, double yMax) = 0;

  /** Solves the Poisson problem for an external charge distribution and
	    puts results into an external potential grid
	*/
  virtual void findPotential(Grid2D* rhoGrid,Grid2D*  phiGrid) = 0;

protected:

	//checks that sizes of Grid2D instances are the same as solver
	void checkSizes(Grid2D* rhoGrid,Grid2D*  phiGrid);

	//should be implemented in subclasses. It should be called in both types of constructors.
	virtual void init(int xSize, int ySize, double xMin, double xMax, double yMin, double yMax) = 0;

protected:

  //Grid size
  int xSize_;
  int ySize_;

   //Grid array and parameters
  double xMin_, xMax_, yMin_, yMax_;
  double  dx_  ,  dy_;

};

//end of SC_POISSON_SOLVER_BASE_2D_H ifdef
#endif
