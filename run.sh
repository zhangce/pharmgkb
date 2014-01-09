#! /bin/bash

cd "$(dirname $0)/../..";
ROOT_PATH=`pwd`

$ROOT_PATH/app/pharmgkb/prepare_data.sh
env JAVA_OPTS="-Xmx4g" sbt "run -c $ROOT_PATH/app/pharmgkb/application.conf"
