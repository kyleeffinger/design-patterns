

constexpr int kRedTimeoutSec = 4;
constexpr int kYellowTimeoutSec = 1;
constexpr int kGreenTimeoutSec = 3;
constexpr int kSystemRunTimeSec = 17;

class TrafficLight;

// State interface that all states must adhere to
class AbstractTrafficState {
    public:
        // Pure virtual method (= 0) requires child classes to override
        virtual void onEnter(TrafficLight& traffic_light) = 0;
        virtual ~AbstractTrafficState() = default;
};

class Red : public AbstractTrafficState {
    public:
        void onEnter(TrafficLight& traffic_light) override;
};

class Green : public AbstractTrafficState {
    public:
        void onEnter(TrafficLight& traffic_light) override;
};

class Yellow : public AbstractTrafficState {
    public:
        void onEnter(TrafficLight& traffic_light) override;
};

class TrafficLight {
    public:
        TrafficLight();
        ~TrafficLight() = default;

        void set_next_state(AbstractTrafficState* state);

        void run(int duration_s);

        Red red_state;
        Green green_state;
        Yellow yellow_state;
        
    private:
        AbstractTrafficState* current_state;
};