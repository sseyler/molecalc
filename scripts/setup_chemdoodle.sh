#!/bin/bash

VERSION=11.9.0

cd molcalc/static/

wget https://web.chemdoodle.com/downloads/ChemDoodleWeb-${VERSION}.zip

unzip ChemDoodleWeb-${VERSION}.zip

mkdir chemdoodleweb

cp -r ChemDoodleWeb-${VERSION}/install/* chemdoodleweb/
cp -r ChemDoodleWeb-${VERSION}/src/* chemdoodleweb/

rm -r ChemDoodleWeb-${VERSION}*


