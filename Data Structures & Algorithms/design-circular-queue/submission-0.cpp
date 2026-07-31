class MyCircularQueue {
public:
    MyCircularQueue(int k) {
        this->k = k;
    }
    
    bool enQueue(int value) {
        if (!isFull()){
            q.push_back(value);
            filled++;
            return true;
        }
        else return false;
    }
    
    bool deQueue() {
        if (!isEmpty()){
            pos++;
            filled--;
            return true;
        }
        else return false;
    }
    
    int Front() {
        if (!isEmpty()) return q[pos];
        else return -1;
    }
    
    int Rear() {
        if (!isEmpty()) return q[q.size()-1];
        else return -1;
    }
    
    bool isEmpty() {
        return (filled==0);
    }
    
    bool isFull() {
        return (filled==k);
    }
    private:
    int k;
    int filled = 0;
    int pos = 0;
    vector<int> q;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */