# Clear unwanted directores and files
cd src

cd pip
mp reset
cd ..

cd cli
mp reset
cd ..

cd npm
rm -r node_modules
cd ../..

dskill # https://github.com/gadhagod/.DS_Kill