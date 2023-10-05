from delivery import Delivery, delivery_registry

workflow = {
    "1": delivery_registry
}


def normal_workflow():
    d = Delivery("1")
    # Normal flow
    while True:
        state = delivery_registry[d.status]
        assert state.name == d.status
        state.transition(d)

        if d.status == "cancelled" or d.status == "delivered":
            break


def issue_cancellation_workflow():
    d = Delivery("1")
    # Issue cancelation flow
    while True:
        state = delivery_registry[d.status]
        assert state.name == d.status
        if d.status == "assign_rider":
            state.transition(d, "cancelled")
        else:
            state.transition(d)

        if d.status == "cancelled" or d.status == "delivered":
            break

def invalid_state_workflow():
    d = Delivery("1")
    # Invalid state flow
    while True:
        try:
            state = delivery_registry[d.status]
            assert state.name == d.status
            if d.status == "assign_rider":
                state.transition(d, "delivered")
            else:
                state.transition(d)

            if d.status == "cancelled" or d.status == "delivered":
                break
        except ValueError:
            print("Invalid state provided")
            break


def main():
    """
    Test different workflow scenarios
    """
    normal_workflow()

    print("\n------------------------------------------\n")

    issue_cancellation_workflow()

    print("\n------------------------------------------\n")
    
    invalid_state_workflow()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("program exited")
