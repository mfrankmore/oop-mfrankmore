/*
    State Pattern Code Example - This example descirbes the time for someone to wake up depending if it is a weekday or weekend
    Matt Frankmore
*/

#include <iostream>
#include <typeinfo>

using namespace std;

class Context;

//All methods that all concrete states should implement
class State {

    protected:
    Context *_context;

    public:
    virtual ~State() {
    }

    void setContext(Context *context) {
        this->_context = context;
    }

    virtual void handle1() = 0;
    virtual void handle2() = 0;
};

class Context {

    private:
    State *_state;

    public:
    //Context allows switching state at runtime
    Context(State *state) : _state(nullptr) {
        this->transitionTo(state);
    }
    
    ~Context() {
        delete _state;
    }

    //Outputs the transition to console and switches states
    void transitionTo(State *state) {
        cout << "Context: Transition to " << typeid(*state).name() << ".\n";
        if (this->_state != nullptr)
            delete this->_state;
        this->_state = state;
        this->_state->setContext(this);
    }

    void request1() {
        this->_state->handle1();
    }

    void request2() {
        this->_state->handle2();
    }

};

/*
*   Concrete State implementations
*/

class Weekday : public State {
    public:
    //Switch states after run
    void handle1() override;
    //Keep Current State after run
    void handle2() override {
        cout << "Weekday handles request2.\n"; //Here to illustrate the changes in state
        cout << "   Today is a Weekday, you need to wake up at 7:00am and go to sleep by 11:00pm.\n";
    }
};

class Weekend : public State {
    public:
    void handle1() override {
        cout << "Weekend handles request1.\n"; //Here to illustrate the changes in state
        cout << "    Today is a Weekend, wake up and go to sleep when you want.\n";
    }
    void handle2() override {
        cout << "Weekend handles request2.\n"; //Here to illustrate the changes in state
        cout << "   Today is a weekend, wake up when you want but you need to go to sleep by 11:00pm.  Tomorrow is a Weekday.\n";
        cout << "Weekend wants to change the state of the context.\n"; //Here to illustrate the changes in state

        this->_context->transitionTo(new Weekday);
    }
};

void Weekday::handle1() {
    cout << "Weekday handles request1.\n"; //Here to illustrate the changes in state
    cout << "   Today is a weekday, you need to wake up at 7:00am and go to sleep whenever.  Tomorrow is the weekend.\n";
    cout << "Weekday wants to change the state of the context.\n";  //Here to illustrate the changes in state

    this->_context->transitionTo(new Weekend);
}

//Function that starts everything and would process the state requests
void clientCode() {
    Context *context = new Context(new Weekend);
    //Events that would change the object's internal state (Hard coded to start on a Sunday and goes until the next Sunday)
    context->request2();    //Sunday - Switches to Weekday
    context->request2();    //Monday
    context->request2();    //Tuesday
    context->request2();    //Wednesday
    context->request2();    //Thursday
    context->request1();    //Friday - Switches to Weekend
    context->request1();    //Saturday
    context->request2();    //Sunday - Switches to Weekday
    delete context;
}

int main() {
    clientCode();
    return 0;
}