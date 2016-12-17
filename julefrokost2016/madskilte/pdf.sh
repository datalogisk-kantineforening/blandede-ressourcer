#!/bin/sh

cp -a output output-pdf
cd output-pdf
for x in *.svg; do
    svg2pdf_inkscape $x
done
rm *.svg
