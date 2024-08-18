# Cicero Compiler CPP

Compiler for translating Regular Expressions (REs) into a domain specific ISA for [Cicero](https://github.com/necst/cicero).

## Build with Docker

The simplest way to build the compiler is by using [Docker](https://docs.docker.com/engine/install/). `Docker/Dockerfile` is provided to build the image:

```bash
# Build docker image which contains build dependencies
docker build -t cicero_build_environment:latest Docker

# Run build and test within docker image
docker run -v $PWD:/app cicero_build_environment:latest /bin/bash /app/Docker/build_and_test.sh
```

## Build manually 

Install dependencies first:

```bash
# Ubuntu Linux
# Add LLVM apt repository, follow instruction on https://apt.llvm.org/
apt install libmlir-16-dev mlir-16-tools llvm-16-dev antlr4 libantlr4-runtime-dev cmake

# Fedora Linux
dnf install cmake antlr4 antlr4-cpp-runtime-devel mlir-devel llvm-devel
```

1. `cmake`: cross platform build file generator
2. `antlr4`: tool for building parser/lexer from declarative grammar/tokens
3. `antlr4-cpp-runtime-devel`: C++ runtime for antlr4
4. `mlir-devel`: intermediate representation library
5. `llvm-devel`: compiler infrastructure library

Once dependencies are installed, clone this repo and `cd` into it:

```bash
mkdir build
cd build
# Optional, only if you want to build tests
git submodule update --init --recursive
# If you don't want to build tests, add `-DBUILD_TESTING=OFF` to the next command
cmake ..
cmake --build .
```

## Usage

Once built, the compiler executable can be found in `./build/ciceroc`.

To compiler an example `ab|cd` RE into `out.cicero`, enabling all optimizations, you can run:

`./build/ciceroc --regex="ab|cd" --emit=compiled -o out.cicero -Oall`

Different output targets can be achieved by specifying one of the available options: `--emit=regexmlir|ciceromlir|ciceromlir.dot|compiled`.

Optimizations can be enabled all together (`-Oall`), or one by one: `-Oregex`, `-Oregexboundary`, `-Ojump`.

Output binary can be inspected using `./build/objdump binary.cicero`

## Paper Citation

If you find this repository useful, please use the following citations:

```
@inproceedings{somaini2025cicero,
    title = {Combining MLIR Dialects with Domain-Specific Architecture for Efficient Regular Expression Matching},
    author = {Andrea Somaini and Filippo Carloni and Giovanni Agosta and Marco D. Santambrogio and Davide Conficconi},
    year = 2025,
    month = {mar},
    booktitle={2025 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)}
 } 
```
