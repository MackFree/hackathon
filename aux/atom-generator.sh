#!/bin/bash

for file in assets/img/*.png
do
    if [[ "$file" != *"-small.png" ]]
    then
        atom_name="$(echo ${file} | cut -d '/' -f 3)"
        atom_name="${atom_name%.png}"
        echo "${atom_name} = Atom(\"${atom_name}\".title(), 0, 0, 0, \"${file}\", \"${file%.png}.txt\")"
    fi
done
