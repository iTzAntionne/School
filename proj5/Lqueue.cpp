#ifndef LQUEUE_CPP
#define LQUEUE_CPP
#include <string>
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

//Templated node class used in templated linked list
template <class T>
class Node {
    public:
      Node(const T& data); //Constructor
      void SetData(const T& data); //Sets data in node
      void SetNext(Node<T>* next); //Sets next pointer
      T& GetData(); //Gets data from node
      Node<T>* GetNext(); //Gets next pointer
    private:
      T m_data;
      Node<T>* m_next;
};

//Overloaded constructor for Node
template <class T>
Node<T>::Node( const T& data) {
   m_data = data;
   m_next = NULL;
}

//Returns the data from a Node
template <class T>
T& Node<T>::GetData() {
   return m_data;
}

//Sets the data in a Node
template <class T>
void Node<T>::SetData( const T& data) {
   m_data = data;
}

//Gets the pointer to the next Node
template <class T>
Node<T>* Node<T>::GetNext() {
   return m_next;
}

//Sets the next Node
template <class T>
void Node<T>::SetNext( Node<T>* next) {
   m_next = next;
}

template <class T>
class Lqueue {
 public:
  // Name: Lqueue() (Linked List Queue) - Default Constructor
  // Desc: Used to build a new linked queue (as a linked list)
  // Preconditions: None
  // Postconditions: Creates a new lqueue where m_head and m_tail point to nullptr
  // Required
  Lqueue();

  // Name: ~Lqueue() - Destructor
  // Desc: Used to destruct a Lqueue
  // Preconditions: There is an existing lqueue with at least one node
  // Postconditions: An lqueue is deallocated (including dynamically allocated nodes)
  //                 to have no memory leaks!
  // Required
 ~Lqueue();

  // Name: Lqueue (Copy Constructor)
  // Preconditions: Creates a copy of existing LQueue
  //                Requires a Lqueue
  // Postconditions: Copy of existing Lqueue
  // Required
  Lqueue(const Lqueue&);

  // Name: operator= (Overloaded Assignment Operator)
  // Preconditions: Copies an Lqueue into an existing Lqueue
  //                Requires a Lqueue
  // Postconditions: Copy of existing Lqueue
  // Required
  Lqueue<T>& operator= (Lqueue&);

  // Name: Push
  // Preconditions: Takes in data. Creates new node. 
  //                Requires a Lqueue
  // Postconditions: Adds a new node to the end of the lqueue.
  // Required
  void Push(const T&);

  // Name: Pop
  // Preconditions: Lqueue with at least one node. 
  // Postconditions: Removes first node in the lqueue, returns data from first node.
  // Required
  T Pop();

  // Name: Display
  // Preconditions: Outputs the lqueue.
  // Postconditions: Displays the data in each node of lqueue
  // Required (used only for testing)
  void Display();

  // Name: Front
  // Preconditions: Requires a populated lqueue
  // Postconditions: Returns whatever data is in front
  // Required
  T Front();

  // Name: IsEmpty
  // Preconditions: Requires a lqueue
  // Postconditions: Returns if the lqueue is empty.
  // Required
  bool IsEmpty();

  // Name: GetSize
  // Preconditions: Requires a lqueue
  // Postconditions: Returns m_size
  // Required
  int GetSize();

  // Name: Find()
  // Preconditions: Requires a lqueue
  // Postconditions: Iterates and if it finds the thing, returns index, else -1
  // Required
  int Find(T&);

  // Name: Swap(int)
  // Preconditions: Requires a lqueue
  // Postconditions: Swaps the nodes at the index with the node prior to it.
  // Required
  void Swap(int);

  // Name: Clear
  // Preconditions: Requires a lqueue
  // Postconditions: Removes all nodes in a lqueue
  // Required
  void Clear();

  // Name: At
  // Precondition: Existing Lqueue
  // Postcondition: Returns object from Lqueue at a specific location
  // Desc: Iterates to node x and returns data from Lqueue
  // Required
  T At (int x);

private:
  Node <T> *m_head; //Node pointer for the head
  Node <T> *m_tail; //Node pointer for the tail
  int m_size; //Number of nodes in queue
};

//**********Implement Lqueue Class Here***********
//**********All Functions Are Required Even If Not Used for Trivia**************

template<class T>
Lqueue<T>::Lqueue() { // initializes queue
    m_head = nullptr;
    m_tail = nullptr;
    m_size = 0;
}

template<class T>
Lqueue<T>::~Lqueue() {
//    Node<T> *ptr = m_head;
//    while(ptr != nullptr){
//        m_head = ptr; //sets m_head to ptr
//        ptr = ptr->GetNext(); //moves ptr to next node
//        delete m_head;
//    }
    this->Clear(); // destroys queue
    m_head = nullptr;
    m_tail = nullptr;
    m_size = 0;
}

template<class T>
Lqueue<T>::Lqueue(const Lqueue &source) { // deep copies vars
    m_head = source.m_head;
    m_tail = source.m_tail;
    m_size = source.m_size;
}

template<class T>
Lqueue<T> &Lqueue<T>::operator=(Lqueue &source) {
    if(&source == this){
        return *this;
    }
    m_head = source.m_head;
    m_tail = source.m_tail;
    m_size = source.m_size;

    return *this;
}

template<class T>
void Lqueue<T>::Push(const T &data) {
    Node <T> *track = new Node <T>(data);

    if(m_head == nullptr){ // makes the head and tail point to the data
        m_head = track;
        m_tail = track;
    }else{
        m_tail->SetNext(track); // adds node to the end of the queue
        m_tail = track;

    }

    m_size++;

}

template<class T>
T Lqueue<T>::Pop() { // pops the first node of the queue off
    if(m_size == 0){ // checks if empty
        cout << "Queue is empty" << endl;
        return NULL;
    }

    Node<T> *track = m_head;
    T data = Front();
    m_head = m_head->GetNext();


    if(m_head == nullptr){
        m_tail = nullptr;
    }

    delete track; // deletes node
    m_size--;

    return data;
}

template<class T>
void Lqueue<T>::Display() { // displays all the data for each node
    Node<T> *track = m_head;
    while(track != nullptr){
        cout << track->GetData() << endl;
        track = track->GetNext();
    }
}

template <class T>
T Lqueue<T>::Front() { // gets the m head val
    if (m_head == nullptr) {
        return NULL;
    }
    return m_head->GetData();
}

template<class T>
bool Lqueue<T>::IsEmpty() { // checks if queue is empty
    return m_head == nullptr;
}

template<class T>
int Lqueue<T>::GetSize() { // returns size
    return m_size;
}

template<class T>
int Lqueue<T>::Find(T &target) { // finds the data  given a target
    if(IsEmpty()){
        return -1;
    }

    Node<T> *track = m_head;
    for(int i = 0; i < m_size; i++){ //iterates through the queue
        if(track->GetData() == target) // finds target
            return i;
        else
            track = track->GetNext();
    }

    if(track == nullptr){
        return -1;
    }
    return -1;
}

//template<class T>
//void Lqueue<T>::Swap(int) {
//    if(!m_head){
//        return m_head;
//    }
//    Node<T> *first = m_head;
//    Node<T> *second = m_head->GetNext();
//    Node<T> *temp = new Node<T> ;
//    temp->GetNext() = first;
//    Node<T> *prev = temp;
//
//    while(second){
//        Node<T> *temp2 = second->GetNext();
//        first->GetNext() = second->GetNext();
//        second->GetNext() = first;
//        prev->GetNext() = second;
//        prev = first;
//
//        if(temp2){
//            first = temp;
//            second = temp2->GetNext();
//        }
//
//    }
//    return temp->GetNext();
//
//}

template <class T>
void Lqueue<T>::Clear() {
    //cheks if head is null else pops
    while (m_head) {
        Pop();
    }

    m_tail = nullptr;
    m_size = 0;
}

template<class T>
T Lqueue<T>::At(int target) {
    Node<T> *track = m_head;
    for(int i = 0; i < target; i++){ // finds the target index and outputs data
        track = track->GetNext();
    }
    return track->GetData();
}

#endif
