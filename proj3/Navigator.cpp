#include "Route.h"
#include "Navigator.h"
#include "Port.h"

#include <string>
#include <iostream>
#include <vector>
using namespace std;

Navigator::Navigator(string fileName) {
    m_fileName = fileName;
}

Navigator::~Navigator() {

}

void Navigator::Start() {
    ReadFile();
    MainMenu();
}

void Navigator::DisplayPorts() {
    if (m_ports.empty()) { //Checks to see if the linked list is empty
        cout << "There are no ports" << endl; //Output if it is empty
        return;
    } else {
        for (int i = 0; i < int(m_ports.size()); i++) { //Iterates to end of list
            cout << i + 1 << ") " << m_ports[i]->GetName() << ", " << m_ports[i]->GetLocation() << endl; //Outputs value in port
        }
    }
}

void Navigator::ReadFile() {
    string name, location, north, west;
    ifstream Ports(m_fileName);

    if (Ports.is_open()) {
        while (getline(Ports, name, ',') &&
               getline(Ports, location, ',')&&
               getline(Ports, north, ',')&&
               getline(Ports, west)) {

            Port *port = new Port(name, location, stod(north), stod(west));
            m_ports.push_back(port);
        }
        Ports.close();
    }
}

void Navigator::InsertNewRoute() {
    int choice = -2;
    DisplayPorts();
    cout << "Enter the port number you would like to add to the Route: (enter 0 to end): " << endl;
    cin>>choice;
    Route *route = new Route;

    while(choice != 0){
        if(choice > -1 && choice < int(m_ports.size())){
            route->InsertEnd(m_ports.at(choice-1)->GetName(), m_ports.at(choice-1)->GetLocation(),
                             m_ports.at(choice-1)->GetNorth(), m_ports.at(choice-1)->GetWest());
            cout << "Route added " << endl;
        }
        else{
            cout << "Enter a valid index." << endl;
        }
        DisplayPorts();
        cout << "Enter the port number you would like to add to the Route: (enter 0 to end): " << endl;
        cin>>choice;
    }
    if(route->GetSize() > 1){
        string name = route->UpdateName();
        m_routes.push_back(route);
        cout << "Route added." << endl;
    }else{
        cout << "Route could not be added (need 2)." << endl;
    }
}

void Navigator::MainMenu() {
    int choice = 0;

    do{
        cout << "What would you like to do?: " << "\n"
             << "1. Create New Route" << "\n"
             << "2. Display Route" << "\n"
             << "3. Remove Port From Route" << "\n"
             << "4. Reverse Route" << "\n"
             << "5. Exit" << endl;
        cin >> choice;

        switch(choice){
            case 1:
                InsertNewRoute();
                break;

            case 2:
                DisplayRoute();
                break;

            case 3:
                RemovePortFromRoute();
                break;

            case 4:
                ReverseRoute();
                break;

            case 5:
                break;

            default:
                cout << "Input a valid choice." << endl;
        }
    }while(choice != 5);
}

int Navigator::ChooseRoute() {
    int ind = -1;
    if(m_routes.size() != 0){
        cout << "Choose a route: " << endl;
        for(unsigned int i = 0; i < m_routes.size(); i++){
            cout << i + 1 << ") " << m_routes[i]->GetName() << endl;
        }
        cin >> ind;
    }else{
        cout << "No routes have been created yet." << endl;
    }

    return ind-1;
}

void Navigator::DisplayRoute() {
    m_routes[ChooseRoute()]->DisplayRoute();
}

void Navigator::RemovePortFromRoute() {
    int ind = ChooseRoute();
    m_routes[ind]->RemovePort(ind);
    if(ind == 2-1){
        m_routes[ind+1]->SetName(m_ports[ind]->GetName());
        m_routes.at(ind)->UpdateName();
    }else if(ind == int(m_routes.size() - 1)){
        m_routes[ind-1]->SetName(m_ports[ind]->GetName());
        m_routes[ind-1]->UpdateName();
    }
}

double Navigator::RouteDistance(Route *) {
    return 0;
}

void Navigator::ReverseRoute() {
    int ind = ChooseRoute();
    m_routes.at(ind)->ReverseRoute();
    m_routes[ind]->SetName(m_ports[ind]->GetName());
    m_routes.at(ind)->UpdateName();
}
