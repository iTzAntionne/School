#include "Route.h"

#include <fstream>
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

Route::Route() {
    m_size = 0;
    m_head = nullptr;
    m_head = nullptr;
    m_name = "Test";
}

void Route::SetName(string name) {
    m_name = name;
}

Route::~Route() {
    Port *curr = m_head; //Node pointer to m_head
    while(curr != nullptr){ //Iterates and removes each node
        m_head = curr; //sets m_head to curr
        curr = curr->GetNext(); //moves curr to next node
        delete m_head;
    }
    m_head = nullptr;
}

void Route::InsertEnd(string name, string location, double north, double west) {
    Port *temp = new Port(name, location, north, west);
    Port *start = m_head;

    if(m_head == nullptr){
        m_head = temp;
        temp->SetNext(nullptr);
        return;
    }
    while (start->GetNext() != nullptr){
        start = start->GetNext();
    }
    temp->SetNext(nullptr);
    start->SetNext(temp);
    m_size++;
}

void Route::RemovePort(int port) {
    Port *curr = m_head;
    Port *ind = new Port;
    int inc = 0;

    if (port == 1){
        m_head = curr->GetNext();
    }else{
        while (curr != nullptr){
            curr = curr->GetNext();
            inc++;
        }
        if (port > 2 && port <= inc){
            curr = m_head;
            for(int i = 1; i < port;i++){
                ind = curr;
                curr = curr->GetNext();
            }
            ind->SetNext(curr->GetNext());
        }
        else{
            cout << "Two ports must always be present, cannot delete." <<endl;
        }
        delete curr;
    }
}

string Route::GetName() {
    return m_name;
}

string Route::UpdateName() {
    string name;
    Port *temp = m_head;
    name += temp->GetName() + " to ";
    while(temp != nullptr){
        temp = temp->GetNext();
    }
    name += temp->GetName();
    return name;
}

int Route::GetSize() {
    return m_size;
}

void Route::ReverseRoute() {
    Port *prev, *curr, *next;
    if (m_head == nullptr){
        cout<< "List is empty" <<endl;
        return;
    }

    if(m_head->GetNext() == nullptr){
        return;
    }

    prev = m_head;
    curr = prev->GetNext();
    next = curr->GetNext();
    prev->SetNext(nullptr);
    curr->SetNext(prev);
    while (next != nullptr){
        prev = curr;
        curr = next;
        next = next->GetNext();
        curr->SetNext(prev);
    }
    m_head = curr;
}

Port *Route::GetData(int index) {
    if(index > m_size || index < 0) {
        return nullptr;
    }

    Port *start = m_head;
    int inc = 0;

    while(start != nullptr && index != inc){
        start = start->GetNext();
        inc++;
    }
    return start;
}

void Route::DisplayRoute() {
    Port *temp = m_head;
    if (m_head == nullptr){
        cout << "The List is Empty" << endl;
        return;
    }

    if(m_size < 2){
        cout << "There are not enough ports to be displayed currently. " << endl;
        return;
    }

    cout<< "Ports: " << endl;
    while (temp != nullptr){
        cout << temp << ", " << temp->GetNorth() << ", " << temp->GetWest() << endl;
        temp = temp->GetNext();
    }
}
