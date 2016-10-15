# Install script for directory: /home/charles/hri/human_robot_interaction/puppetbot_ws/src/hlpr_speech/hlpr_speech_recognition

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/charles/hri/human_robot_interaction/puppetbot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/hlpr_speech_recognition.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hlpr_speech_recognition/cmake" TYPE FILE FILES
    "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/hlpr_speech_recognitionConfig.cmake"
    "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/hlpr_speech_recognitionConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hlpr_speech_recognition" TYPE FILE FILES "/home/charles/hri/human_robot_interaction/puppetbot_ws/src/hlpr_speech/hlpr_speech_recognition/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/hlpr_speech_recognition" TYPE PROGRAM FILES "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/speech_recognizer")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/hlpr_speech_recognition" TYPE PROGRAM FILES "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/speech_listener")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/hlpr_speech_recognition" TYPE PROGRAM FILES "/home/charles/hri/human_robot_interaction/puppetbot_ws/build/hlpr_speech/hlpr_speech_recognition/catkin_generated/installspace/speech_gui")
endif()

