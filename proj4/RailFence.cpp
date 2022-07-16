#include "Cipher.h"
#include "RailFence.h"
#include <istream>
#include <string>
using namespace std;

// Name: RailFence (Default Constructor)
// Desc: Constructor to build an empty RailFence Cipher (Defaults to 3 rails)
// Preconditions - None
// Postconditions - Creates a RailFence cipher
RailFence::RailFence() {
    Cipher();
    m_rails = 3;
}

// Name: RailFence (Overloaded Constructor)
// Desc: Constructor to build a populated RailFence Cipher (Defaults to 3 rails)
// Preconditions - Pass it the message, isEncrypted, and number of rails (any integer)
// Postconditions - Creates a RailFence cipher to be encrypted
RailFence::RailFence(string message, bool isEncrypted, int nRails) {
    Cipher(message, isEncrypted);
    m_rails = nRails;
}

// Name: RailFence (Destructor)
// Desc: Destructor - Anything specific part of RailFence to delete?
// Preconditions - ~RailFence exists
// Postconditions - RailFence destroyed
RailFence::~RailFence() {

}

// Name: Encrypt
// Desc: Letters are placed on a fence rail based on the number of rails
//       Letters are read from one rail at a time into a single string
// Preconditions - Message exists
// Postconditions - A single encrypted string is stored
void RailFence::Encrypt() {
    
}

// Name: Decrypt
// Desc: Single encrypted string is pushed back on the rails and reversed
// Preconditions - Message exists
// Postconditions - The decrypted string is stored
void RailFence::Decrypt() {

}

// Name: ToString
// Desc - A function that returns the string of the object type
// Preconditions - The object exists
// Postconditions - The subtype is returned (RailFence in this case)
string RailFence::ToString() {
    return std::string();
}

// Name: FormatOutput()
// Desc - A function that returns the formatted output for Output function
// Preconditions - The object exists (use stringstream)
// Postconditions - r, delimiter, isencrypted, delimiter,
//                  message, delimiter, m_rails are returned for output
string RailFence::FormatOutput() {
    return std::string();
}

