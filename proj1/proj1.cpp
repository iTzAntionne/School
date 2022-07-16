/*****************************************
** File:    proj1.cpp
** Project: CMSC 202 Project 1, Spring 2022
** Author:  Antionne Andries
** Date:    2/16/22
** Section: 10/15
** E-mail:  a345@umbc.edu
***********************************************/
#include <iostream>
#include <string>
#include <ctime>
#include <fstream>

using namespace std;

bool checkWord(string[], string, int);
bool reset(char);
bool checkWin(string, string, int);
string checkLetter(string, string);
void readFile(string[]);
void play();

const int SIZE = 2315;
const char AMP = '&';
const char EXC = '!';

int main(){
    char ans;
    do{
        play();
        cout << "Do you want to play again?(y/n): " << endl;
        cin >> ans;
    }while(reset(ans));
    return 0;
}

//Plays the game
void play(){

    const int RANDOM = rand() % (SIZE - 2) + 1;
    string wordle[SIZE] ;
    string guess;
    readFile(wordle);
    int x = 0;
    string printBoard[6] = {"_____", "_____", "_____",//Prints the board
                            "_____", "_____", "_____"};


    string answer = wordle[RANDOM];

    cout << "Welcome to UMBC Wordle" << '\n' << "Your file was imported"
    << '\n' << "2315 words imported" << '\n' << "Ok, I'm thinking of a five"
                                                " letter word." << '\n'
                                                << "What word would you like to guess?" << endl;

    cin >> guess;

    //Validates the word guess
    while(!checkWord(wordle, guess, SIZE)) {
        cout << "That is not a valid word." << endl;
        cout << "Enter a valid word" << '\n';
        cin.clear();
        cin.ignore(256, '\n');
        cin >> guess;
    }
    while(!checkWin(guess, answer, x)){//Checks if the game was won
        if(checkWord(wordle, guess, SIZE)){//if word guessed prints out line with ampersands and exclamation marks if any
            x++;
            string line = checkLetter(guess, answer);
            for(int i = x - 1; i < x; i++){
                printBoard[i] = line;
            }
            for(int i = 0; i < 6; i++){
                cout << printBoard[i] << endl;
            }
        }
        cout << "Guess again: " << endl;
        cin.clear();
        cin >> guess;
    }
}

//Checks and sees if a letter is in the right position or not
string checkLetter(string guess, string answer){
    string line = "_____";

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            if(guess[i] == answer[j]){
                line[i] = AMP;
            }
        }

        if(guess[i] == answer[i]){
            line[i] = EXC;
        }
    }
    return line;
}

//Checks if the word is a valid word
bool checkWord(string arr[], string guess, int size){
    while(size-- > 0){
       if(guess == arr[size]){
           return true;
       }
    }
    return false;
}

//Checks if the word guessed is the winning word
bool checkWin(string guess, string answer, int guesses){
    if(guess == answer){
        cout << "You guess the right word!" << endl;
        return true;
    }else if(guesses == 5){
        cout << "You lost :( "<< endl;
        cout << "The word was '" << answer << "'" << endl;
        return true;
    }
    return false;
}

// Asks if you want to play the game again
bool reset(char ans){
    if(ans == 'n'){
        cout << "Thank you for playing UMBC Wordle" << endl;
        return false;
    }else{
        cout << "restarting game..." << endl;
        return true;
    }
}

//Reads in the words into an array
void readFile(string arr[]){
    srand(time(NULL));
    string word;
    int x = 0;
    ifstream words ("proj1_data.txt");
    if(words.is_open()) {
        while (words >> word) {
            arr[x] = word;
            x++;
        }
    }
    words.close();
}