#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/charles/hri/human_robot_interaction/puppetbot_ws/src/hlpr_speech/hlpr_speech_recognition"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/charles/hri/human_robot_interaction/puppetbot_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/charles/hri/human_robot_interaction/puppetbot_ws/install/lib/python2.7/dist-packages:/home/charles/hri/human_robot_interaction/puppetbot_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/charles/hri/human_robot_interaction/puppetbot_ws/build" \
    "/usr/bin/python" \
    "/home/charles/hri/human_robot_interaction/puppetbot_ws/src/hlpr_speech/hlpr_speech_recognition/setup.py" \
    build --build-base "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/charles/hri/human_robot_interaction/puppetbot_ws/install" --install-scripts="/home/charles/hri/human_robot_interaction/puppetbot_ws/install/bin"
