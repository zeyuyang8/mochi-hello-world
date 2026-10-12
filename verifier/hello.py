from .checks import result


def verify_input(value):
    if not value.name.strip():
        return result(False, "name must not be empty")
    return result(True, "input is valid")


def verify_output(input_value, output_value, workspace):
    if output_value.greeting != f"Hello, {input_value.name}!":
        return result(False, "the greeting does not name the requested person")
    return result(True, "greeting is made")


def verify_task(arguments, reference, workspace):
    return result(True, "the greeting is the reply; nothing is saved")
