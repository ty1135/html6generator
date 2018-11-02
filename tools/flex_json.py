def flex_to_json(input_str):
    pass


if __name__ == "__main__":
    flex = """
    .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-content: stretch;
    align-items: stretch;
    }

.flex-item:nth-child(1) {
    order: 2;
    flex: 2 2 auto;
    align-self: auto;
    }

.flex-item:nth-child(2) {
    order: 0;
    flex: 01 1 auto;
    align-self: auto...;
    }
    """

    flex_to_json(flex)