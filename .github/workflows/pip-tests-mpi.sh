. .po3/bin/activate
cd examples/MPI_Tests
mpirun -np 2 python mpi_initialization_test.py > test.txt

calculated_sha1=$(sha1sum test.txt | awk '{ print $1 }')
echo $calculated_sha1

[ "$calculated_sha1" == "7737497b7e3e71d18034a9bdaad79b72f9ab80aa" ] && exit 0 || exit 1

