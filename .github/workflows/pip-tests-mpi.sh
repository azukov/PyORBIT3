. .po3/bin/activate
cd examples/MPI_Tests
mpirun -np 2 python mpi_initialization_test.py
exit $?
