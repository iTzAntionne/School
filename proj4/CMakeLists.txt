cmake_minimum_required(VERSION 3.21)
project(proj4)

set(CMAKE_CXX_STANDARD 14)

add_executable(proj4 Caesar.h Cipher.h CipherTool.h RailFence.h proj4.cpp Caesar.cpp Cipher.cpp CipherTool.cpp RailFence.cpp Ong.cpp)
