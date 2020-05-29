#!/bin/bash

cd ..
mkdir -p bin
cd kernel_stats
make
cd ..
make suite
