import numpy as np
import time 

from fastga import convert_normals_to_hilbert, GaussianAccumulatorKD, MatX3d

def main():
    normals = np.array([
        [-1, 0, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, -1, 0]
    ])
    t0 = time.perf_counter()
    ga = GaussianAccumulatorKD(0, 100)
    t1 = time.perf_counter()
    print("Number of Buckets: {}".format(len(ga.buckets)))
    print(ga.buckets)
    converted = MatX3d(normals)
    print(np.asarray(converted))
    t2 = time.perf_counter()
    bucket_indexes = ga.get_bucket_indexes(converted)
    t3 = time.perf_counter()
    print(np.asarray(bucket_indexes))
    print("Building Index Took: {}; Query Took: {}".format((t1-t0) * 1000, (t3 - t2)* 1000))
    

if __name__ == "__main__":
    main()