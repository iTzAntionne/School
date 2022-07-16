#include "Port.h"

#include <string>
using namespace std;

Port::Port() {
    m_name = "New Port";
    m_location = "New Location";
    m_west = 0.0;
    m_north = 0.0;
    m_next = nullptr;
}

Port::Port(string name, string location, double north, double west) {
    m_north = north;
    m_west = west;
    m_location = location;
    m_name = name;
    m_next = nullptr;
}

Port::~Port() {

}

string Port::GetName() {
    return m_name;
}

Port *Port::GetNext() {
    return m_next;
}

double Port::GetNorth() {
    return m_north;
}

double Port::GetWest() {
    return m_west;
}

string Port::GetLocation() {
    return m_location;
}

void Port::SetNext(Port *nextPort) {
    m_next = nextPort;
}
