#include<iostream>
template <class T>
class Stack 
{
private:
    T* data;    
    int m_capacity;
    int m_size;
public:
    Stack(int);
    ~Stack();
public:
    void Push(T data);
    void Pop();
    T Top();
    bool isEmpty();
    bool isFull();
};

template<class T>
Stack<T>::Stack(int capacity) : m_capacity(capacity), m_size(0) { data = new T[m_capacity]; }

template<class T> 
Stack<T>::~Stack(){ delete [] data; }


// Adds elements to the stack which is based on resizable, dynamic array.
template<class T>
void Stack<T>::Push(T element)
{
    if (m_size == m_capacity) {
       int new_capacity = 2 * m_capacity;
       T * tmp = new T[new_capacity];
       for (int i = 0; i < m_capacity; i++)
            tmp[i] = data[i];
       delete [] data;
       data = tmp;
       m_size++;
       m_capacity*=2;
       std::cout << new_capacity << " " << m_size << '\n';
       tmp[m_size] = element;
    }
    else {
        m_size++;
        data[m_size] = element;
    }
    std::cout << "Size of steck - " << m_size << '\n';
    std::cout << "Capacity of stack - "  << m_capacity <<'\n';
}

//Remove elements from the stack.
template<class T>
void Stack<T>::Pop(){
    if (m_size != 0) 
    {
        m_size--;
    }
     //  m_size--;
       // T * tmp = new T[m_capacity];
       // for (int i = 0; i < m_size; i++)
       //     tmp[i] = data[i];
       // delete [] data;
       // data = tmp;
    std::cout << "Stack size after pop - " << m_size << '\n';
    std::cout << "Stack capacity after pop - " << m_capacity << '\n';
}

// Shows array last element value.
template<class T>
T Stack<T>::Top()
{
    if (m_size == 0) 
    {
        isEmpty();
    }
    else 
    {
        std::cout << "m_size - " << m_size << '\n';
        std::cout << "Top element- "  << data[m_size] <<'\n';
        return data[m_size];
    }
}

// Check whether stack is empty.
template<class T>
bool Stack<T>::isEmpty()
{
    if (m_size == 0) 
    {
        std::cout << "Stack is empty" << '\n';
        return true;
    }
}

// Check whether stack is full of elements.
template<class T>
bool Stack<T>::isFull()
{
    if (m_size == m_capacity)
    {
        std::cout << "Stack is full" << '\n';
        return true;
    }
}


int main()
{
    Stack<float> s(2);
    s.Pop();
    s.Push(78.9);  
    s.Top(); 
    s.isEmpty();
    s.Push(8.8);
   // s.Pop();
    s.Top();
    s.Push(8.5);
    s.Top();
    s.Push(9.9);
    s.Top();
    s.Pop();
    s.Top();
    s.isFull();
    s.Push(6.7);
    s.Top();
    s.Push(5.9);
    s.Top();
    s.Pop();
    s.Top();
}
