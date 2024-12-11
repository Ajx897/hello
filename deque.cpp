#include <iostream>
using namespace std;

class Deque {
private:
    int* arr;
    int front;
    int rear;
    int size;
    int capacity;

public:
    Deque(int cap) {
        capacity = cap;
        arr = new int[capacity];
        front = -1;
        rear = -1;
        size = 0;
    }

    bool isFull() {
        return size == capacity;
    }

    bool isEmpty() {
        return size == 0;
    }

    void addFront(int element) {
        if (isFull()) {
            cout << "Deque is full, cannot add to front." << endl;
            return;
        }
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (front == 0) {
            front = capacity - 1;
        } else {
            front--;
        }
        arr[front] = element;
        size++;
    }

    void addRear(int element) {
        if (isFull()) {
            cout << "Deque is full, cannot add to rear." << endl;
            return;
        }
        if (rear == -1) {
            front = 0;
            rear = 0;
        } else if (rear == capacity - 1) {
            rear = 0;
        } else {
            rear++;
        }
        arr[rear] = element;
        size++;
    }
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty, cannot delete from front." << endl;
            return;
        }
        cout << "Deleted " << arr[front] << " from the front." << endl;
        if (front == rear) {
            front = rear = -1;  
        } else if (front == capacity - 1) {
            front = 0;
        } else {
            front++;
        }
        size--;
    }

    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty, cannot delete from rear." << endl;
            return;
        }
        cout << "Deleted " << arr[rear] << " from the rear." << endl;
        if (front == rear) {
            front = rear = -1;
        } else if (rear == 0) {
            rear = capacity - 1;
        } else {
            rear--;
        }
        size--;
    }

    void display() {
        if (isEmpty()) {
            cout << "Deque is empty." << endl;
            return;
        }
        cout << "Deque elements are: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) {
                break;
            }
            i = (i + 1) % capacity;
        }
        cout << endl;
    }

    ~Deque() {
        delete[] arr;
    }
};
int main() {
    Deque dq(5);  
    dq.addRear(10);
    dq.addRear(20);
    dq.addFront(5);
    dq.addFront(2);
    dq.addRear(30);
    dq.display(); 
    dq.deleteFront();  
    dq.deleteRear();   
    dq.display();  

    return 0;
}
