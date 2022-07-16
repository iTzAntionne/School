#include "CipherTool.h"
#include "Cipher.h"
#include "Caesar.h"
#include "RailFence.h"
#include "Ong.h"
#include <fstream>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

// Name: CipherTool Constructor
// Desc - Creates a new CipherTool and sets m_filename based on string passed
// Preconditions - Input file passed and populated with Cipher
// Postconditions - CipherTool created
CipherTool::CipherTool(string) {

}

// Name: CipherTool Destructor
// Desc - Calls destructor for all ciphers in m_ciphers
// Preconditions - m_ciphers is populated
// Postconditions - m_ciphers deallocated and vector emptied
CipherTool::~CipherTool() {

}

// Name: LoadFile
// Desc - Opens file and reads in each Cipher. Each Cipher dynamically allocated
// and put into m_ciphers (c is Caesar, r is RailFence, and o is Ong)
// Preconditions - Input file passed and populated with Ciphers
// Postconditions - m_ciphers populated with Ciphers
void CipherTool::LoadFile() {

}

// Name: StringToBoolean
// Desc - Helper function that converts a string to a boolean for reading in file
// Preconditions - Passed string of either 0 or 1
// Postconditions - Returns false if 0 else true
bool CipherTool::StringToBoolean(string input) {
    return false;
}

// Name: DisplayCiphers
// Desc - Displays each of the ciphers in the m_ciphers
// Preconditions - Input file passed and m_ciphers populated
// Postconditions - Displays ciphers
void CipherTool::DisplayCiphers() {

}

// Name: EncryptDecrypt
// Desc - Encrypts or decrypts each of the ciphers in the m_ciphers
// Preconditions - Input file passed and m_ciphers populated
// Postconditions - Either Encrypts or Decrypts each cipher in m_ciphers
void CipherTool::EncryptDecrypt(bool) {

}

// Name: Export
// Desc - Exports each of the ciphers in the m_ciphers (so they can be reused)
// Preconditions - Input file passed and m_ciphers populated
// Postconditions - All ciphers exported
void CipherTool::Export() {

}

// Name: Menu
// Desc - Displays menu and returns choice
// Preconditions - m_ciphers all populated
// Postconditions - Returns choice
int CipherTool::Menu() {
    return 0;
}

// Name: Start
// Desc - Loads input file, allows user to choose what to do
// Preconditions - m_ciphers populated with ciphers
// Postconditions - none
void CipherTool::Start() {

}
