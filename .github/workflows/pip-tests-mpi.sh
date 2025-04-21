. .po3/bin/activate
cd examples/MPI_Tests
mpirun -np 2 python mpi_initialization_test.py | tee test.txt

calculated_sha1=$(sha1sum test.txt | awk '{ print $1 }')
echo $calculated_sha1
cat test.txt

[ "$calculated_sha1" == "d94e03044bf06c7a42d07505b50fa58b4b30e49a" ] && exit 0 || exit 1

