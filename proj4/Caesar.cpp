#include "Caesar.h"
#include "Cipher.h"
#include <istream>
#include <string>
using namespace std;

// Name: Caesar (Default Constructor)
// Desc: Constructor to build an empty Caesar Cipher (Defaults to shift 3)
// Preconditions - None
// Postconditions - Creates a Caesar cipher to be encrypted
Caesar::Caesar() {
    Cipher();
    m_shift = 3;
}

// Name: Caesar (Overloaded Constructor)
// Desc: Constructor to build a populated Caesar Cipher (Defaults to shift 3)
// Preconditions - Pass it the message, isEncrypted, and shift (any integer)
// Postconditions - Creates a Caesar cipher to be encrypted
Caesar::Caesar(string message, bool isEncrypted, int shift) {
    Cipher(message, isEncrypted);
    m_shift = shift;
}

// Name: Caesar (Destructor)
// Desc: Destructor - Anything specific to Caesar to delete?
// Preconditions - ~Caesar exists
// Postconditions - Caesar destroyed
Caesar::~Caesar() {

}

// Name: Encrypt
// Desc: Shifts characters right based on shift (lower stay lower, upper stay upper)
// Preconditions - Message exists
// Postconditions - Shifts each character "right".
void Caesar::Encrypt() {
    if(GetIsEncrypted()){
        return;
    }

    for(int i = 0; i < GetMessage().size(); i++) {
        unsigned int atChar = int(GetMessage()[i]);
        atChar += m_shift;

        if ((atChar  <= 90 && atChar  >= 65) || (atChar  <= 122 && atChar  >= 97)) {
            GetMessage()[i] = atChar;
        } else if((!(atChar  <= 90 && atChar  >= 65) || !(atChar  <= 122 && atChar  >= 97)) && (atChar - m_shift <= 90 && atChar - m_shift >= 65) || (atChar - m_shift <= 122 && atChar - m_shift >= 97)) {
            GetMessage()[i] = atChar - 26;
        }else{
            GetMessage()[i] = atChar - m_shift;
        }
    }
    SetMessage(GetMessage());
    ToggleEncrypted();
}

// Name: Decrypt
// Desc: Shifts characters left based on shift (lower stay lower, upper stay upper)
// Preconditions - Message exists
// Postconditions - Shifts each character "left".
void Caesar::Decrypt() {
    if(!GetIsEncrypted()){
        return;
    }

    for(int i = 0; i < GetMessage().size(); i++) {
        unsigned int atChar = int(GetMessage()[i]);
        atChar -= m_shift;

        if ((atChar  <= 90 && atChar  >= 65) || (atChar  <= 122 && atChar  >= 97)) {
            GetMessage()[i] = atChar;
        } else if((!(atChar  <= 90 && atChar  >= 65) || !(atChar  <= 122 && atChar  >= 97)) && (atChar + m_shift <= 90 && atChar + m_shift >= 65) || (atChar + m_shift <= 122 && atChar + m_shift >= 97)) {
            GetMessage()[i] = atChar + 26;
        }else{
            GetMessage()[i] = atChar + m_shift;
        }
    }
    SetMessage(GetMessage());
    ToggleEncrypted();
}

// Name: ToString
// Desc - A function that returns the string of the object type
// Preconditions - The object exists
// Postconditions - The subtype is returned (Caesar in this case)
string Caesar::ToString() {
    return "(Caesar)";
}

// Name: FormatOutput()
// Desc - A function that returns the formatted output for Output function
// Preconditions - The object exists (use stringstream)
// Postconditions - c, delimiter, isencrypted, delimiter,
//                  message, delimiter, m_shift are returned for output
string Caesar::FormatOutput() {
    return std::string();
}
