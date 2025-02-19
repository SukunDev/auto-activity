from AutoActivity import AutoActivity


if __name__ == "__main__":
    auto = AutoActivity(process_name=["chrome", "code"])
    try:
        auto.run()
    except KeyboardInterrupt:
        print("exit")
        