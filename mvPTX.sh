#!/bin/bash
    for file in $1/*.xml ;
    do mv "$file" "${file%.*}.ptx" ;
    done

