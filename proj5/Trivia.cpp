/*****************************************************************************
 ** File: Trivia.cpp
 ** Project: CMSC 202 Project 5, Spring 2022
 ** Author:  Kush Shah and CMSC202
 ** Date:    04/05/2022
 ** Email:   k216@umbc.edu
 **
 Description: CPP file for Trivia class. Includes both class definition and
 class function definitions. Loads a file of trivia questions
*****************************************************************************/

#ifndef TRIVIA_CPP
#define TRIVIA_CPP
#include "Lqueue.cpp"
#include "Question.cpp"
#include <fstream>
#include <vector>
using namespace std;

const string DEFAULT_FILE = "proj5_string.txt";
const char DELIMITER = '|';

template <class T>
class Trivia {
public:
  // Name: Default Constructor
  // Desc: Displays the title, Loads Questions and calls menu
  // Indicates if the file was not loaded.
  // Precondition: None
  // Postcondition: User is prompted with assignment menus
  Trivia(string filename);

  // Name: Destructor
  // Desc: Deallocates memory allocated for the Questions and
  // resets all variables.
  // Precondition: A Trivia exists.
  // Postcondition: All dynamically allocated memory in Trivia is deleted.
  ~Trivia();

  // Name: LoadQuestions
  // Desc: Each input file will be for a specific type of question (int, double, string)
  //       Reads in Questions from a file and stores them in anLqueue.
  //       An input file will be for exactly one type of question (int, double, string)
  // Precondition: None.
  // Postcondition: Returns true if file was read. Otherwise, it returns false.
  bool LoadQuestions(string filename);

  // Name: MainMenu
  // Desc: Presents user with menu options for showing subjects and allowing
  // user to work on a subject.
  // Precondition: None.
  // Postcondition: The main menu is presented.
  void MainMenu();

  // Name: DisplaySubjects
  // Desc: Presents all Subjects with corresponding numerical identifiers.
  // Precondition: Subjects have been added.
  // Postcondition: All assignments are printed to the screen.
  void DisplaySubjects();

  // Name: StartSubject
  // Desc: Starts working on a selected Subject.
  // Displays the number of questions in subject.
  // Starts at beginning and goes through each question.
  // After all questions have been answered:
  //       displays total correct, incorrect, and percentage correct
  // Precondition: m_questions has been populated
  // Postcondition: Returns to main menu
  void StartSubject();

  // Name: AddSubject
  // Desc: Checks to see if a subject exists in m_subjects.
  //       If not, inserts subject into m_subjects.
  // Precondition: A Subject exists.
  // Postcondition: Add subject to m_subjects if new subject.
  void AddSubject(string subject);

  // Name: ChooseSubject
  // Desc: Allows a user to choose one of the subjects to work on. Lists all subjects
  // in m_subjects and allows use to choose one. Returns value - 1 (location in vector)
  // Precondition: A Subject exists.
  // Postcondition: Returns value entered minus one
  int ChooseSubject();

  // Name: QuestionsPerSubject
  // Desc: Iterates over m_questions and counts how many questions match the subject
  // passed into function
  // Precondition: A Subject exists.
  // Postcondition: Returns number of questions of a particular subject
  int QuestionsPerSubject(string subject);

  // Name: DisplayTitle
  // Desc: Displays opening Welcome message
  // Precondition: None.
  // Postcondition: Title is displayed.
  void DisplayTitle();

private:
  Lqueue<Question<T>* >* m_questions; // Holds questions using a specific data type
  vector<string> m_subjects; //Populated as file is loaded
};

//**********Implement Trivia Class Here***********
template <class T>
Trivia<T>::Trivia(string filename) { // starts the trivia game
    DisplayTitle(); // displays title
    if(LoadQuestions(filename)){ // checks filename correct
        MainMenu();
        cout << "Thanks for playing UMBC trivia!" << endl;
    }else{
        cout << "Could not read file." << endl;
    }

}

template <class T>
Trivia<T>::~Trivia<T>() { //destroys all dynamically allocated memory
    for(int i = 0; m_questions->GetSize(); i++){
        delete m_questions->At(i);
    }

    if(m_questions)
        m_questions->Clear();

    delete m_questions;
}

template <class T>
void Trivia<T>::DisplaySubjects() { // displays all subjects
    for(int i = 0; i < int(m_subjects.size()); i++){
        cout << i + 1 << "." << m_subjects[i] << endl;
    }
}

template <class T>
void Trivia<T>::DisplayTitle() { // displays title
    cout << "Welcome to UMBC Trivia!" << endl;
}

template <class T>
void Trivia<T>::AddSubject(string subject) {
    bool added = false;

    if(m_subjects.size() == 0){ // checks if size is 0
        m_subjects.push_back(subject);
    }else{
        for(int i = 0; i < int(m_subjects.size()); i++){ // iterates through size of m subs
            if(m_subjects.at(i) == subject){ // checks if sub in m subject
                added = true;
            }
        }
    }
    if(!added){ // if not
        m_subjects.push_back(subject); // add subject
    }
}

template <class T>
int Trivia<T>::ChooseSubject() {
    int choice = -1;

    while(choice < 1 || choice > int(m_subjects.size())){ // checks if invalid
        cout << "What subject would you like to attempt?" << endl;
        DisplaySubjects();
        cin >> choice;

        if(choice < 1 || choice > int(m_subjects.size())){ // if invalid enter valid choice
            cout << "Enter a valid option" << endl;
        }
    }
    return choice - 1;
}

template <class T>
void Trivia<T>::StartSubject() {
    int right = 0;
    int wrong = 0;
    int count = 1;
    int subs = ChooseSubject();

    cout << "There are " << QuestionsPerSubject(m_subjects[subs]) << " question(s) in this subject." << endl;

    for(int i = 0; i < m_questions->GetSize(); i++){ // iterates through m questions
        T ans;
        if(m_questions->At(i)->m_subject == m_subjects[subs]){ // checks if that q is in m subjects
            cout << count << ". Question: " << *m_questions->At(i) << endl
                 << "Please answer with a(n) " << m_questions->At(i)->m_subject << endl;
            count++;

            cin >> ans;

            if(m_questions->At(i)->m_answer == ans){ // checks if correct
                right++;
                cout << "Correct" << endl;
            }else{ // else wrong
                wrong++;
                cout << "Incorrect" << endl;
            }
        }

    }

    cout << "You got " << right << " questions correct." << endl;
    cout << "You got " << wrong << " questions incorrect." << endl;
    cout << "Which is " << right/(right+wrong) << "%." << endl; // calculates %
}

template <class T>
int Trivia<T>::QuestionsPerSubject(string subject) {
    int numSubs = 0;
    for(int i = 0; i < m_questions->GetSize(); i++){ // iterates through m questions
        if(m_questions->At(i)->m_subject == subject){ // checks if that sub matches
            numSubs++; // counts sub
        }
    }
    return numSubs;
}

template <class T>
bool Trivia<T>::LoadQuestions(string filename) {
    //initialize vars
    ifstream theFile(filename);
    string subject, question, answerType, difficulty, trash;
    T answer;
    if(theFile.is_open()) {
        m_questions = new Lqueue<Question<T>*>();
        //getline in the while condition
        while (
                getline(theFile, subject, DELIMITER) &&
                getline(theFile, question, DELIMITER) &&
                getline(theFile, answerType, DELIMITER) &&
                getline(theFile, difficulty, DELIMITER)) {
            theFile >> answer;
            getline(theFile, trash);
            //initialize new question
            //public members can be directly set
            Question<T> *theQ = new Question<T>(subject, question, answerType, stoi(difficulty), answer);
            m_questions->Push(theQ);
            AddSubject(subject);
        }
        //close file
        //successful load
        theFile.close();
        return true;
    }
    //file didn't open
    return false;
}

template <class T>
void Trivia<T>::MainMenu() {
    int choice = 0;
    do{ // prompts user
        cout << "Choose an option." << endl
             << "1. Display Subjects " << endl
             << "2. Start Subject " << endl
             << "3. Quit " << endl;
        cin >> choice;

        if(choice > 0 && choice < 4){
            switch (choice){ // check choice

                case 1:

                    DisplaySubjects(); // displays sub
                    break;
                case 2:

                    StartSubject(); // starts sub
                    break;
                case 3:
                    break;
            }
        }else{
            cout << "Enter a valid option" << endl;
        }

    }while(choice != 3);

}


#endif
