# PGI Compiler Suite

| Command

 | Language

 | Compiler

 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------- | ---------- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pgf77

                                   | FORTRAN 77

                                                                                                                                                                                                                                                                                                                                          | PGF77

                                              |
| pgf95 

                                 | Fortran 90/95/F2003

                                                                                                                                                                                                                                                                                                                                 | PGF95

                                              |
| pgfortran 

                             | PGI Fortran

                                                                                                                                                                                                                                                                                                                                         | PGFORTRAN

                                          |
| pghpf

                                   | High Performance Fortran

                                                                                                                                                                                                                                                                                                                            | PGHPF

                                              |
| pgcc

                                    | ANSI C99 and K&R C

                                                                                                                                                                                                                                                                                                                                  | PGCC C

                                             |
| pgCC

                                    | ANSI C++ with cfront features

                                                                                                                                                                                                                                                                                                                       | PGC++

                                              |
| pgdbg

                                   | Source code debugger

                                                                                                                                                                                                                                                                                                                                | PGDBG

                                              |
| pgprof

                                  | Performance profiler

                                                                                                                                                                                                                                                                                                                                | PGPROF

                                             |
`hello.f90` is a Fortran program.  Compile and execute this program
interactively by entering the following commands into the console:

```bash
module load pgi
pgf95 hello.f90
./a.out
```
