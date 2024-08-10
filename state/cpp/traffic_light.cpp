#include <chrono>
#include <iostream>
#include <thread>

#include "traffic_light.h"

// Concrete states to implement requirements
 void Red::onEnter(TrafficLight& traffic_light) {
    std::cout << "Entering the Red state." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(kRedTimeoutSec));
    std::cout << "Red light timer expired." << std::endl;
    traffic_light.set_next_state(&traffic_light.green_state);
}

void Yellow::onEnter(TrafficLight& traffic_light) {
    std::cout << "Entering the Yellow state." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(kYellowTimeoutSec));
    std::cout << "Yellow light timer expired." << std::endl;
    traffic_light.set_next_state(&traffic_light.red_state);
}

void Green::onEnter(TrafficLight& traffic_light) {
    std::cout << "Entering the Green state." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(kGreenTimeoutSec));
    std::cout << "Green light timer expired." << std::endl;
    traffic_light.set_next_state(&traffic_light.yellow_state);
}

TrafficLight::TrafficLight() {
    current_state = &red_state;
}

void TrafficLight::set_next_state(AbstractTrafficState* state) {
        current_state = state;
}

void TrafficLight::run(int duration_s) {
    auto start_time = std::chrono::high_resolution_clock::now();
    while (std::chrono::duration_cast<std::chrono::seconds>(std::chrono::high_resolution_clock::now() - start_time).count() < duration_s) {
        current_state->onEnter(*this);
    }
}

int main() {
    TrafficLight traffic_light;

    traffic_light.run(kSystemRunTimeSec);

    return 0;
};
