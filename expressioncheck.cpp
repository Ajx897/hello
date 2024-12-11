#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to check if the given expression is well-parenthesized
bool isBalanced(string expression) {
    stack<char> s;  // Stack to store opening parentheses

    // Loop through each character in the expression
    for (char ch : expression) {
        // If it's an opening bracket, push it onto the stack
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        }
        // If it's a closing bracket, check if it matches the top of the stack
        else if (ch == ')' || ch == '}' || ch == ']') {
            // If the stack is empty or the top element doesn't match, it's unbalanced
            if (s.empty()) {
                return false;
            }

            // Check if the current closing bracket matches the top of the stack
            char top = s.top();
            if ((ch == ')' && top == '(') || 
                (ch == '}' && top == '{') || 
                (ch == ']' && top == '[')) {
                s.pop();  // Pop the matching opening bracket
            } else {
                return false;  // Mismatched parentheses
            }
        }
    }

    // If the stack is empty, it means all parentheses were matched
    return s.empty();
}

int main() {
    string expression;

    // Input expression
    cout << "Enter an expression: ";
    getline(cin, expression);

    // Check if the expression is well-parenthesized
    if (isBalanced(expression)) {
        cout << "The expression is well-parenthesized." << endl;
    } else {
        cout << "The expression is not well-parenthesized." << endl;
    }

    return 0;
}
