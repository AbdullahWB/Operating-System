# Performance Comparison:

## Non-threaded:
    * Sequential, slower for multiple files, no parallelism.
## Threaded:
    * Concurrent, faster for multiple files, but GIL limits true parallelism in Python.


# Priority Scheduling Impact:

## Non-threaded: 
    * No effect, processes run sequentially.

## Threaded: 
    *Prioritizing threads could optimize resource use, improve response time for critical tasks, but requires thread priority management.



